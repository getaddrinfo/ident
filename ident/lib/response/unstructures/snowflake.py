from cattrs import Converter
from ..types import Snowflake

def _unstruct_snowflake(it: Snowflake) -> str:
    return str(it)

def apply(conv: Converter):
    conv.register_unstructure_hook(
        Snowflake,
        _unstruct_snowflake
    )