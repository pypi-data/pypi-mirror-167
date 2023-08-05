import setuptools
  
with open("GameWidgets/README.md", "r") as fh:
    description = fh.read()
  
setuptools.setup(
    name="GameWidgets",
    version="0.0.4",
    author="Manomay tyagi",
    author_email="tyagimanomay57@gmail.com",
    packages=["GameWidgets"],
    description="Pygame becomes easier",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/gituser/test-tackage",
    license='MIT',
    python_requires='>=3.8',
    install_requires=['pygame']
)