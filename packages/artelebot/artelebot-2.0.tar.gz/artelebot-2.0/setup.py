import os , codecs

from setuptools import setup, find_packages

pkg = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(pkg, "README.md"), encoding="utf-8") as fh:
	
    long_description = "\n" + fh.read()


setup(

    name="artelebot",
    
    version="2.0",
    
    author="gay",
    
    author_email="",
    
    description = ("Arabic TeleBot"),
    
    long_description_content_type="text/markdown",
    
    url="",
    
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    
    long_description=long_description,
    
    packages=find_packages(),
    
    install_requires=['requests'],
    
    keywords=['telebot','artelebot'],
    
    classifiers=[
    
        "Development Status :: 1 - Planning",
        
        "Intended Audience :: Developers",
        
        "Programming Language :: Python :: 3",
        
        "Operating System :: Unix",
        
        "Operating System :: MacOS :: MacOS X",
        
        "Operating System :: Microsoft :: Windows",
    ]
)
