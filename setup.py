from setuptools import setup, find_packages

setup(
    name="krex",
    version="0.0.1",  
    author="Kairos Research",
    author_email="labs@kairosresearch.io",
    description="A lightweight Python package providing minimal trading functions for selected exchanges, organized by exchange-specific modules.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kairos-research-ltd/krex.git", 
    packages=find_packages(exclude=["krex/test*", ".gitignore"]),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11.5",
    install_requires=open("requirements.txt").read().splitlines(),
    include_package_data=True, 
)
