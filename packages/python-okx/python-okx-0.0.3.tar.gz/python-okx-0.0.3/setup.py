import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-okx",
    version="0.0.3",
    author="okxv5api",
    author_email="api@okg.com",
    description="Python SDK for OKX OpenAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://okx.com/docs-v5/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "httpx",
        "h2"
    ]
)