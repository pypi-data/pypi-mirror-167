
import setuptools
from pyseat.version import __version__

# with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="pyseat",
    version=__version__,
    author="Lingxi Chen",
    author_email="chanlingxi@gmail.com",
    description="Structure Entropy hierArchy deTection (SEAT) for clustering, ordering, and embedding",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/deepomicslab/seat",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
