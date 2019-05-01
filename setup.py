from setuptools import setup


with open("README.md", "r") as stream:
    long_description = stream.read()

setup(name='minimaldb',
    version='1.0',
    description='Minimalistic document oriented database.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/ZAZPRO/minimaldb',
    author='Daniil Mira',
    author_email='daniilmira@gmail.com',
    packages=setuptools.find_packages(),
    classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
    ],
)
