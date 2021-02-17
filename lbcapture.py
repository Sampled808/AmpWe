#!/usr/bin/env python3

import subprocess
import pulsectl

def record_sounds(output_file="record.wav", time=0):
    pulse = pulsectl.Pulse().source_list()[0].name
    fmt = "pulse"
    if time != 0:
        subprocess.check_output("ffmpeg -f {} -i {} -t {} -y {}".format(fmt, pulse, time/1000, output_file), stderr=subprocess.STDOUT, shell=True)
    else:
        try:
            subprocess.check_output("ffmpeg -f {} -i {} -y {}".format(fmt, pulse, output_file), stderr=subprocess.STDOUT, shell=True)
        except KeyboardInterrupt:
            pass
        except:
            return -1
    return 0
