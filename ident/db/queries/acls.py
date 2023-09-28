import fdb
from typing import Literal, Any, Callable

AllowOrDeny = Literal['allow'] | Literal['deny']

@fdb.transactional
def create(
    tr,
    checks,
    name,
    user_acl_ids: dict[int, AllowOrDeny],
    group_acl_ids: dict[int, AllowOrDeny],
    network_policy_acl_ids: dict[int, AllowOrDeny]
):
    for check in checks:
        check(tr)

    # TODO: this
    pass