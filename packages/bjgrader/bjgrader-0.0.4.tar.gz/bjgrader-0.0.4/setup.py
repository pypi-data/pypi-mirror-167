import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="bjgrader",
    version="0.0.4",
    author="Dooho Lee",
    author_email="dhdev5ba@gmail.com",
    url="https://github.com/BlueYellowGreen/bjgrader",
    description="Grade a solution using baekjoon online sample inputs and outputs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=['requests', 'beautifulsoup4'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=['bjgrader'],
)