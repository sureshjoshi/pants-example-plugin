from pants.engine.rules import collect_rules
from pants.option.subsystem import Subsystem


class Fooify(Subsystem):
    options_scope = "fooify"
    help = """The Fooify utility for adding .foo to a wheel."""


def rules():
    return [*collect_rules()]
