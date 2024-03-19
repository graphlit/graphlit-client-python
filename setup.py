from setuptools import setup, find_packages

# Read the content of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='graphlit_client',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'PyJWT',
    ],
    author='Graphlit',
    author_email='questions@graphlit.com',
    description='A package for creating tokens for Graphlit services',
    url='https://github.com/graphlit/graphlit-client-python',
    long_description=long_description,
    long_description_content_type="text/markdown",
)
