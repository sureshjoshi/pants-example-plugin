from __future__ import annotations

from typing import Iterable

from pants.engine.rules import Rule, collect_rules
from pants.option.subsystem import Subsystem


class Fooify(Subsystem):
    options_scope = "fooify"
    help = """The Fooify utility for adding .foo to a wheel."""


def rules() -> Iterable[Rule]:
    return collect_rules()
