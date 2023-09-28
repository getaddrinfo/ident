import inspect

def map_type_to_kwargs(func):
    signature = inspect.signature(func)

    parameters = signature.parameters.values()

    # [type] -> set(keys)
    type_to_kwargs_key: dict[type, set[str]] = dict()

    for param in parameters:
        # flask is probably going to handle this if this is the case
        if param.annotation is None:
            continue

        ty = param.annotation

        if ty in type_to_kwargs_key:
            type_to_kwargs_key[ty].add(param.name)
        else:
            type_to_kwargs_key[ty] = { param.name }

    return type_to_kwargs_key

def function_name(f):
    mod = inspect.getmodule(f)

    if mod is not None:
        return f'{mod.__name__}.{f.__name__}'

    return f.__name__