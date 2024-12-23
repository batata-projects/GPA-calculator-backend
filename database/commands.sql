-- creating users table
create table
  public.users (
    first_name text not null,
    last_name text not null,
    email text not null,
    id uuid not null,
    constraint users_pkey primary key (id),
    constraint users_email_key unique (email),
    constraint users_id_fkey foreign key (id) references auth.users (id)
  ) tablespace pg_default;

-- creating courses table
CREATE TABLE public.courses (
    grade DOUBLE PRECISION NULL,
    user_id UUID NOT NULL,
    id UUID NOT NULL DEFAULT gen_random_uuid(),
    graded BOOLEAN NOT NULL,
    subject TEXT NOT NULL,
    course_code TEXT NOT NULL,
    credits SMALLINT NOT NULL,
    term INTEGER NOT NULL,
    CONSTRAINT courses_pkey PRIMARY KEY (id),
    CONSTRAINT unique_course_per_term UNIQUE (user_id, subject, course_code, term),
    CONSTRAINT courses_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) TABLESPACE pg_default;

-- Update user when course updated (not implemented)
CREATE OR REPLACE FUNCTION update_user_when_update_courses()
RETURNS TRIGGER AS $$
DECLARE
    max_grade INT;
    max_grade_credits INT;

    insertt BOOLEAN := FALSE;
