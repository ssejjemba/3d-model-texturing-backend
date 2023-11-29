from setuptools import setup, find_packages

setup(
    name="common",
    version="0.1.0",
    description="Common libraries for 3D Model Texturing Backend",
    author="Daniel Ssejjemba",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        # e.g., "requests", "numpy"
    ],
    tests_require=[
        "pytest",
    ],
)
