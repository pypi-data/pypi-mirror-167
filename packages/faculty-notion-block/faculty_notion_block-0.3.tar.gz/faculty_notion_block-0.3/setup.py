from setuptools import setup, find_packages


setup(
    name="faculty_notion_block",
    version="0.3",
    license="MIT",
    author="Kelvin Yeung",
    author_email="yeung_kelvin@hotmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    keywords="notion block project",
    install_requires=[
        "pydantic",
        "requests",
    ],
)
