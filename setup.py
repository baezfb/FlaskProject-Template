import pathlib

import setuptools

setuptools.setup(
    name="openwebpos",
    version="0.0.5",
    description="Web-based Point of Sale System",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/baezfb/OpenWebPOS",
    author="Javier Baez",
    author_email="baezdevs@gmail.com",
    license="MIT License",
    project_urls={
        "source": "https://github.com/baezfb/openwebpos",
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.11, <3.13",
    install_requires=[
        "flask>=3.0.0, <4.0.0",
        "flask-login>=0.6.3, <0.7.0",
        "flask-wtf>=1.2.1, <1.3.0",
        "flask-sqlalchemy>=3.1.1, <3.2.0",
        "python-dotenv>=1.0.0, <2.0.0",
        "pytz>=2021.3, <2022.0",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
)
