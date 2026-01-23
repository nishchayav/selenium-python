from exceptions import InvalidInputError, AuthorizationError


class MarksDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if any(mark < 0 or mark > 100 for mark in value):
            raise InvalidInputError("Error: Marks should be between 0 and 100")
        setattr(obj, self.private_name, value)


class SalaryDescriptor:
    def __get__(self, obj, objtype=None):
        if not obj.is_admin:
            raise AuthorizationError("Access Denied: Salary is confidential")
        return obj._salary

    def __set__(self, obj, value):
        obj._salary = value
