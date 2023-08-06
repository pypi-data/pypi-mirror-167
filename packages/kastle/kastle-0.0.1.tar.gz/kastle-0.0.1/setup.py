import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kastle",
    version="0.0.1",
    author="Will Wang",
    author_email="No.1@pku.edu.cn",
    description="KASTLE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/I-E-E-E/KAML",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)