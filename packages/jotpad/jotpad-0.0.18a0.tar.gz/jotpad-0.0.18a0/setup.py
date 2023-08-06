import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jotpad",
    version="0.0.18-alpha",
    install_requires=[
        "appdirs>=1.4.0",
        "typer[all]>=0.6.0",
    ],
    author="Scott Russell",
    author_email="me@scottrussell.net",
    description="Jotpad is a cli tool for managing notes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scrussell24/jotpad",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points = '''
        [console_scripts]
        jotpad=jotpad:app
    '''
)
