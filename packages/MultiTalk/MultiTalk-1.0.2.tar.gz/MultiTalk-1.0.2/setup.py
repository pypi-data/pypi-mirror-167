from setuptools import setup, find_packages

setup(
    name="MultiTalk",
    version="1.0.2",
    author="sonyakun",
    packages=find_packages(),
    install_requires=["requests","asyncio"],
    include_package_data=True,
)