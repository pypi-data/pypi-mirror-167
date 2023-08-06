from setuptools import setup

with open("README.rst", encoding='utf-8') as readmeFile:

    setup(
        name="path_parent",
        version="1.0.3",
        keywords=("path", "parent"),
        description="Append '..' to path setting.",
        long_description=readmeFile.read(),
        license="MIT Licence",
        url="https://github.com/adf0001/path_parent",
        author="fwg",
        author_email="adf0001@163.com",
        packages=["path_parent"],
        include_package_data=True,
        platforms="any",
    )
