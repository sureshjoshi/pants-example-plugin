from pants.engine.target import COMMON_TARGET_FIELDS, Dependencies, Target


class FooifyDependenciesField(Dependencies):
    pass


class FooifyTarget(Target):
    alias = "fooify_distribution"
    core_fields = (
        *COMMON_TARGET_FIELDS,
        FooifyDependenciesField,
    )
    help = "The `fooify` target will take in a wheel dependency and add a .foo extension to the end."
