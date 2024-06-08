from typing import Optional, Union

from pydantic import EmailStr, NonNegativeFloat, NonNegativeInt
from supabase import Client

from src.common.utils.types.UsernameStr import UsernameStr
from src.common.utils.types.UuidStr import UuidStr
from src.db.models.users import User
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

    def get_all_users(self) -> list[User]:
        data = self.client.table(SupabaseTables.USERS).select("*").execute()
        if not data.data:
            return []
        return [User.model_validate(user) for user in data.data]
