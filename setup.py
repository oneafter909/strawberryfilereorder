#!/usr/bin/env python3

from setuptools import setup

long_description = """
Manage your files. Better.
"""

setup(
    name='strawberry',
    version='4.0.0',
    description='Strawberry',
    long_description=long_description.strip(),
    author='Vincenzo Talarico',
    author_email='vincenzo.donato2002@gmail.com',
    url='https://github.com/oneafter909/strawberryfilereorder',
    keywords='reorder',
    license='GPLv3',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=['strawberry'],
    python_requires='>=3.5',
    scripts=[
        'strawberry/swb.py',
        'strawberry/creationdateutils.py',
        'strawberry/face_detection.py',
        'strawberry/face_recognition.py',
        'strawberry/face_recognition_core.py',
        'strawberry/faceRecognizer.py',
        'strawberry/GUI.py',
        'strawberry/identifier.py',
        'strawberry/__main__.py',
        'strawberry/reorderutility.py',
        ],
    entry_points={
        'console_scripts': [
            'strawberry=swb:begin',
            ],
        }
)
