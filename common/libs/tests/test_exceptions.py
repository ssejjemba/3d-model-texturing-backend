from libs.error_handling.exceptions import BaseException, FieldError, FieldErrorsMixin
from libs.error_handling.remote import BadRequestError


def test_base_exception():
    class FooError(BaseException):
        INVALID_FORMAT = 'invalid_format'

    foo = FooError('Oops', code=FooError.INVALID_FORMAT, data=dict(a=1))

    assert foo.message == 'Oops'
    assert foo.code == FooError.INVALID_FORMAT
    assert foo.data == {'a': 1}


def test_field_errors():
    class FooFieldError(FieldErrorsMixin, BaseException):
        pass

    field_errors = [
        FieldError('foo', 'Oops', 'invalid'),
        FieldError('bar', 'Great', 'too_short'),
    ]
    foo = FooFieldError(field_errors=field_errors)

    assert foo.field_errors == field_errors


def test_remote_exceptions():
    error = BadRequestError(
        'Bad', code='bad'
    )
    assert error.message == 'Bad'
    assert error.code == 'bad'
