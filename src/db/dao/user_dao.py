from typing import Optional, Union

from pydantic import EmailStr, NonNegativeFloat, NonNegativeInt
from supabase import Client

from src.common.utils.types import UsernameStr, UuidStr
from src.db.models import User
from src.db.tables import SupabaseTables


class UserDAO:
    def __init__(self, client: Client) -> None:
        self.client = client

    def get_user_by_id(self, user_id: UuidStr) -> Optional[User]:
        data = (
            self.client.table(SupabaseTables.USERS)
            .select("*")
            .eq("id", user_id)
            .execute()
        )
        if not data.data:
            return None
        return User.model_validate(data.data[0])

    def get_user_by_email(self, email: EmailStr) -> Optional[User]:
        data = (
            self.client.table(SupabaseTables.USERS)
            .select("*")
            .eq("email", email)
            .execute()
        )
        if not data.data:
            return None
        return User.model_validate(data.data[0])

    def get_user_by_username(self, username: str) -> Optional[User]:
        data = (
            self.client.table(SupabaseTables.USERS)
            .select("*")
            .eq("username", username)
            .execute()
        )
        if not data.data:
            return None
        return User.model_validate(data.data[0])

    def create_user(
        self,
        user_data: dict[
            str,
            Union[
                UuidStr, EmailStr, UsernameStr, str, NonNegativeInt, NonNegativeFloat
            ],
        ],
    ) -> Optional[User]:
        User.model_validate(user_data)
        data = self.client.table(SupabaseTables.USERS).insert(user_data).execute()
        if not data.data:
            return None
        return User.model_validate(data.data[0])

    def update_user(
        self,
        user_id: UuidStr,
        user_data: dict[
            str,
            Union[
                UuidStr,
                EmailStr,
                UsernameStr,
                str,
                NonNegativeInt,
                NonNegativeFloat,
                None,
            ],
        ],
    ) -> Optional[User]:
        User.model_validate_partial(user_data)
        data = (
            self.client.table(SupabaseTables.USERS)
            .update(user_data)
            .eq("id", user_id)
            .execute()
        )
        if not data.data:
            return None
        return User.model_validate(data.data[0])

    def delete_user(self, user_id: UuidStr) -> Optional[User]:
        data = (
            self.client.table(SupabaseTables.USERS).delete().eq("id", user_id).execute()
        )
        if not data.data:
            return None
        return User.model_validate(data.data[0])

    def get_users_by_query(
        self,
        id: Optional[UuidStr] = None,
        username: Optional[UsernameStr] = None,
        email: Optional[EmailStr] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        credits: Optional[NonNegativeInt] = None,
        counted_credits: Optional[NonNegativeInt] = None,
        grade: Optional[NonNegativeFloat] = None,
    ) -> list[User]:
        queries = self.client.table(SupabaseTables.USERS).select("*")
        if id:
            queries = queries.eq("id", id)
        if username:
            queries = queries.eq("username", username)
        if email:
            queries = queries.eq("email", email)
        if first_name:
            queries = queries.eq("first_name", first_name)
        if last_name:
            queries = queries.eq("last_name", last_name)
        if credits:
            queries = queries.eq("credits", credits)
        if counted_credits:
            queries = queries.eq("counted_credits", counted_credits)
        if grade:
            queries = queries.eq("grade", grade)
        data = queries.execute()
        if not data.data:
            return []
        return [User.model_validate(user) for user in data.data]
