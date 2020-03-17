import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-sql-middleware",  # Replace with your own username
    version="0.0.5",
    author="Fata Nugraha",
    author_email="fatanugraha@outlook.com",
    description="Simple SQL Middleware for Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fatanugraha/django-sql-middleware",
    install_requires=['django',],
    packages=setuptools.find_packages(exclude=["tests*"]),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
