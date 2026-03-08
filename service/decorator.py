from fastapi import HTTPException


def field_varible(name_argument: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            name_arg = kwargs.get(name_arg)
            if not name_arg:
                raise HTTPException(400, "bad request")
            return func(*args, **kwargs)

        return wrapper

    return decorator
