import random
import uuid
from unittest.mock import Mock

import pytest


@pytest.fixture
def uuid4():
    return Mock(return_value=uuid.UUID(int=random.getrandbits(128)))
