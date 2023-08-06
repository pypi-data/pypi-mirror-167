import setuptools

# Get README
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="yark",
    version="0.1.3",
    description="YouTube archiving made simple.",
    author="Owen Griffiths",
    author_email="root@ogriffiths.com",
    license="MIT",
    classifiers=[
        "Topic :: System :: Archiving",
        "Topic :: System :: Archiving :: Backup",
        "Topic :: Multimedia :: Video"
    ],
    url="https://github.com/owez/yark",
    include_package_data=True,
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "yark = yark:main",
        ]
    },
    long_description=long_description,
    long_description_content_type="text/markdown"
)