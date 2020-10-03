import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "../README.md").read_text()

# This call to setup() does all the work
setup(
    name="abuu",
    version="1.0.0",
    description="ABUU - Another Bunch of Uselessfull Utils",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/yashshah1/abuu",
    author="Yash Shah",
    author_email="yashshah1234@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["utils", "utils/pandas"],
    include_package_data=True,
    install_requires=["pandas"],
    entry_points={
        "console_scripts": [
            "abuu=utils.__main__:main",
        ]
    },
)