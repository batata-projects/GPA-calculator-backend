from supabase import Client

from src.db.models.users import User
from src.db.models.utils import EmailStr, UuidStr
from src.db.tables import SupabaseTables


class UserDAO:
    def __init__(self, client: Client):
        self.client = client

    def get_user_by_id(self, user_id: UuidStr):
        data = (
            self.client.table(SupabaseTables.USERS)
            .select("*")
            .eq("id", user_id)
            .execute()
        )
        if not data.data:
            return None
        return User.model_validate(data.data[0])

    def get_user_by_email(self, email: EmailStr):
        data = (
            self.client.table(SupabaseTables.USERS)
            .select("*")
            .eq("email", email)
            .execute()
        )
        if not data.data:
            return None
        return User.model_validate(data.data[0])

    def get_user_by_username(self, username: str):
        data = (
            self.client.table(SupabaseTables.USERS)
            .select("*")
            .eq("username", username)
            .execute()
        )
        if not data.data:
            return None
        return User.model_validate(data.data[0])

    def create_user(self, user: User):
        data = (
            self.client.table(SupabaseTables.USERS).insert(user.model_dump()).execute()
        )
        if not data.data:
            return None
        return User.model_validate(data.data[0])

    def update_user(self, user_id: UuidStr, user_data: dict):
        self.client.table(SupabaseTables.USERS).update(user_data).eq(
            "id", user_id
        ).execute()

    def delete_user(self, user_id: UuidStr):
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
