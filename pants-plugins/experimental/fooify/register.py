# This registers all of the plugin hooks that action our sources/dependencies
def rules():
    return []

# This registers our new plugin's target(s) (used in BUILD files)
def target_types():
    return [FooifyTarget]

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
