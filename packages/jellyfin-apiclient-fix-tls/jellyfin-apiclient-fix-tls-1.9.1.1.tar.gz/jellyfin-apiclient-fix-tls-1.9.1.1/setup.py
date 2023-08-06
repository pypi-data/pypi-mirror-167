from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='jellyfin-apiclient-fix-tls',
    version='1.9.1.1',
    author="Cyr-ius",
    author_email="cyr-ius@ipocus.net",
    description="Python API client for Jellyfin",
    license='GPLv3',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cyr-ius/jellyfin-apiclient-fix-tls",
    packages=['jellyfin_apiclient_python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['requests', 'urllib3', 'websocket_client', 'certifi']
)
