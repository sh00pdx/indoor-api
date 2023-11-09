
from autofact_lib_python_error_handler.exceptions.app_error import AppError

import pytest

class TestAppError:
    # Tests that the serialize_errors method is called without errors.
    def test_serialize_errors_happy_path(self):
        # Arrange
        class CustomError(AppError):
            def serialize_errors(self):
                return "Serialized error message"
        error = CustomError()

        # Act
        serialized_error = error.serialize_errors()

        # Assert
        assert serialized_error == "Serialized error message"