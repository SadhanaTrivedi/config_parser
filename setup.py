import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='config_parser',
     version='0.1',
     author="Sadhana Trivedi",
     author_email="xyz@example.com",
     description="Parse the file and write in file",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(exclude=['tests']),
     python_requires=">=3.7",
     install_requires=[
       'pytest', 'pytest-cov', 'python-dotenv', 'PyYAML'
     ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )