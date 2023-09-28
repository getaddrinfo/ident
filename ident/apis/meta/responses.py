from ident.lib.response import define

@define
class GetMeta:
    snowflake_epoch_millis: int
    routes: dict[str, str]