from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='warplol',
    version='1.3.0',
    description='Short URLs using the warp.lol APIs.',
    py_modules=["warplol"],
    package_dir={'': 'src'},
    install_requires=[            # I get to this in a second
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Filippo Romani",
    author_email="mail@filipporomani.it",
    url="https://warp.lol/"
)