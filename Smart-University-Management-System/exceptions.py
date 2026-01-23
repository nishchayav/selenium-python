class UniversityError(Exception):
    def __init__(self, message="University system error"):
        super().__init__(message)


class DuplicateRecordError(UniversityError):
    pass


class InvalidInputError(UniversityError):
    pass


class FileAccessError(UniversityError):
    pass


class AuthorizationError(UniversityError):
    pass



class DuplicateRecordError(UniversityError):
    pass


class InvalidInputError(UniversityError):
    pass


class FileAccessError(UniversityError):
    pass


class AuthorizationError(UniversityError):
    pass
