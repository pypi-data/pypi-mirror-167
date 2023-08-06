from distutils.core import setup

with open('README') as file:
    readme = file.read()

setup(
    name='tiger_wargame',
    version='2.0.1',
    packages=['wargame'],
    url='https://pypi.org',
    license='LICENSE.txt',
    description='tiger\'s wargame',
    long_description=readme,
    author='david',
    author_email='xxxx@mail.com'
)
