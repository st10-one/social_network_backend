from .router_dep import UserDep, priveleg_token
from .orm_dep import intpk, create_at, updata_at
from .sql import sql_dep

__all__ = ["sql_dep", "UserDep", "intpk", 'priveleg_token', "create_at", "updata_at"]
