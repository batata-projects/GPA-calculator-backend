from typing import Any

from pydantic import BaseModel as PydanticBaseModel

from src.db.models.utils.data.ValidData import valid_data


class BaseModel(PydanticBaseModel):
    @classmethod
    def model_validate_partial(cls, data: dict[str, Any]):
        _data = {}
        for field in cls.model_fields:
            if field not in data:
                _data[field] = valid_data[f"{cls.__name__}.{field}"]
            else:
                _data[field] = data[field]
        cls.model_validate(_data)
