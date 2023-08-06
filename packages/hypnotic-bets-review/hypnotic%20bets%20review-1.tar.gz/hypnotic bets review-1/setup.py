import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt','r') as fr:
    requires = fr.read().split('\n')

setuptools.setup(
    # pip3 hypnotic bets review
    name="hypnotic bets review", 
    version="1",
    author="hypnotic bets review",
    author_email="review@hypnoticbets.com",
    description="hypnotic bets review",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://b0ccc3lp4rrx6n37vqoy351o4l.hop.clickbank.net/?tid=py",
    project_urls={
        "Bug Tracker": "https://github.com/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=requires,
)
