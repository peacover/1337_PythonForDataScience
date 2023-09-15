import setuptools
  
with open("README.md", "r") as fh:
    description = fh.read()
  
setuptools.setup(
    name="ft_package",
    version="0.0.1",
    author="Peacover",
    author_email="yer_raki@student.1337.ma",
    # packages=["ft_package"],
    description="A sample test package",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/peacover/1337_PythonForDataScience/tree/main/Python-Starting/ex09/",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[],
)