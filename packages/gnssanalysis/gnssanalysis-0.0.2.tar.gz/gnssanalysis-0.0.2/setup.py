import setuptools

setuptools.setup(
    include_package_data=True,
    name="gnssanalysis",
    version="0.0.2",
    description="basic pyhton module for gnss analysis",
    author="Geoscience Australia",
    author_email="GNSSAnalysis@ga.gov.au",
    packages=setuptools.find_packages(),
    install_requires=["pandas", "boto3", "click", "numpy", "scipy", "matplotlib", "plotext", "tqdm", "unlzw",]
)
