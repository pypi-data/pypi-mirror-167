import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyC4Room",  # Replace with your own username
    version="1.0.0",
    author="nalin29",
    author_email="github@nalinmahajan.com",
    description="Forked Python 3 asyncio package for interacting with Control4 systems and includes room support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nalin29/pyControl4.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        'aiohttp',
        'xmltodict',
        'python-socketio>=4,<5',
        'websocket-client',
    ],
)
