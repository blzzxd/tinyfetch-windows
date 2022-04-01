# Artur Asimov
# https://github.com/artur-asimov/tinyfetch-windows

import psutil
import platform
import socket
import os
import cpuinfo
import sys
from datetime import datetime

ascii = (
    '##### #####',
    '##### #####',
    '##### #####',
    '           ',
    '##### #####',
    '##### #####',
    '##### #####',
)
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)

uname = platform.uname()
svem = psutil.virtual_memory()

# Storing configuration settings in some variables
output = f"""\t    {"-"*4}{os.getlogin()}@{platform.node()}{"-"*4}
{ascii[0]} System: {uname.system}
{ascii[1]} Release: {uname.release}
{ascii[2]} Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}
{ascii[3]} Memory: {get_size(svem.used)} / {get_size(svem.total)}
{ascii[4]} Processor: {cpuinfo.get_cpu_info()['brand_raw']}
{ascii[5]} IP Address: {socket.gethostbyname(socket.gethostname())}
{ascii[6]}"""
if len(sys.argv) == 2 :
    if str(sys.argv[1]) == 'noip' :
        output = f"""\t    {"-"*4}{os.getlogin()}@{platform.node()}{"-"*4}
{ascii[0]} System: {uname.system}
{ascii[1]} Release: {uname.release}
{ascii[2]} Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}
{ascii[3]} Memory: {get_size(svem.used)} / {get_size(svem.total)}
{ascii[4]} Processor: {cpuinfo.get_cpu_info()['brand_raw']}
{ascii[5]} IP Address: ##.##.##.##
{ascii[6]} """

print(output)
