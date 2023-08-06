import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="share-project", 
    version="1.09.16.2022",
    author="Nii Golightly",
    author_email="nlli@pm.me",
    description="A sample template for testing python packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
)