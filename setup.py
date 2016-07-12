import os
from setuptools import find_packages, setup


# directory = os.path.abspath(os.path.dirname(__file__))
"""
with open(os.path.join(directory, 'README.rst')) as f:
    long_description = f.read()
"""

setup(
    name="chatimus_speech",
    version='0.0.2',
    description='Python personal assistant',
    # long_description=long_description,
    url='https://github.com/benhoff/chatimus_speech',
    license='GPL3',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent'],
    author='Ben Hoff',
    author_email='beohoff@gmail.com',
    entry_points={'chatimusmaximus.gui': ['speech_button=speech_button.__init__:add_speech_button',]},
    packages= find_packages(), # exclude=['docs', 'tests']
)
