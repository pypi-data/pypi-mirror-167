#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(join(dirname(__file__), *names), encoding=kwargs.get('encoding', 'utf8')) as fh:
        return fh.read()


setup(
    name='mmisdk',
    version='0.0.4',
    description='A Python library to create and submit EVM transactions to custodians connected with MetaMask Institutional.',
    long_description='{}\n{}'.format(
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.md')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst')),
    ),
    author='Xavier Brochard',
    author_email='xavier.brochard@consensys.net',
    url='https://gitlab.com/ConsenSys/codefi/products/mmi/mmi-sdk-py/-/issues',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3 :: Only',
        # 'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
        'Topic :: Office/Business :: Financial'
    ],
    project_urls={
        'Documentation': 'https://consensys.gitlab.io/codefi/products/mmi/mmi-sdk-py/sdk-python/',
        'Changelog': 'https://gitlab.com/ConsenSys/codefi/products/mmi/mmi-sdk-py/-/blob/main/CHANGELOG.rst',
        'Issue Tracker': 'https://gitlab.com/ConsenSys/codefi/products/mmi/mmi-sdk-py/-/issues',
    },
    keywords='python sdk custodian interact get create transaction',
    python_requires='>=3.6',
    install_requires=[
        'pydantic>=1.10.1',
        'requests>=2.28.1',
    ],
    extras_require={
        "dev": [
            "bump2version==1.0.1",
            "check-manifest==0.48",
            "pytest==7.1.3",
            "twine==4.0.1",
            "tox==3.26.0"
        ]
    },
    setup_requires=[
        'pytest-runner',
    ],
    entry_points={
        'console_scripts': [
            'mmisdk = mmisdk.cli:main',
        ]
    },
)
