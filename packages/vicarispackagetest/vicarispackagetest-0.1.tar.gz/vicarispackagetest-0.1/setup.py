from setuptools import setup, find_packages

VERSION = '0.1'
DESCRIPTION = 'First testing package'
LONG_DESCRIPTION = 'First package, long description, ohoho very long'

setup(
    name='vicarispackagetest',
    version=VERSION,
    author='Vicaris',
    author_email="vicarisfsc@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'testing'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ]
)