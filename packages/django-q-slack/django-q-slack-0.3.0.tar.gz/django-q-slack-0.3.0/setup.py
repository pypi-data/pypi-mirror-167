import os
from setuptools import setup


with open("README.md", "r") as fh:
    README = fh.read()


setup(
    name='django-q-slack',
    version='0.3.0',
    author='Goran Vrbaški',
    author_email='vrbaski.goran@gmail.com',
    keywords='django distributed task queue worker scheduler cron redis disque ironmq sqs orm mongodb multiprocessing slack',
    packages=['django_q_slack'],
    install_requires=['requests>=2.0.0'],
    url='https://django-q.readthedocs.org',
    license='MIT',
    description='A Slack support plugin for Django Q',
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
