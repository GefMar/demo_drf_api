from pathlib import Path

import pytest
from _pytest.fixtures import fixture

fixture_filenames = ("fixtures.py", "factories.py")

pytest_plugins = [
    str(fixture_path).replace(".py", "").replace("/", ".")
    for filename in fixture_filenames
    for fixture_path in Path(".").rglob(filename)
]
