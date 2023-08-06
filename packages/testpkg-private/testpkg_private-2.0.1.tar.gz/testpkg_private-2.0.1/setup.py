from distutils.core import setup

with open('README') as file:
    readme = file.read()

setup(
    name='testpkg_private',
    version='2.0.1',
    packages=['wargame'],
    url='http://localhost:8081/simple',
    license='LICENSE.txt',
    description='test pkg private',
    long_description=readme,
    author='david',
    author_email='xxxx@mail.com'
)
