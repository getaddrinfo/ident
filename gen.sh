#!/bin/bash

# runs protoc on `/defs`, writing to `ident/db/buf` w/ proto stub + pyi definitions
protoc -I=./defs --python_out=ident/db/buf --pyi_out ident/db/buf $(find ./defs -type f -name '*.proto')