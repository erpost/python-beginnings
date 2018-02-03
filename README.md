#Install Python, Pip and Virtualenv

# Python 3
sudo yum -y install gcc
sudo yum -y install epel-release
sudo yum -y install python34
sudo yum -y install python34-devel
sudo yum -y install python34-setuptools
sudo python3 /usr/lib/python3.4/site-packages/easy_install.py pip
sudo -H pip3 install --upgrade pip


# Python 2
sudo yum -y install python-pip
sudo -H pip install --upgrade pip

# Virtualenv
sudo pip3 install virtualenv
virtualenv venv --python=python3.6 
source venv/bin/activate
deactivate