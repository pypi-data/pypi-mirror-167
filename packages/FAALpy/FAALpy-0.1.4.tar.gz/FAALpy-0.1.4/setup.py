from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name = "FAALpy",
      version = "0.1.4",
      description="A python version of the .jar library FAAL",
      url="https://github.com/MKilani/FAALpy",
      author="Marwan Kilani",
      author_email="kilani.edu@gmail.com",
      license='MIT',
      include_package_data=True,
      packages=find_packages(),
      package_data={'FAALpy': ['config/*.txt', 'config/saliences/*.txt']},
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      install_requires=[
      "numexpr"
      ],
      python_requires='>=3.0')


