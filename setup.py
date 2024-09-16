from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dailytask/__init__.py
from dailytask import __version__ as version

setup(
	name="dailytask",
	version=version,
	description="Custom Development",
	author="Vivek",
	author_email="vivekchamp84@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
