from .fixtures.auth.schemas import login_request, register_request
from .fixtures.common.session import session
from .fixtures.common.utils.types.CourseCodeStr import (
    invalid_course_code,
    valid_course_code,
)
from .fixtures.common.utils.types.CourseGradeFloat import (
    invalid_course_grade_float,
    valid_course_grade_float,
)
from .fixtures.common.utils.types.CourseNameStr import (
    invalid_course_name,
    valid_course_name,
)
from .fixtures.common.utils.types.CourseReferenceNumberStr import (
    invalid_course_reference_number,
    valid_course_reference_number,
)
from .fixtures.common.utils.types.PasswordStr import invalid_password, valid_password
from .fixtures.common.utils.types.TermStr import invalid_term, valid_term
from .fixtures.common.utils.types.UsernameStr import (
    invalid_username1,
    invalid_username2,
    valid_username,
)
from .fixtures.common.utils.types.UuidStr import invalid_uuid, valid_uuid
from .fixtures.common.utils.validators.EmailValidator import invalid_email, valid_email
from .fixtures.common.utils.validators.NameValidator import invalid_name, valid_name
from .fixtures.controller.routers._base_router import (
    router_empty,
    router_error,
    router_successful,
)
from .fixtures.controller.schemas._base_schemas import test_query
from .fixtures.db.dao._base_dao import (
    test_dao_empty,
    test_dao_error,
    test_dao_successful,
)
from .fixtures.db.models._base_model import test_object1, test_object2, test_objects
from .fixtures.db.models.available_courses import (
    available_course1,
    available_course2,
    available_courses,
    available_courses_data,
    available_courses_same_course_name,
    available_courses_same_credits,
    available_courses_same_terms,
    invalid_available_course_data,
)
from .fixtures.db.models.courses import (
    course1,
    course2,
    courses,
    courses_same_available_course_id,
    courses_same_grade,
    courses_same_user_id,
)
from .fixtures.db.models.terms import term1, term2, terms, terms_same_name
from .fixtures.db.models.users import (
    user1,
    user2,
    users,
    users_same_counted_credits,
    users_same_credits,
    users_same_first_name,
    users_same_grade,
    users_same_last_name,
)
from .fixtures.others.gotrue import gotrue_session, gotrue_user
from .fixtures.others.jwt import (
    invalid_jwt,
    invalid_signature,
    valid_jwt,
    valid_signature,
)
from .fixtures.others.tokens import (
    invalid_access_token,
    invalid_refresh_token,
    valid_access_token,
    valid_refresh_token,
)
from .fixtures.others.uuid import uuid4
