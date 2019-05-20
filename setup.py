import setuptools
import re
import os
import ast

# parse version from locust/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')
_init_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "nima_cast", "__init__.py")
with open(_init_file, 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setuptools.setup(
    name="nima_cast",
    version=version,
    url="https://github.com/nimamahmoudi/nima_cast",
    author="Nima Mahmoudi",
    author_email="nima_mahmoudi@live.com",
    description="This is a project that could connect to a minio server and sream the conents on a chromecast device.",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    install_requires=['minio'],
    dependency_links=['https://github.com/balloob/pychromecast'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
