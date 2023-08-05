import setuptools

with open("README.md", 'r') as fh:
    long_desc = fh.read()

setuptools.setup(
    name="metku",
    version="0.1.5",
    url="https://github.com/kuisidu/metku",
    author="Kristo Mela, Jaakko Huusko, Viktor Haimi",
    description="Module for structural analysis and optimization",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=['numpy', 'matplotlib', 'scipy',
                      'deap', 'ortools', 'treelib']
)
