import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="devto-articles-backup", # Replace with your own username
    version="0.3.0",
    author="Alessio Michelini",
    author_email="alessio@michelini.dev",
    description="Small package to fetch articles from Dev.to",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/darkmavis1980/devto-articles-backup",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    scripts=['bin/devto-backup'],
)