from setuptools import setup

setup(
    name = "Organ Donation",
    version = "1.0",
    description = "organ donation app",
    packages = ["organdonationwebapp"],
    package_dir={'models': 'organdonationwebapp/models','controller':'organdonationwebapp/controller'}
)
