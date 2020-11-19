#!/bin/python3
import os

email='alan@foralan.cn'
name='yangyixuan'

os.system('sudo apt-get install git')
os.system('git config --global user.email ' + email)
os.system('git config --global user.name ' + name)