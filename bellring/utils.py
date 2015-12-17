#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Eduard Trott
# @Date:   2015-12-17 16:54:19
# @Email:  etrott@redhat.com
# @Last modified by:   etrott
# @Last Modified time: 2015-12-17 17:25:44

import logging
import subprocess
import sys
import os
import yaml


# Load logging before anything else
logging.basicConfig(format='>> %(message)s')
logr = logging.getLogger('ring')

''' Load the config file so modules can import and reuse '''
CONFIG_FILE = os.path.expanduser('~/.bellring')
if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE) as _:
        config = yaml.load(_)
else:
    config = {}
# destination: "Blue Jeans"

def run(cmd, shell=True):
    if not shell:
        cmd = cmd if isinstance(cmd, list) else cmd.split()
    try:
        process = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=shell)
    except Exception as error:
        logr.error("'{0}' failed: {1}".format(cmd, error))
        raise
    output, errors = process.communicate()
    if process.returncode != 0 or errors:
        if output:
            logr.error(output)
        if errors:
            logr.error(errors)
        sys.exit(process.returncode)
    return output, errors


def get_duration(path_to_wav):
    import wave
    import contextlib
    with contextlib.closing(wave.open(path_to_wav, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration
