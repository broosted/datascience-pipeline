from setuptools import find_packages, setup

setup(
    name="datascience_project",
    version="0.0.1",
    author="broosted",
    author_email="broosted@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"}
)
