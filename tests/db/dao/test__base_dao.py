import pytest

from tests.fixtures.db.dao._base_dao import TestDAO
from tests.fixtures.db.models._base_model import TestObject


class TestBaseDAO:
    class TestGetByQuery:
        def test_get_test_object_by_query_successful(
            self, test_object1: TestObject, test_dao_successful: TestDAO
        ) -> None:
            result = test_dao_successful.get_by_query(
                id=test_object1.id, name=test_object1.name
            )

            assert result == [test_object1]

        def test_get_test_object_by_query_empty(self, test_dao_empty: TestDAO) -> None:
            result = test_dao_empty.get_by_query()

            assert result == []

        def test_get_test_object_by_query_error(self, test_dao_error: TestDAO) -> None:
            with pytest.raises(Exception):
                test_dao_error.get_by_query()

    class TestGetById:
        def test_get_test_object_by_id_successful(
            self, test_object1: TestObject, test_dao_successful: TestDAO
        ) -> None:
            assert test_object1.id is not None

            result = test_dao_successful.get_by_id(test_object1.id)

            assert result == test_object1

        def test_get_test_object_by_id_empty(self, test_dao_empty: TestDAO) -> None:
            result = test_dao_empty.get_by_id("")

            assert result is None

        def test_get_test_object_by_id_error(self, test_dao_error: TestDAO) -> None:
            with pytest.raises(Exception):
                test_dao_error.get_by_id("")

    class TestCreate:
        def test_create_test_object_successful(
            self, test_object1: TestObject, test_dao_successful: TestDAO
        ) -> None:
            result = test_dao_successful.create(test_object1.model_dump())

            assert result == test_object1

        def test_create_test_object_error(self, test_dao_error: TestDAO) -> None:
            with pytest.raises(Exception):
                test_dao_error.create({})

    class TestCreateMany:
        def test_create_many_test_object_successful(
            self, test_object1: TestObject, test_dao_successful: TestDAO
        ) -> None:
            result = test_dao_successful.create_many([test_object1.model_dump()])

            assert result == [test_object1]

        def test_create_many_test_object_error(self, test_dao_error: TestDAO) -> None:
            with pytest.raises(Exception):
                test_dao_error.create_many([{}])

    class TestUpdate:
        def test_update_test_object_successful(
            self, test_object1: TestObject, test_dao_successful: TestDAO
        ) -> None:
            assert test_object1.id is not None

            result = test_dao_successful.update(
                test_object1.id, test_object1.model_dump()
            )

            assert result == test_object1

        def test_update_test_object_error(self, test_dao_error: TestDAO) -> None:
            with pytest.raises(Exception):
                test_dao_error.update("", {})

    class TestDelete:
        def test_delete_test_object_successful(
            self, test_object1: TestObject, test_dao_successful: TestDAO
        ) -> None:
            assert test_object1.id is not None

            result = test_dao_successful.delete(test_object1.id)

            assert result == test_object1

        def test_delete_test_object_error(self, test_dao_error: TestDAO) -> None:
            with pytest.raises(Exception):
                test_dao_error.delete("")
