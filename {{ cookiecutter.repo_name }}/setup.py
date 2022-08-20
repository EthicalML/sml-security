from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="{{ cookiecutter.repo_name }}",
    version="0.1.0",
    url="https://github.com/{{ cookiecutter.repo_user }}/{{ cookiecutter.repo_name }}.git",
    author="{{ cookiecutter.repo_user }}",
    author_email="",
    description="{{ cookiecutter.description }}",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "mlserver==1.1.0",
    ],
    long_description=Path("README.md").read_text(),
    license="{{ cookiecutter.open_source_license }}",
)

