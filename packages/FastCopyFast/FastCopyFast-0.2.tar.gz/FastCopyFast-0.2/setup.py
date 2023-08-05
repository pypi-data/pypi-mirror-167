from setuptools import setup, find_packages
import codecs
import os

#change to dict
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(r"C:\Users\Gamer\anaconda3\envs\dfdir\_tmp_PyGitUpload_000003\README.md", encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.2'
DESCRIPTION = "3 functions to copy faster"

# Setting up
setup(
    name="FastCopyFast",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/FastCopyFast',
    author="Johannes Fischer",
    author_email="<aulasparticularesdealemaosp@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    #packages=[],
    keywords=['copy', 'file copy', 'copy faster'],
    classifiers=['Topic :: System', 'Topic :: System :: Archiving', 'Topic :: System :: Archiving :: Backup', 'Topic :: System :: Archiving :: Compression', 'Topic :: System :: Archiving :: Mirroring', 'Topic :: System :: Archiving :: Packaging', 'Topic :: System :: Filesystems'],
    install_requires=[],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*