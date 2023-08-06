import re
import setuptools


with open("zombies/__init__.py", "r") as file:
    text = file.read()

    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', text, re.MULTILINE
    ).group(1)
    description = re.search(r'"""([\w\s.]+)"""', text).group(1)


with open("README.rst", "r") as file:
    readme = file.read()


packages = ["zombies"]


extra_requires = {"dev": ["black"]}


setuptools.setup(
    name="zombies",
    author="The Master",
    license="MIT",
    description=description,
    long_description=readme,
    long_description_content_type="text/x-rst",
    version=version,
    packages=packages,
    include_package_data=True,
    python_requires=">=3.6.0",
    extra_requires=extra_requires,
    entry_points={
        "console_scripts": [
            "zombies = zombies.cli:main",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Interpreters",
        "Typing :: Typed",
    ],
)
