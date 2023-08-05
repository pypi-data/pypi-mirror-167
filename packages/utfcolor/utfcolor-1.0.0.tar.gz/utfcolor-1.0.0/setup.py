import setuptools

with open("requirements.txt") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name="utfcolor",
    version="1.0.0",
    license="MIT",
    author="5omega",
    author_email="5omega@posteo.de",
    description="Convert text to images with Python",
    long_description_content_type="text/plain",
    long_description="Visit https://github.com/5omega/utfcolor for more information.",
    url="https://github.com/5omega/utfcolor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=requirements,
    python_requires=">=3.6.9",
)
