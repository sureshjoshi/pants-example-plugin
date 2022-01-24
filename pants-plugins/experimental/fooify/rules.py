from dataclasses import dataclass

from pants.core.goals.package import BuiltPackage, PackageFieldSet
from pants.engine.fs import (
    CreateDigest,
    Digest,
)
from pants.engine.rules import Get, collect_rules, rule
from pants.engine.target import Dependencies
from pants.engine.unions import UnionRule
from pants.util.logging import LogLevel

@dataclass(frozen=True)
class FooifyFieldSet(PackageFieldSet):
    required_fields = (Dependencies,)

    dependencies: Dependencies


@rule(level=LogLevel.DEBUG)
async def run_fooify() -> BuiltPackage:
    # Make a rule that can compile safely
    empty_digest = await Get(Digest, CreateDigest())
    return BuiltPackage(
        digest=empty_digest,
        artifacts=(),
    )

def rules():
    return [*collect_rules(), UnionRule(PackageFieldSet, FooifyFieldSet)]
