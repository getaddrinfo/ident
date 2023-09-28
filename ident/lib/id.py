from snowflake import SnowflakeGenerator

EPOCH = 1688166000000

_gen = SnowflakeGenerator(1, epoch=EPOCH)

def generate() -> int:
    return next(_gen)