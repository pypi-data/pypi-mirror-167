import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mt5_order_handle",      # Replace with your own username
    version="1.0.1",
    author="Kritthanit_Malathong",
    author_email="kritthanit.m@gmail.com",
    description="a package that contain python function for handle mt5 order",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['MetaTrader5', 'pandas', 'datetime'],
    python_requires='>=3.9',
)
