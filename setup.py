from setuptools import setup, find_packages

setup(
    name='easyscrapper',
    version='1.0.0',
    author='Krishna Tadi',
    author_email='er.krishnatadi@gmail.com',
    description='EasyScrapper is a simple and effective Python package for web scraping. It allows you to fetch and extract data from any website without the hassle of complex parsing logic. This package is designed for developers who need quick and reliable web scraping solutions.',
    packages=find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url='https://github.com/krishnatadi/easyscrapper',
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
    ],
    python_requires='>=3.6',
    keywords='web scraping, data extraction, html parser, scraping',
    project_urls={
    'Documentation': 'https://github.com/krishnatadi/easyscrapper#readme',
    'Source': 'https://github.com/krishnatadi/easyscrapper',
    'Issue Tracker': 'https://github.com/krishnatadi/easyscrapper/issues',
    },
    license='MIT'
)
