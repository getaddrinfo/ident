from typing import Annotated, Any

from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic_core import CoreSchema, PydanticCustomError, core_schema

class SnowflakePydanticAnnotation:
    @classmethod
    def __get_pydantic_core_schema__(cls, _source_type: Any, _handler: GetCoreSchemaHandler) -> CoreSchema:
        def from_string(value: str) -> Snowflake:
            """
            Coerces from a string to a Snowflake
            """
            
            try:
                value = int(value)
                assert value >= 0, 'value must be greater than 0'
                return value
            except ValueError:
                raise PydanticCustomError(
                    'snowflake_type',
                    'Value is not a valid snowflake',
                    dict()
                )
            except AssertionError:
                raise PydanticCustomError(
                    'snowflake_type',
                    'Value is not a valid snowflake',
                    dict()
                )
        
        from_string_schema = core_schema.chain_schema([
            core_schema.str_schema(),
            core_schema.no_info_plain_validator_function(from_string)
        ])

        return core_schema.json_or_python_schema(
            json_schema=from_string_schema,
            python_schema=core_schema.union_schema([
                core_schema.is_instance_schema(int),
                from_string_schema
            ])
        )
    
    @classmethod
    def __get_pydantic_json_schema__(cls, _core_schema: CoreSchema, handler: GetJsonSchemaHandler):
        return handler(core_schema.StringSchema())
    
Snowflake = Annotated[
    int,
    SnowflakePydanticAnnotation
]