python_sources(name="libhelloworld", sources=["**/*.py"])

python_distribution(
    name="helloworld-dist",
    dependencies=[":libhelloworld"],
    wheel=True,
    sdist=False,
    provides=python_artifact(
        name="helloworld-dist",
        version="0.0.1",
        description="A distribution for the hello world library.",
    ),
)

fooify_distribution(
    name="helloworld-foo",
    dependencies=[":helloworld-dist"],
)
