from pants.engine.target import (
    COMMON_TARGET_FIELDS,
    Target,
)

class FooifyTarget(Target):
    alias = "fooify"
    core_fields = (
        *COMMON_TARGET_FIELDS,
    )
    help = "The `fooify` target will take in a wheel dependency and add a .foo extension to the end."