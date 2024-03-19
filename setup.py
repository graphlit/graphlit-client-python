from setuptools import setup, find_packages

setup(
    name='graphlit_client',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PyJWT',
    ],
    author='Graphlit',
    author_email='questions@graphlit.com',
    description='A package for creating tokens for Graphlit services',
    url='https://github.com/graphlit/python-graphlit-client',
)
