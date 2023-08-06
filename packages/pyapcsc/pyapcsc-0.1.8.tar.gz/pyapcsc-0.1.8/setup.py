"""Setup for pyoctoprintapi"""

# https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
# http://peterdowns.com/posts/first-time-with-pypi.html
# pip install -e .
# Upload to PyPI Live
# python setup.py sdist bdist_wheel
# twine upload dist/pyoctoprintapi-* --skip-existing

from setuptools import setup

setup(
    name="pyapcsc",
    packages=["pyapcsc"],
    version="0.1.8",
    description="An asynchronous Python library for communicating with the APC Smart Connect API",
    author="Ryan Fleming",
    author_email="rfleming71@users.noreply.github.com",
    license="MIT",
    url="https://github.com/rfleming71/pyapcsc",
    install_requires=["aiohttp"],
    keywords=["apc", "smartconnect", "homeassistant"],
    classifiers=["Natural Language :: English", "Programming Language :: Python :: 3"],
)
