from setuptools import setup, find_packages

setup(
    name="franklin-fastapi-extension",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "mysql-connector-python"
    ],
    include_package_data=True,
    description="This is a FastAPI Extension to simplify the creation process of APIS",
    author="Franklin Neves Filho",
    url="https://github.com/franklinnevesfilho/SimpleAPI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: WTFPL License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.8"
)
