from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='canopto',
    version='1.0.0',
    author='Atticus T',
    author_email='theresurgence2@proton.me',
    url="https://github.com/theresurgence/canopto",
    description="canopto is a tool to sync course files and videos from the Canvas LMS hosted by the National University of Singapore(NUS).",
    license='GPLv3',
    packages=find_packages(),
    entry_points={
            'console_scripts': [
                'canopto=canopto.__main__:cli'
            ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    keywords='canopoto canvas panopto nus',
    install_requires=requirements,
    zip_safe=False
)
