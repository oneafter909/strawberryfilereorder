#!/usr/bin/env python

from setuptools import setup

long_description = """
Keep reordered your PC.
"""

setup(
    name='strawberry',
    version='2.1',
    description='Strawberry',
    long_description=long_description.strip(),
    author='Vincenzo Talarico',
    author_email='vincenzo.donato2002@gmail.com',
    url='https://github.com/oneafter909/strawberryfilereorder',
    keywords='reorder',
    license='GPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=['strawberry'],
    python_requires='>=3.5',
    install_requires=[
        "m3u8>=0.3.12,<0.4",
        "requests>=2.13,<3.0",
    ],
    entry_points={
        'console_scripts': [
            'strawberry=strawberry.swb:main',
        ],
    }
)

