#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Eduard Trott
# @Date:   2015-12-17 14:41:33
# @Email:  etrott@redhat.com
# @Last modified by:   etrott
# @Last Modified time: 2015-12-17 16:47:09

import logging
import os
import subprocess
import sys


# Load logging before anything else
logging.basicConfig(format='>> %(message)s')
logr = logging.getLogger('ring')


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

# AUDIO_DESTINATION = '"Blue Jeans"'
AUDIO_DESTINATION = '"SoundRecorder"'

AUDIO_FILE = os.path.expanduser("~/Downloads/23265__digifishmusic__spanner-chime-soft.wav")
AUDIO_SOURCE = '"Monitor of Built-in Audio Analog Stereo"'
AUDIO_VOLUME = 70000

MIC_SOURCE = '"Built-in Audio Analog Stereo"'
MIC_VOLUME = 30000
import time
if __name__ == "__main__":
    audio_sources_desc = run(
        "pactl list sources|sed -n -e 's/\t\tdevice\.description = //p'")[0].split('\n')[:-1]
    audio_sources_names = run(
        "pactl list sources|sed -n -e 's/\tName: //p'")[0].split()
    audio_source = dict(zip(audio_sources_desc, audio_sources_names))
    # print audio_source
    # Identify BJ Source-Output
    source_outputs_info = run(
        "pactl list source-outputs|sed -n -e 's/Source Output #//p; s/\t\tapplication.name = //p'")[0].split('\n')[:-1]
    try:
        source_output_idx = source_outputs_info[
            source_outputs_info.index(AUDIO_DESTINATION) - 1]
    except:
        raise RuntimeError("Can't find recording")
    # Load ring_bell
    run("pactl upload-sample %s" %
        ("%s ringbell" % (AUDIO_FILE)))
    # Move source output to monitor and adjust a volume
    run("pactl move-source-output %s %s" % (source_output_idx,
                                            audio_source[AUDIO_SOURCE]))
    run("pactl set-source-output-volume %s %s" %
        (source_output_idx, AUDIO_VOLUME))
    # Play sound
    run("pactl play-sample ringbell alsa_output.pci-0000_00_1b.0.analog-stereo")
    time.sleep(get_duration(AUDIO_FILE))
    # Move source output back and adjust a volume
    run("pactl move-source-output %s %s" %
        (source_output_idx, audio_source[MIC_SOURCE]))
    run("pactl set-source-output-volume %s %s" %
        (source_output_idx, MIC_VOLUME))
