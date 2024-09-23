from setuptools import setup, find_packages

setup(
    name='operalib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'behave',
    ],
    description='A library of reusable Behave steps for Opera application.',
    author='Ivan',
    author_email='jmatamoros@infoya.ca',
    url="https://github.com/yourusername/behave-steps-library.git",
)