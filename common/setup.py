from setuptools import setup

setup(
    name="common",
    version="0.1.0",
    description="Common libraries for 3D Model Texturing Backend",
    author="Daniel Ssejjemba",
    packages=[
        "common/libs",
        "common/libs/config",
        "common/libs/encryption",
        "common/libs/error_handling",
        "common/libs/helpers"
    ],
    install_requires=[
        # List your dependencies here
        # e.g., "requests", "numpy"
    ],
    tests_require=[
        "pytest",
    ],
)
