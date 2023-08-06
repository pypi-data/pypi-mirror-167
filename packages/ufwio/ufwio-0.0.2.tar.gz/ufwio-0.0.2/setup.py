import setuptools
with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="ufwio",
  version="0.0.2",
  author="Wangyang.zuo",
  author_email="wangyang.zuo@sophon.com",
  description="A package for LMDB database operations",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/pypa/sampleproject",
  packages=setuptools.find_packages(),
  install_requires=[
      "numpy",
      "lmdb",
      "scipy",
      "scikit-image",
      "google",
      "protobuf==3.19.0",
  ],
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)