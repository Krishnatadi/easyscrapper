from setuptools import setup, find_packages

setup(
    name='easyscrapper',
    version='1.0.2',
    author='Krishna Tadi',
    author_email='er.krishnatadi@gmail.com',
    description='easyscrapper is a fast, lightweight Python package and CLI tool that lets developers, data scientists, and AI engineers extract text, HTML, emails, links, canonical, meta and images from any public webpage - perfect for AI, RAG pipelines, SEO, content aggregation, and scalable data workflows with just one command or a few lines of code.',
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
    keywords='web scraping, data extraction, html parser, scraping, easyscrapper, RAG, AI, Text Chuncking',
    project_urls={
    'Documentation': 'https://github.com/krishnatadi/easyscrapper#readme',
    'Source': 'https://github.com/krishnatadi/easyscrapper',
    'Issue Tracker': 'https://github.com/krishnatadi/easyscrapper/issues',
    },
    entry_points={
    'console_scripts': [
        'easyscrapper = easyscrapper.cli:main'
    ],
},  

    license='MIT'
)
