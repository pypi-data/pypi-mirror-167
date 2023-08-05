from setuptools import setup, find_packages

requirements = [
    'beautifulsoup4 == 4.11.1',
    'certifi == 2021.10.8',
    'charset-normalizer == 2.0.12',
    'feedparser == 6.0.8',
    'idna == 3.3',
    'requests == 2.27.1',
    'sgmllib3k == 1.0.0',
    'soupsieve == 2.3.2.post1',
    'urllib3 == 1.26.9'
]

setup(
    name='cnareader',
    version='1.0.0',
    author='Atticus T',
    author_email='theresurgence2@proton.me',
    url="https://github.com/theresurgence/cnareader",
    description="cnareader is a distraction-free terminal user interface client for reading the latest news from Channel News Asia.",
    license='GPLv3',
    packages=find_packages(),
    entry_points={
            'console_scripts': [
                'cnareader=src.__main__:cli'
            ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    keywords='CNA tui python',
    install_requires=requirements,
    zip_safe=False
)
