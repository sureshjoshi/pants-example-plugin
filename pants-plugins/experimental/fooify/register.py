from experimental.fooify.rules import rules as fooify_rules
from experimental.fooify.target_types import FooifyTarget

# This registers all of the plugin hooks that action our sources/dependencies
def rules():
    return [*fooify_rules()]

# This registers our new plugin's target(s) (used in BUILD files)
def target_types():
    return [FooifyTarget]
