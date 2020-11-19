#!/bin/python3
import os

necessary_list=[
    'vim',
    'proxychains4'
]

for software in necessary_list:
    os.system('sudo apt-get install '+software)