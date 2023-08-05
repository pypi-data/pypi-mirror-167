from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name="hexp",
    version='0.1.1',
    py_modules=['hexp'],
    description="Dump contents of input in hexadecimal.",
    author="Mano",
    author_email="shapely_indexes0d@icloud.com",
    install_requires=[
        'Click',
    ],
    scripts=['bin/hexp'],
    url="https://github.com/manorajesh/hexp",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    keywords="hexdump hex hexadecimal",
    long_description_content_type="text/markdown",
    long_description=readme(),
)