import mimetypes
from fastapi import HTTPException


def vallidation_type(content):
    get_type = mimetypes.guess_type(content)[0]
    extens_type = mimetypes.guess_extension(get_type) if get_type else None

    if extens_type not in ['.png','.jpg', '.jpeg']:
        raise HTTPException(422, "Incorect format photo")
    return 'ok'




