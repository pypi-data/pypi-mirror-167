from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.2'
DESCRIPTION = "Create a .bat file on your desktop to run your script"

# Setting up
setup(
    name="CreateBat",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/CreateBat',
    author="hansalemao",
    author_email="<aulasparticularesdealemaosp@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    keywords=['batch', 'bat', 'windows', 'python bat'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        #"Operating System :: Unix",
        #"Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    install_requires=[
         
      ]
)

#python setup.py sdist bdist_wheel
#twine upload dist/*