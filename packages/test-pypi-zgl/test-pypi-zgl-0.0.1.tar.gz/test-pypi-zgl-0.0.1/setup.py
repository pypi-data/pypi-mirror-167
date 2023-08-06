from setuptools import (
    find_packages,
    setup,
)

setup(
    name='test-pypi-zgl',
    version='0.0.1',
    description='test-pypi',
    classifiers=[],
    keywords='test-pypi',
    author='zgl',
    author_email='',
    url='',
    license='MIT',
    packages=find_packages(exclude=[]),
    package_data={'': ['*.*']},
    include_package_data=True,
    install_requires=[],
    long_description='test-pypi'
)
