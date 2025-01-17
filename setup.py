# @Author: archer
# @Date:   2019-07-23T10:25:25+01:00
# @Last modified by:   archer
# @Last modified time: 2019-07-23T10:25:41+01:00


import setuptools

setuptools.setup(
    name='SimpleDataTransport',
    version='1.5',
    author="Raymond Tunstill",
    author_email="ray.tunstill@live.co.uk",
    description="Simple python 2/3 library for transporting images/data to a remote machine, applying transformations "
                "and returning a response.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RaymondKirk/SimpleDataTransport",
    packages=["SimpleDataTransport"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=['Flask', 'numpy', 'requests', 'jsonpickle'],
)
