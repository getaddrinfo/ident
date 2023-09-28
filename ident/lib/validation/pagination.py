from .base import Lax

from typing import Annotated
from annotated_types import Interval, Ge

class PaginationQueryParams(Lax):
    limit: Annotated[int, Interval(ge=1, le=100)] = 25
    next: Annotated[int, Ge(0)] = 0