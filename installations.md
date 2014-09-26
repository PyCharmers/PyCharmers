Introduction to PyCharmers
============

Welcome to PyCharmers! PyCharmers is SLAC's premier Intro to Python course. We'll be building this course throughout the semester with your help!

##Getting setup to use Python
While we prefer you to have a Linux or Unix operating system on your computer, we'll still help if you want to use Windows for the first few lessons. After that, you will need Linux.

### Installing on Linux
Open a terminal and type

```
apt-get update
sudo apt-get install python3
```

### Installing on OS X
Get the latest version [here](https://www.python.org/downloads/). While Macs come with Python preinstalled, we're going to want to have the latest version of Python 3.


## Setting up a Virtual Machine with Ubuntu
While you have a lot of options for getting Linux on your computer, we recommend getting [VMWare Player](https://my.vmware.com/web/vmware/free#desktop_end_user_computing/vmware_player/6_0), and installing the latest version of [64-bit Ubuntu](http://www.ubuntu.com/download/desktop).


## Getting Started
Now that we've all got Python installed, let's try writing some code!

Go ahead and open up a terminal and type `python` then press enter. If you get a message like `'command not found'` try `python3` instead. If that still doesn't work you probably didn't install Python correctly.

If you did install it correctly, you should see something like this:

```
$ python
Python 3.4.1
[GCC 4.2.1]
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Those three arrows pointing to the right tell us we are in the Python interpreter, so any Python code we type here will be executed.

So let's get started.

## Adding Useful Programs to Ubuntu
* Update repositories and current packages:
```
sudo apt-get update &&
sudo apt-get upgrade
```
* Sublime Text 3
```
sudo add-apt-repository ppa:webupd8team/sublime-text-3 &&
sudo apt-get update &&
sudo apt-get install sublime-text-installer
```
* Google Chrome 
```
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - &&
sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' &&
sudo apt-get update &&
sudo apt-get install google-chrome-stable
```
* Python (add 3 at end for Python3.4) 
```
sudo apt-get install python
```
* Pip (add 3 at end for Pip3)
```
sudo apt-get install python-pip
``` 
* git
```
sudo apt-get install git
```

### Sublime Package Manager
Sublime has a lot of wonderful plugins that allow you to customize your environment to suit your needs and style. These plugins can be installed with a few keypresses with the Sublime package manager.
* Open Sublime and type 'ctrl+\`' and copy the following line into the console
```
import urllib.request,os,hashlib; h = '7183a2d3e96f11eeadd761d777e62404' + 'e330c659d4bb41d3bdf022e94cab3cd0'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```



