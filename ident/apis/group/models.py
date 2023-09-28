from ident.lib.validation import Strict, Lax
from ident.lib.validation.types import Snowflake


# list members
class ListMembersUrlParams(Strict):
    group_id: Snowflake