from __future__ import annotations

from typing import Iterable

from experimental.fooify import subsystem
from experimental.fooify.rules import rules as fooify_rules
from experimental.fooify.target_types import FooifyTarget
from pants.engine.rules import Rule
from pants.engine.target import Target
from pants.engine.unions import UnionRule


# This registers all of the plugin hooks that action our sources/dependencies
def rules() -> Iterable[Rule | UnionRule]:
    return [*fooify_rules(), *subsystem.rules()]


# This registers our new plugin's target(s) (used in BUILD files)
def target_types() -> Iterable[type[Target]]:
    return [
        FooifyTarget,
    ]
