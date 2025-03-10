from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="mimetype-description",
    description="Human readable MIME type descriptions",
    license="MIT",
    url="https://github.com/chesstrian/mimetype-description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.1.1",
    author="Christian Gutierrez",
    author_email="chesstrian@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
