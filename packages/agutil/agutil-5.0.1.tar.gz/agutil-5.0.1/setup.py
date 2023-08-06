from setuptools import setup
try:
    from pip.req import parse_requirements
except ImportError:
    from pip._internal.req import parse_requirements

def extract_requirement(package):
    if hasattr(package, 'req'):
        return str(package.req)
    return str(package.requirement)

import sys
if sys.version_info == (3.3):
    import warnings
    warnings.warn(
        "Warning: Python 3.3 is no longer officially supported by agutil"
    )
elif sys.version_info<(3,4):
    print("This python version is not supported:")
    print(sys.version)
    print("agutil requires python 3.4 or greater")
    sys.exit(1)

with open('README.md') as r:
    long_desc = r.read()

from agutil import __version__ as version

setup(
    name="agutil",
    version=version,
    packages=[
        "agutil",
        "agutil.io",
        "agutil.io.src",
        "agutil.parallel",
        "agutil.parallel.src",
        "agutil.security",
        "agutil.security.src",
        "agutil.src",
    ],
    entry_points={
        "console_scripts":[
            "agutil-secure = agutil.security.console:main"
        ]
    },
    install_requires=[
        extract_requirement(package) for package in parse_requirements(
            'requirements.txt',
            session=''
        )
    ],
    tests_require=[
        extract_requirement(package) for package in parse_requirements(
            'tests/requirements.txt',
            session=''
        )
    ],
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Security :: Cryptography',
        'Topic :: Utilities',

        'License :: OSI Approved :: MIT License',

        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only"
    ],

    author = "Aaron Graubert",
    author_email = "captianjroot@live.com",
    description = "A collection of python utilities",
    long_description = long_desc,
    long_description_content_type = "text/markdown",
    license = "MIT",
    keywords = "range progress bar loading encryption decryption RSA AES io sockets utilities",
    url = "https://gitlab.graubert.com/agraubert/agutil",   #
)
