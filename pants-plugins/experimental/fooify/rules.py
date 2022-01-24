from dataclasses import dataclass
import logging

from pants.core.goals.package import BuiltPackage, BuiltPackageArtifact, PackageFieldSet
from pants.engine.fs import (
    CreateDigest,
    Digest,
    DigestEntries,
    FileEntry
)
from pants.engine.rules import Get, MultiGet, collect_rules, rule
from pants.engine.target import (
    DependenciesRequest,
    FieldSetsPerTarget,
    FieldSetsPerTargetRequest,
    Targets,
)
from pants.engine.unions import UnionRule
from pants.util.logging import LogLevel

from experimental.fooify.subsystem import Fooify
from experimental.fooify.target_types import FooifyDependenciesField

logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class FooifyFieldSet(PackageFieldSet):
    required_fields = (FooifyDependenciesField,)

    dependencies: FooifyDependenciesField


@rule(level=LogLevel.DEBUG)
async def run_fooify(fooify: Fooify, field_set: FooifyFieldSet) -> BuiltPackage:
    logger.info(f"Incoming field set: {field_set}")

    # What is Get?
    # https://www.pantsbuild.org/docs/rules-api-concepts#await-get---awaiting-results-in-a-rule-body
    targets = await Get(Targets, DependenciesRequest(field_set.dependencies))
    
    # NOTE: This is hardcoded for this example
    wheel_target = targets[0]

    # All of the following is to eventually unwrap to get the wheel file itself
    packages = await Get(
        FieldSetsPerTarget,
        FieldSetsPerTargetRequest(PackageFieldSet, [wheel_target]),
    )
    wheel_field_set = packages.field_sets[0]
    wheel_package = await Get(BuiltPackage, PackageFieldSet, wheel_field_set) 
    
    # What is a Digest?
    # https://www.pantsbuild.org/docs/rules-api-file-system#core-abstractions-digest-and-snapshot

    # Grab the Wheel file entry, and re-created it with the .foo extension
    digest_entries = await Get(DigestEntries, Digest, wheel_package.digest)
    wheel_file_entry = digest_entries[0]
    assert isinstance(wheel_file_entry, FileEntry)
    foo_file_entry = FileEntry(path=wheel_file_entry.path + ".foo", file_digest=wheel_file_entry.file_digest)
    fooified = await Get(Digest, CreateDigest([foo_file_entry]))

    # Ensure the new file is correctly logged during the build process
    artifact = BuiltPackageArtifact(relpath=foo_file_entry.path)

    # Ensure the fooified file is output to dist/ and 
    return BuiltPackage(
        digest=fooified,
        artifacts=(artifact,),
    )

def rules():
    return [*collect_rules(), UnionRule(PackageFieldSet, FooifyFieldSet)]
