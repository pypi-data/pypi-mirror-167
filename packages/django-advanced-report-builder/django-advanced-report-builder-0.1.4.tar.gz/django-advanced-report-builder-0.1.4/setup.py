import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-advanced-report-builder",
    version="0.1.4",
    author="Thomas Turner",
    description="Django app that allows you to build reports from modals",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/django-advance-utils/django-advanced-report-builder",
    include_package_data=True,
    packages=['advanced_report_builder'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
