__all__ = ('ValidationError', 'DetailedValidationError')

class ValidationError:
    message: str
    code: str

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message

    @staticmethod
    def lookup(type: str):
        if type not in _definitions:
            raise ValueError(f"{type} not found in definitions")

        return _definitions[type]

    def __call__(self, ctx: dict) -> 'DetailedValidationError':
        return DetailedValidationError(self.code, self.message, ctx)


class DetailedValidationError:
    code: str
    message: str

    def __init__(self, code: str, message: str, ctx: dict) -> None:
        self.code = code
        self.message = message.format(**ctx)

    def to_dict(self):
        return {'code': self.code, 'message': self.message}


_definitions = {
    # assertion
    'assertion_error': ValidationError("ASSERTION_FAILED", "Assertion failed on value"),

    # bool
    'bool_parsing': ValidationError("TYPE_CAST_BOOl", "Not a valid bool"),
    'bool_type': ValidationError("TYPE_CAST_BOOL", "Not a valid bool"),

    # bytes
    'bytes_too_long': ValidationError("BYTES_INVALID_LENGTH", "Value is too long {max_length}"),
    'bytes_too_short': ValidationError("BYTES_INVALID_LENGTH", "Value is too short"),
    'bytes_type': ValidationError("TYPE_CAST_BYTES", "Not valid bytes"),

    # callable
    'callable_type': ValidationError("TYPE_CAST_CALLABLE", "Not a valid callable"),

    # dataclass
    'dataclass_exact_type': ValidationError("TYPE_CAST_DATACLASS", "Not valid for dataclass"),
    'dataclass_type': ValidationError("TYPE_CAST_DATACLASS", "Not valid for dataclass"),

    # date
    'date_from_datetime_inexact': ValidationError("TYPE_CAST_DATE", "Date must be exactly midnight"),
    'date_future': ValidationError("DATE_NOT_IN_FUTURE", "Not in the future"),
    'date_parsing': ValidationError("TYPE_CAST_DATE", "Not a valid date"),
    'date_past': ValidationError("DATE_NOT_IN_PAST", "Not in the past"),
    'date_type': ValidationError("TYPE_CAST_DATE", "Not a valid date"),

    # datetime
    'datetime_future': ValidationError("DATETIME_NOT_IN_FUTURE", "Not in the future"),
    'datetime_object_invalid': ValidationError("TYPE_CAST_DATETIME", "Not a valid datetime"),
    'datetime_parsing': ValidationError("TYPE_CAST_DATETIME", "Not a valid datetime"),
    'datetime_past': ValidationError("DATETIME_NOT_IN_PAST", "Not in the past"),
    'datetime_type': ValidationError("TYPE_CAST_DATETIME", "Not a valid datetime"),

    # decimal
    'decimal_max_digits': ValidationError("FLOAT_INVALID_NUM_DIGITS", "Too many digits"),
    'decimal_max_places': ValidationError("FLOAT_INVALID_NUM_PLACES", "Too many places"),
    'decimal_parsing': ValidationError("TYPE_CAST_FLOAT", "Not a valid float"),
    'decimal_whole_digits': ValidationError("FLOAT_INVALID_VALUE", "Too many whole digits"),

    # dict
    'dict_type': ValidationError("TYPE_CAST_OBJECT", "Not a valid object"),

    # enum
    'enum': ValidationError("TYPE_CAST_ENUM", "Not a valid enum member; Expected one of {expected}"),

    # extra
    'extra_forbidden': ValidationError("UNKNOWN_FIELD", "Not a recognised field"),

    # finite_number
    'finite_number': ValidationError("TYPE_CAST_FLOAT", "Not a valid float"),

    # float
    'float_parsing': ValidationError("TYPE_CAST_FLOAT", "Not a valid float"),
    'float_type': ValidationError("TYPE_CAST_FLOAT", "Not a valid float"),

    # frozen field
    'frozen_field': ValidationError("FIELD_FROZEN", "Field is frozen"),
    'frozen_instance': ValidationError("INSTANCE_FROZEN", "Instance is frozen"),

    # frozen set
    'frozen_set_type': ValidationError("TYPE_CAST_FROZEN_SET", "Not a valid frozen set"),

    # attrs
    'get_attribute_error': ValidationError("GET_ATTRIBUTE", "(internal)"),

    # greater than
    'greater_than': ValidationError("VALUE_TOO_SMALL", "Must be greater than {gt}"),
    'greater_than_equal': ValidationError("VALUE_TOO_SMALL", "Must be greater than or equal to {ge}"),

    # int
    'int_from_float': ValidationError("TYPE_CAST_INT", "Not a valid integer"),
    'int_parsing': ValidationError("TYPE_CAST_INT", "Not a valid integer"),
    'int_parsing_size': ValidationError("TYPE_CAST_INT", "Not a valid integer"),
    'int_type': ValidationError("TYPE_CAST_INT", "Not a valid integer"),

    # invalid_key
    'invalid_key': ValidationError("TYPE_CAST_DICT_KEY", "Not a valid string"),

    # instance
    'is_instance_of': ValidationError("INVALID_INSTANCE", "Wrong type"),

    # subclass
    'is_subclass_of': ValidationError("NOT_A_SUBCLASS", "Not a subclass"),

    # iterable
    'iterable_type': ValidationError("TYPE_CAST_ITERABLE", "Not a valid iterable"),
    'iteration_error': ValidationError("INVALID_ITERATION", "Iteration failed"),

    # json
    'json_invalid': ValidationError("TYPE_CAST_JSON", "Not a valid json string"),
    'json_type': ValidationError("TYPE_CAST_JSON", "Invalid JSON"),

    # less than
    'less_than': ValidationError("VALUE_TOO_LARGE", "Must be less than {lt}"),
    'less_than_equal': ValidationError("VALUE_TOO_LARGE", "Must be less than or equal to {le}"),

    # list
    'list_type': ValidationError("TYPE_CAST_LIST", "Not a valid list"),

    # literal
    'literal_error': ValidationError("INVALID_LITERAL", "Not a valid literal"),

    # mapping
    'mapping_type': ValidationError("INTERNAL", "Mapping protocol failure"),

    # missing
    'missing': ValidationError("FIELD_REQUIRED", "Field is required"),
    'missing_argument': ValidationError("ARGUMENT_REQUIRED", "Argument required"),
    'missing_keyword_only_argument': ValidationError("ARGUMENT_REQUIRED", "Argument required"),
    'missing_potential_only_argument': ValidationError("ARGUMENT_REQUIRED", "Argument required"),

    # models
    'model_attributes_type': ValidationError("TYPE_CAST_EXTRACTABLE", "Cannot extract from provided type"),
    'model_type': ValidationError("TYPE_CAST_MODEL", "Not a valid model"),
    'multiple_argument_values': ValidationError("TOO_MANY_ARGS", "Too many arguments given"),

    # multiple of
    'multiple_of': ValidationError("VALUE_MULTIPLE_OF", "Not a multiple"),

    # attribute
    'no_such_attribute': ValidationError("FIELD_UNKNOWN", "Not a known field"),

    # none
    'none_required': ValidationError("TYPE_CAST_NONE", "Not a valid none"),
    'none_disallowed_for_optional': ValidationError('FIELD_REQUIRED', "Value cannot be None if set"),

    # recursion
    'recursion_loop': ValidationError("INTERNAL_RECURSION", "Recursion detected..."),

    # set
    'set_type': ValidationError("TYPE_CAST_SET", "Not a valid set"),

    # string
    'string_pattern_mismatch': ValidationError("STRING_NOT_MATCHES", "Does not match somethiong >?>"),
    'string_sub_type': ValidationError("TYPE_CAST_STRING", "Not a valid string"),
    'string_too_long': ValidationError("VALUE_TOO_LONG", "Value must be shorter than {max_length}"),
    'string_too_short': ValidationError("VALUE_TOO_SHORT", "Value must be longer than {min_length}"),
    'string_type': ValidationError("TYPE_CAST_STRING", "Not a valid string"),
    'string_unicode': ValidationError("TYPE_CAST_STRING", "Not a valid unicode string"),

    # time delta
    'time_delta_parsing': ValidationError("TYPE_CAST_TIMEDELTA", "Not a valid time delta"),
    'time_delta_type': ValidationError("TYPE_CAST_TIMEDELTA", "Not a valid time delta"),

    # time
    'time_parsing': ValidationError("TYPE_CAST_TIME", "Not a valid time"),
    'time_type': ValidationError("TYPE_CAST_TIME", "Not a valid time"),

    # timezone
    'timezone_aware': ValidationError("TYPE_CAST_DATETIME", "Must specify timezone"),
    'timezone_naive': ValidationError("TYPE_CAST_NAIVE_DATETIME", "Must not specify timezone"),

    # list length
    'too_long': ValidationError("VALUE_TOO_LONG", "Value must contain less than {max_length} items"),
    'too_short': ValidationError("VALUE_TOO_SHORT", "Value must contain at least {min_length} items"),

    # tuple
    'tuple_type': ValidationError("TYPE_CAST_TUPLE", "Not a valid tuple"),

    # unexpected argument
    'unexpected_keyword_argument': ValidationError("INTERNAL", "Unexpected keyword argument"),
    'unexpected_positional_argument': ValidationError("INTERNAL", "Unexpected positional argument"),

    # union
    'union_tag_valid': ValidationError("UNION_INVALID_DISCRIMINATOR", "Not a valid union discriminator, expected one of {TODO}"),
    'union_tag_not_found': ValidationError("UNION_INVALID_DISCRIMINATOR", "Not a valid union discriminator, expected one of {TODO}"),

    # url
    'url_parsing': ValidationError("TYPE_CAST_URL", "Not a well-formed URL"),
    'url_scheme': ValidationError("URL_INVALID_SCHEME", "URL has invalid scheme"),
    'url_syntax_violation': ValidationError("TYPE_CAST_URL", "Not a well-formed URL"),
    'url_too_long': ValidationError("URL_TOO_LONG", "Value must be less than 2083 characters"),
    'url_type': ValidationError("TYPE_CAST_URL", "Not a valid URL"),

    # uuid
    'uuid_parsing': ValidationError("TYPE_CAST_UUID", "Not a valid UUID"),
    'uuid_type': ValidationError("TYPE_CAST_UUID", "Not a valid UUID"),
    'uuid_version': ValidationError("UUID_WRONG_VERSION", "Invalid UUID version"),
    'value_error': ValidationError("VALUE_ERROR", "Value Error occurred"),

    ## custom types
    # snowflake
    'snowflake_type': ValidationError('TYPE_CAST_SNOWFLAKE', "Not a valid Snowflake")
}