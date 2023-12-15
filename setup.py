from setuptools import setup, find_packages

from ngram_graph import __version__

with open("Readme.md") as f:
    long_description = f.read()

setup(
    name="ngram_graph",
    version=__version__,
    author="infinityofspace",
    url="https://github.com/infinityofspace/ngram_graph",
    description="Create N-Gram graphs from text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "dgl>=1.1.3",
        "torch>=2.1.2"
    ]
)
