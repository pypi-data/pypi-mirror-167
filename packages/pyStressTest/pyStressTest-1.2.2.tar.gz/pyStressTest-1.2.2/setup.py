from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='pyStressTest',
    version='1.2.2',
    description='Module for resource stress testing and automatic statistics generation',
    long_description=LONG_DESCRIPTION,
    license="MIT",
    author='Chekashov Matvey/Ryize',
    author_email='chekashovmatvey@gmail.com',
    url="https://github.com/Ryize/pyStressTest",
    packages=find_packages(),
    install_requires=['requests', 'matplotlib']
)
