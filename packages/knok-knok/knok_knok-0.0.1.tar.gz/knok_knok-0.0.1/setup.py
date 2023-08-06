from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = "knok_knok",
    version = '0.0.1',
    author = 'Ajay Sharma',
    author_email = 'ajaysh4rma132@gmail.com',
    description = 'For sending push notifications to android and ios devices',
    long_description_content_type='text/markdown',
    long_description = long_description,
    packages = find_packages(),
    install_requires = ['requests'],
    keywords = ['push', 'notifications', 'android', 'ios', 'fcm', 'gcm'],
    url = 'https://github.com/AjaySharma132/knok_knok',
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Communications",
        "Topic :: Software Development :: Libraries",
    ]
)