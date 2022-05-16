from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="AdsQueryPkg",
    version="0.0.1",
    description="Search for metrics to analyse the dynamics of the interest in a specific topic related to astronomy and astrophysics.",
    author="Parker Levesque",
    author_email="parker.levesque@mail.utoronto.ca",
    packages=find_packages(),
)
