#!/bin/bash
# Use only if you need to perform changes on the user system such as installing software
sudo dpkg --configure -a
sudo apt-get install python3-lxml
sudo apt-get install requests
