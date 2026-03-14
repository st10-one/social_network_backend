import datetime
from typing import Annotated

from sqlalchemy.orm import mapped_column



create_at = Annotated[datetime.datetime, mapped_column(server_default=datetime.datetime.utcnow,)]
updata_at = Annotated[datetime.datetime, mapped_column(server_default=datetime.datetime.utcnow, onupdate=datetime.datetime.now)]
intpk = Annotated[int, mapped_column(primary_key=True)]
