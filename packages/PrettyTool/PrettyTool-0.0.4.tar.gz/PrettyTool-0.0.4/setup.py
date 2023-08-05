from setuptools import setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="PrettyTool",
    version="0.0.4",
    description="Create gorgeous command line interfaces with this all-in-one module!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules="PrettyTool",
    package_dir={"": "PrettyTool"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "yaspin",
        "termcolor",
        "pyfiglet",
        "tabulate"
    ]
)
