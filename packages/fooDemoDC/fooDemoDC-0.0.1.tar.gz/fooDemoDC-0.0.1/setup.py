from setuptools import setup

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="fooDemoDC",
    version="0.0.1",
    description="Guide",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/dance858/FooDemoDC",
    author="Daniel Cederberg",
    author_email="roberto.prevato@gmail.com",
    keywords="core utilities",
    license="MIT",
    packages=["my_foo"],
    install_requires=[],
    include_package_data=True,
)