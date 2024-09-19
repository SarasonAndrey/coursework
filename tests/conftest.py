from typing import Any

import pytest


@pytest.fixture
def account() -> Any:
    return "73654108430135874305"


@pytest.fixture
def account1() -> Any:
    return "64686473678894779589"


@pytest.fixture
def account2() -> Any:
    return "35383033474447895560"
