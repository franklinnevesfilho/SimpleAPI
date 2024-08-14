from franklin_fastapi_extension import DTO
import re


@DTO
class MockDTO:
    message: str


@DTO
class ValidationTest:
    message: str

    VALIDATIONS = {
        'message': re.compile(r'^[a-zA-Z]+$')
    }
