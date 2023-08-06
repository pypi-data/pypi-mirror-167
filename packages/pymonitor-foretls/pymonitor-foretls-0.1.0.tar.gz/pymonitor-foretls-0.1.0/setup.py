from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='pymonitor-foretls',
    version='0.1.0',
    python_requires='>=3.7',
    description="pymonitoring like pytest just for monitoring",
    author="Noa gradovitch",
    author_email="noahgrad@gmail.com",
    url="https://github.com/noahgrad/pymonitor",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
    ],
    zip_safe=False
)
