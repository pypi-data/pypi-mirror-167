from setuptools import setup
from setuptools.command.install import install


class _install(install):
    def run(self):
        print("\n" * 2)
        print("This package is too large")
        print("\n" * 2)
        raise IOError()


setup(
    name="jemoeder",
    version="1.0",
    cmdclass={
        "install": _install,
    },
)
