import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "lexas",
    version = "1.0.3",
    author = "CShark",
    author_email = "datlaptrinh@gmail.com",
    description = "a python3 package for encrypt and decrypt content with password",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://cshark.io/lexas",
    project_urls = {
        "Bug Tracker": "https://cshark.io/lexas/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ["pycryptodome"],
    package_dir = {"": ".\\"},
    python_requires = ">=3.6"
)