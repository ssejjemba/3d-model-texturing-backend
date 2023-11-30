from setuptools import setup

setup(
    name="common",
    version="0.1.0",
    description="Common libraries for 3D Model Texturing Backend",
    author="Daniel Ssejjemba",
    packages=[
        "libs",
        "libs/config",
        "libs/encryption",
        "libs/error_handling",
        "libs/helpers"
    ],
    install_requires=[
        # List your dependencies here
        # e.g., "requests", "numpy"
    ],
    tests_require=[
        "pytest",
    ],
)
