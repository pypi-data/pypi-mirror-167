from distutils.core import setup

with open('README') as file:
    readme = file.read()

setup(
    name='some_unique_name',
    version='2.0.0',
    packages=['wargame'],
    url='https://testpypi.python.org/pypi/some_unique_name/',
    license='LICENSE.txt',
    description='my first game',
    long_description=readme,
    author='david',
    author_email='xxxx@mail.com'
)
