from http import HTTPStatus


class EmailError(Exception):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.message = {'error': 'Wrong email format'}
        self.code = HTTPStatus.NOT_ACCEPTABLE

class PhoneError(Exception):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.message = {'error': 'Wrong phone format'}
        self.code = HTTPStatus.NOT_ACCEPTABLE