from datetime import datetime
from typing import Annotated

from sqlalchemy.orm import mapped_column
from sqlalchemy import func


create_at = Annotated[datetime, mapped_column(server_default=func.now(),)]
updata_at = Annotated[datetime, mapped_column(server_default=func.now(), onupdate=func.now())]
intpk = Annotated[int, mapped_column(primary_key=True)]
