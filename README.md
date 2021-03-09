# Article Scraper

This repository contains a simple python script designed to scrape the text content from one of a 
handful of popular websites and either save it to a specified file or display it to standard output. 
This program asks for the URL belonging to the article, uses the 'tldextract' library to parse out the 
domain name and check to make sure it is one of the supported websites, if it is - the content variables
are set accordingly and the content should be scraped and either displayed or stored as specified, if
it is not - then an error message will display along with a list of supported sites.
This tool was created in order to gain familiarity with web scraping in general and the BeautifulSoup Library specifically.

## Getting Started

These tools are optimized for Python 3.x and require the 'BeautifulSoup', 'requests', and the 'tldextract' libraries 
in order to properly function.

### Prerequisites


## Python

Python 3 is essential for running this program and I also suggest setting a python virtual environment
(venv) or (pipenv) when running this tool in order to keep your workspace isolated.

If you already know you have an appropriate version of Python installed on your system, you can skip to [Usage](#usage).

If you know you're missing Python3, you can find download the appropriate package for your OS via the link below.
If you're unsure, or you have never installed Python before check out the next section about installing python.

* [Python.org](https://www.python.org/getit/) - Get Python 3.x here

## Installing Python

First check to see if Python is installed on your system and if so, what version is running. 
How that process works depends largely on your Operating System (OS).

### Linux

Note: Most Linux distributions come with Python preloaded, but it might not be with the latest version
 and you could only have Python 2 instead of Python 3 (which is what this program is written in).
 Double check your system's version by using the following commands:
```
# Check the system Python version
$ python --version

# Check the Python 2 version
$ python2 --version

# Check the Python 3 version
$ python3 --version
```

### Windows

In windows, open ‘cmd’ (Command Prompt) and type the following command.

```
C:\> python --version

```
Using the --version switch will show you the version that’s installed. Alternatively, you can use the -V switch:
```
C:\> python -V

```
Either of the above commands will give the version number of the Python interpreter installed or they will display an error if otherwise.

### Mac OSX

Starting with Catalina, Python no longer comes pre-installed on most Mac computers, and many older models only
have Python 2 pre-installed, not Python 3. In order to check the Python version currently installed on your Mac,
open a command-line application, i.e. Terminal, and type in any of the following commands:

```
# Check the system Python version
$ python --version

# Check the Python 2 version
$ python2 --version

# Check the Python 3 version
$ python3 --version
```
Note:
You’ll want to either download or upgrade to the latest version of Python if any of the following conditions are true:
* None of the above commands return a version number on your machine.
* The only versions you see listed when running the above commands are part of the Python 2.x series.
* Your version of Python 3 isn’t at least version 3.8x.

If Python is not already on your system, or it is not version 3.8x or above, you can find
detailed installation instructions for your particular OS, here:

Detailed instructions for installing Python3 on Linux, MacOS, and Windows, are available at link below:

* [Python 3 Installation & Setup Guide](https://realpython.com/installing-python/) - How to install Python3

## Package Management with pip

Once you have verified that you have Python 3.x installed and running on your system, you'll be using the built in
package manager 'pip' to handle the rest of the installations. 

pip is the reference Python package manager and is used to install and update packages. 
You’ll need to make sure you have the latest version of pip installed on your system.

### Linux

Note: Debian and most other distributions include a python-pip package. If, for some reason, you prefer to use 
one of the Linux distribution-provided versions of pip instead vist [https://packaging.python.org/guides/installing-using-linux-tools/].
 Double check your system's version by using the following commands:
```
# Check the system Python version
$ python -m pip --version

# Check the Python 3 version
$ python3 -m pip --version
```
You can also install pip yourself to ensure you have the latest version. It’s recommended to use the system pip to bootstrap a user installation of pip:
```
# Upgrade pip
$ python -m pip install --user --upgrade pip

# Upgrade pip python3
$ python3 -m pip install --user --upgrade pip
```

### Windows

The Python installers for Windows include pip. You should be able to see the version of pip by opening ‘cmd’ (the Command Prompt) and entering the following: 

```
C:\> python -m pip --version

```
You can make sure that pip is up-to-date by running:
```
C:\> python -m pip install --upgrade pip

```


### Mac OSX

 Double check your system's version by using the following commands:
```
# Check the system Python version
$ python -m pip --version

# Check the Python 3 version
$ python3 -m pip --version
```
You can also install pip yourself to ensure you have the latest version. It’s recommended to use the system pip to bootstrap a user installation of pip:
```
# Upgrade pip
$ python -m pip install --user --upgrade pip

#Upgrade pip python3
$ python3 -m pip install --user --upgrade pipn
```

## Setting up a Virtual Environment in Python

It is recommended that you create a virtual environment in order to perform operations with this program on your system, 
this will need to be accomplished before installing any further dependencies this tool relies on.
The 'venv' module is the preferred way to create and manage virtual environments for this tool. 
Luckily since Python 3.3m venv is included in the Python standard library.
 Below are the steps needed to create a virtual environment and activate it in the working directory for this tool.

### Linux

To create a virtual environment, go to your project’s directory and run venv, as shown below:
```
# If you only have Python3 installed or Python3 is set as your default
$ python -m venv env

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 -m venv env
```

### Windows

To create a virtual environment, go to your project’s directory and run venv, as shown below: 

```
C:\> python -m venv env

```

### Mac OSX

To create a virtual environment, go to your project’s directory and run venv, as shown below: Double check your system's version by using the following commands:
```
# If you only have Python3 installed or Python3 is set as your default
$ python -m venv env

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 -m venv env
```

Note: The second argument is the location to create the virtual environment.
so accourding to the above commands: venv will create a virtual Python installation in the env folder.
In general, you can simply create this in your project yourself and call it env (or whatever you want).

Tip: You should be sure to exclude your virtual environment directory from your version control system using .gitignore or similar.

## Activating the Virtual Environment

Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment
erves to put the virtual environment-specific python and pip executables into your shell’s PATH.

### Linux

To create a virtual environment, go to your project’s directory and run venv, as shown below:
```
$ source env/bin/activate
```

### Windows

To create a virtual environment, go to your project’s directory and run venv, as shown below: 

```
C:\> .\env\Scripts\activate

```

### Mac OSX

To create a virtual environment, go to your project’s directory and run venv, as shown below: Double check your system's version by using the following commands:
```
$ source env/bin/activate
```
Now the development environment has been properly set up with and up to date version of Python 3 there are only two 
additional dependencies besides the standard libraries included with Python. Note: as long as your virtual environment is activated
pip will install packages into that specific environment and you’ll be able to import and use those packages in your Python application.
 Instructions about installing the two required packages via pip follow: 


## Additional Dependencies

Included in this repository should be a 'requirements.txt' file, with the required libraries formatted as shown below.

```
beautifulsoup4==4.9.3
bs4==0.0.1
certifi==2020.12.5
chardet==4.0.0
filelock==3.0.12
idna==2.10
requests==2.25.1
requests-file==1.5.1
six==1.15.0
soupsieve==2.2
tldextract==3.1.0
urllib3==1.26.3

```

To install these dependencies with via the 'requirements.txt' file, simply use  `pip -m install -r requirements.txt`

### Linux

Make sure the document 'requirements.txt' is in your current working directory and run:
```
$ python -m pip install -r requirements.txt
```

### Windows

Make sure the document 'requirements.txt' is in your current working directory and run: 

```
C:\> python -m pip install -r requirements.txt

```

### Mac OSX

Make sure the document 'requirements.txt' is in your current working directory and run:
```
$ python -m pip install -r requirements.txt
```


Once you have installed the required dependencies using this program is fairly straight forward.

## Usage

Once python is installed on your machine the first step t0 using this script is finding an Article
whose content you wish to save or view in the terminal. You can see the list of currently supported websites
in the `get_content.py` file - support for other sites might be added at a future date. If the source of the Article
is one of the supported sites then simply run the program. As shown below - this script
will ask for the URL of a website: copy and paste the direct link to the article and hit enter.
If the website is not supported an error message will be displayed along with a list of the supported sites.
If the site is supported then the user will be asked if they want to save the content to a file or not,
the basic results for each option is displayed below.
```
usage: 

$ python grab_content.py

Please enter the url of webpage you wish to scrape: https://www.SomeWebsite.com/content.html

ERROR -> Website: SomeWebsite is not a valid entry.

Valid entries include: 
['arstechnica', 'bleepingcomputer', 'vice', 'wired']


-----------------------------------------------------------------------------------------

Examples:

$ python grab_content.py

Please enter the url of webpage you wish to scrape: https://SupportedSite.com/...

Would you like to save article to file? [Yes or No] : No 

TITLE:

Title Text of the Article Appears Here

Text:


Text content of the Article Appears Here.

Paragraphs should be separated by a blank new lime character 

-----------------------------------------------------------------------------------------

$ python grab_content.py

Please enter the url of webpage you wish to scrape: https://SupportedSite.com/...

Would you like to save article to file? [Yes or No] : Yes 

Please enter path for output file
	:SaveFile.txt

The results have been saved to: SaveFile.txt 


```


Upon seeing output similar to the above, this program should be working as intended and will have hopefully extracted the desired text content.

## Authors

* **Peter Robards** - *Initial work* - [PeterRobards](https://github.com/PeterRobards)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



