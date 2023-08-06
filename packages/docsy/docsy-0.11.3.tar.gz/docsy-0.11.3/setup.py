import pathlib

from setuptools import find_packages, setup

this_directory = pathlib.Path(__file__).parent
with open(this_directory / "README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="docsy",
    install_requires=["markdown >= 0.0.1", "httpserver >= 0.0.1"],
    python_requires=">=3.3",
    version="0.11.3",
    description='Client for docsy',
    author="GinoZhang",
    author_email="gino0922@163.com",
    maintainer="Gino Zhang",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/ginoblog/docsy",
    entry_points={
        "console_scripts": [],
    },
    license="see LICENSE",
    keywords=["docsy","docs","render","html","markdown"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    extras_require={
        "dev": [
            "setuptools",
            "wheel",
            "twine",
        ]
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Education",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Games/Entertainment :: Simulation"
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