BEGIN
   PERFORM set_config('search_path', 'public', true);

    IF pg_trigger_depth() > 1 THEN
        RETURN NEW;
    END IF;
    IF TG_OP = 'INSERT' THEN
        SELECT EXISTS (
            SELECT 1 FROM public.courses c
            WHERE c.user_id = NEW.user_id
              AND c.subject = NEW.subject
              AND c.course_code = NEW.course_code
              AND c.credits = NEW.credits
              AND c.grade >-1
              AND c.id != NEW.id
        ) INTO insertt;

        IF insertt THEN
            SELECT c.grade, c.grade * c.credits
            INTO max_grade, max_grade_credits
            FROM public.courses c
            WHERE c.user_id = NEW.user_id
            AND c.subject = NEW.subject
            AND c.course_code = NEW.course_code
            AND c.credits = NEW.credits
            AND c.grade > -1
            AND c.id != NEW.id
            ORDER BY c.grade DESC, c.term DESC
            LIMIT 1;


            IF max_grade < NEW.grade and new.grade != -1 and new.graded is true THEN
                UPDATE public.users
                SET grade = grade + (NEW.grade * NEW.credits) - max_grade_credits
                WHERE id = NEW.user_id;
            ELSE
                RETURN NULL;
            END IF;
        ELSE

            IF NEW.graded IS TRUE AND NEW.grade IS NOT NULL and new.grade != -1 THEN
                UPDATE public.users
                SET grade = COALESCE(grade, 0) + (NEW.grade * NEW.credits),
                    credits = COALESCE(credits, 0) + NEW.credits,
                    counted_credits = COALESCE(counted_credits, 0) + NEW.credits
                WHERE id = NEW.user_id;
            ELSIF NEW.graded IS FALSE AND (NEW.grade = 1 OR NEW.grade = 0) THEN
                UPDATE public.users
                SET credits = COALESCE(credits, 0) + NEW.credits
                WHERE id = NEW.user_id;
            END IF;
        END IF;

    ELSIF TG_OP = 'UPDATE' THEN
          SELECT EXISTS (
            SELECT 1 FROM public.courses c
            WHERE c.user_id = NEW.user_id
              AND c.subject = NEW.subject
              AND c.course_code = NEW.course_code
              AND c.credits = NEW.credits
              AND c.grade != -1
              AND c.id != NEW.id
        ) INTO insertt;

        IF insertt THEN
            SELECT c.grade, c.grade * c.credits
            INTO max_grade, max_grade_credits
            FROM public.courses c
            WHERE c.user_id = NEW.user_id
            AND c.subject = NEW.subject
            AND c.course_code = NEW.course_code
            AND c.credits = NEW.credits
            AND c.grade != -1
            AND c.id != NEW.id
            ORDER BY c.grade DESC, c.term DESC
            LIMIT 1;

                IF NEW.grade > max_grade and old.grade < max_grade AND NEW.grade !=-1 THEN
                    UPDATE users
                    SET grade = COALESCE(grade + (NEW.grade * NEW.credits) - max_grade_credits)
                    WHERE id = NEW.user_id;

                ELSIF NEW.grade < max_grade and old.grade > max_grade AND NEW.grade !=-1 THEN
                    UPDATE users
                    SET grade = COALESCE(grade - (OLD.grade * OLD.credits) + max_grade_credits)
                    WHERE id = NEW.user_id;
                ELSIF old.grade > max_grade and new.grade > max_grade AND NEW.grade !=-1 THEN
                    UPDATE users
                    SET grade = COALESCE(grade - (OLD.grade * OLD.credits) - (NEW.grade * NEW.credits))
                    WHERE id = NEW.user_id;
                ELSE
                    return NULL;
                END IF;
        ELSE
            IF OLD.graded IS TRUE AND NEW.graded IS FALSE AND OLD.grade IS NOT NULL AND (OLD.grade != -1) THEN
                    UPDATE users
                    SET grade = COALESCE(grade - (OLD.grade * OLD.credits), 0),
                        credits = COALESCE(credits - OLD.credits, 0),
                        counted_credits = COALESCE(counted_credits - OLD.credits, 0)
                    WHERE id = OLD.user_id;

            ELSIF OLD.graded IS FALSE AND NEW.graded IS TRUE  AND OLD.grade IS NOT NULL AND (OLD.grade != -1) THEN
                UPDATE users
                SET credits = COALESCE(credits - NEW.credits, 0)
                    WHERE id = NEW.user_id;
                    RETURN NEW;
            END IF;


            IF NEW.graded IS TRUE AND old.graded IS TRUE AND NEW.grade IS NOT NULL AND NEW.grade != -1 AND OLD.grade IS NOT NULL AND (OLD.grade != -1) THEN
                UPDATE users
                SET grade = grade + (NEW.grade * NEW.credits) - (OLD.grade * OLD.credits)
                WHERE id = NEW.user_id;
                RETURN NEW;
            END IF;

            IF OLD.grade IS NOT NULL AND (NEW.grade IS NULL or New.grade = -1) AND new.graded IS TRUE and old.graded is true THEN
                UPDATE users
                SET grade = COALESCE(grade - (OLD.grade * OLD.credits), 0),
                    credits = COALESCE(credits - OLD.credits, 0),
                    counted_credits = COALESCE(counted_credits - OLD.credits, 0)
                WHERE id = OLD.user_id;

            ELSIF OLD.grade IS NULL AND NEW.grade IS NOT NULL AND NEW.grade != -1 AND new.graded IS TRUE and old.graded IS TRUE THEN
                UPDATE users
                SET grade = COALESCE(grade + (NEW.grade * NEW.credits), 0),
                    credits = COALESCE(credits + NEW.credits, 0),
                    counted_credits = COALESCE(counted_credits + NEW.credits, 0)
                WHERE id = NEW.user_id;
            END IF;

            IF OLD.graded IS FALSE THEN
                IF (OLD.grade = 1 OR OLD.grade = 0) AND (NEW.grade IS NULL or NEW.grade = -1) THEN
                    UPDATE users
                    SET credits = COALESCE(credits - OLD.credits, 0)
                    WHERE id = OLD.user_id;
                ELSIF OLD.grade IS NULL AND (NEW.grade = 1 OR NEW.grade = 0) THEN
                    UPDATE users
                    SET credits = COALESCE(credits + NEW.credits, 0)
                    WHERE id = NEW.user_id;
                END IF;
            END IF;
        END IF;

    ELSIF TG_OP = 'DELETE' THEN
        IF EXISTS (SELECT 1 FROM public.courses c WHERE c.user_id = OLD.user_id
                                            AND c.subject = OLD.subject
                                            AND C.GRADE != -1
                                            AND c.course_code = OLD.course_code
                                            AND c.credits = OLD.credits) AND OLD.grade != -1 THEN
            IF (SELECT c.grade FROM public.courses c WHERE c.user_id = OLD.user_id
                                                AND c.subject = OLD.subject
                                                AND C.GRADE != -1
                                                AND c.course_code = OLD.course_code
                                                AND c.credits = OLD.credits) < OLD.grade THEN
                UPDATE public.users
                SET grade = grade + (SELECT c.grade * c.credits FROM public.courses c WHERE c.user_id = OLD.user_id
                                                                                AND c.subject = OLD.subject
                                                                                AND C.GRADE != -1
                                                                                AND c.course_code = OLD.course_code
                                                                                AND c.credits = OLD.credits)-(OLD.grade * OLD.credits)
                WHERE id = OLD.user_id;

            ELSIF (SELECT c.grade FROM public.courses c WHERE c.user_id = OLD.user_id
                                                    AND c.subject = OLD.subject
                                                    AND c.course_code = OLD.course_code
                                                    AND c.credits = OLD.credits) IS NULL  AND OLD.grade IS NOT NULL AND OLD.grade !=-1 AND OLD.graded IS TRUE THEN
                UPDATE public.users
                SET grade = grade - (OLD.grade * OLD.credits),
                    credits = COALESCE(credits - OLD.credits, 0),
                    counted_credits = COALESCE(counted_credits - OLD.credits, 0)
                WHERE id = OLD.user_id;

            ELSIF (SELECT c.grade FROM public.courses c WHERE c.user_id = OLD.user_id
                                                    AND c.subject = OLD.subject
                                                    AND c.course_code = OLD.course_code
                                                    AND c.credits = OLD.credits)>OLD.grade THEN return null;
            END IF;

        ELSE
            IF OLD.graded IS TRUE AND (OLD.grade IS NOT NULL AND OLD.grade != -1) THEN
                UPDATE public.users
                SET grade = COALESCE(grade - (OLD.grade * OLD.credits), 0),
                    credits = COALESCE(credits - OLD.credits, 0),
                    counted_credits = COALESCE(counted_credits - OLD.credits, 0)
                WHERE id = OLD.user_id;
            ELSIF OLD.graded IS FALSE AND (OLD.grade = 1 OR OLD.grade = 0) THEN
                UPDATE public.users
                SET credits = COALESCE(credits - OLD.credits, 0)
                WHERE id = OLD.user_id;
            END IF;
        END IF;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Resets grade when new graded type is different than the old type
CREATE OR REPLACE FUNCTION reset_grade()
RETURNS TRIGGER AS $$
BEGIN
  IF OLD.graded IS DISTINCT FROM NEW.graded THEN
    NEW.grade := NULL;
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER grade_reset
BEFORE UPDATE ON courses
FOR EACH ROW
EXECUTE FUNCTION reset_grade();

-- Create and delete user profile
create or replace function create_profile_for_user()
returns trigger
language plpgsql
security definer set search_path = ''
as $$
begin
    if new.email_confirmed_at IS NOT NULL AND old.email_confirmed_at IS null then
      insert into public.users (id, email,first_name,last_name)
      values (new.id, new.email, new.raw_user_meta_data ->> 'first_name', new.raw_user_meta_data ->> 'last_name');
    end if;
  return new;
end;
$$;

create or replace function delete_profile_for_user()
returns trigger
language plpgsql
security definer set search_path = ''
as $$
begin
    delete from auth.users where id = OLD.id;
    return null;
end;

