# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

# This call to setup() does all the work
setup(
  name="code_mixed_text_toolkit",
  version="0.3.5",
  description="A library for processing Code Mixed Text. Still in development!",
  long_description_content_type="text/markdown",
  long_description=long_description,
  url="https://code-mixed-text-toolkit.readthedocs.io/",
  author="Reuben Devanesan",
  author_email="reubendevanesan@gmail.com",
  license="MIT",
  classifiers=[
      "Intended Audience :: Developers",
      "License :: OSI Approved :: MIT License",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.9",
      "Programming Language :: Python :: 3.10",
      "Operating System :: OS Independent"
  ],
  # packages=["code_mixed_text_toolkit", "code_mixed_text_toolkit/data", "code_mixed_text_toolkit/preprocessing"],
  packages=find_packages(),
  include_package_data=True,
  data_files=[('code_mixed_text_toolkit/data', ['code_mixed_text_toolkit/data/data.json'])],
  install_requires=["numpy", "pandas", "requests", "tqdm"]
)