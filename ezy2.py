#!/usr/bin/env python
from __future__ import absolute_import
import sys;
import utils.helper as utils;
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

directories_in_curdir = filter(os.path.isdir, os.listdir(os.curdir))

# For pulling code 
for dir_name in directories_in_curdir:
    utils.cmd_exec('cd ' + dir_name + ' && git pull')
  
# For cloning code
with open('/Users/deepak/experiments/fabhotels/projects', 'rU') as f:
    for line_terminated in f:
        line = line_terminated.rstrip('\n')
        utils.cmd_exec('git clone https://deepakfab@bitbucket.org/fabhotelsvaibhav/' + line + '.git')
        # exit()
