import setuptools
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + "/README.md") as file:
    long_description = file.read()

setuptools.setup(
    name="VehicleRecognition",
    version="0.5.1.1",
    author="Onyonka Clifford (vmmr, vehicle colour classification), Rex Mudanya (ANPR, OCR), Jecinta Mulongo (ANPR, OCR)",
    author_email="",
    url="http://192.168.0.73/data_analytics/vehicle-recognition",
    description="Viscan vehicle recognition packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
)
