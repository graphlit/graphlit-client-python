from setuptools import setup, find_packages
import os

# Read the content of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version = os.getenv('PACKAGE_VERSION', '1.0.0')

setup(
    name='graphlit-client',
    version=version,
    packages=find_packages(),
    install_requires=[
        'httpx',
        'pydantic>=2.0.0,<3.0.0',
        'PyJWT',
        'websockets'
    ],
    python_requires='>=3.6',
    author='Unstruk Data Inc.',
    author_email='questions@graphlit.com',
    description='Graphlit API Python Client',
    url='https://github.com/graphlit/graphlit-client-python',
    long_description=long_description,
    long_description_content_type="text/markdown",
)
