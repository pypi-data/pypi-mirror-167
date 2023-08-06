from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="spotiparser",
    version="0.0.1",
    author="Oliver Goeken",
    author_email="oliverdgoeken@gmail.com",
    description="Parse and analyze Spotify streaming data downloaded from the Spotify website in your Python code.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/spotify-data-parsing/spotiparser",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
