#!/usr/bin/python
#
# WiiPCRT
# Wii Parental Control (PIN) Reset Tool - Based on https://wii.marcan.st/parental_src.py
#
# Copyright (C) 2018 Sindastra <https://github.com/sindastra/WiiPCRT>
# Copyright 2008-2009 Hector Martin Cantero <hector@marcansoft.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, os

def has_arg(string):
    return (string in sys.argv or "-"+string in sys.argv or "--"+string in sys.argv or "/"+string in sys.argv)

def has_args(array):
    for i in array:
        if has_arg(i):
            return True
    return False

def printhelp():
    print ("Usage: "+sys.argv[0]+" [options] <request code>")
    print ("The following options are available:")
    print ("-h or --help     Show this help page.")
    print ("-t or --today    Only show unlock code for today's date.")

print ("WiiPCRT - Wii Parental Control (PIN) Reset Tool")
print ("Copyright (C) 2018 Sindastra <https://github.com/sindastra/WiiPCRT>")
print ("Official Website: https://sindastra.github.io/WiiPCRT/")
print ("---------------------------------------------------------------------")

if has_args(["help","h","?"]):
    printhelp()
    sys.exit(0)

only_today = has_args(["today","t"])

if len(sys.argv) < 2:
    printhelp()
    print ("Alternatively:")
    sys.stdout.write ("Input your 8 *digit* request code now: ")
    sys.stdout.flush()
    request_code = sys.stdin.readline().rstrip()
    print ("---------------------------------------------------------------------")
else:
    request_code = sys.argv[len(sys.argv)-1]

rcerr = 0

try:
    int(request_code)
    if len(request_code) != 8:
        rcerr = 1
except ValueError:
    rcerr = 1

if rcerr :
    print ("Please enter an 8 *digit* request code!")
    if os.name == "nt":
        input ("Press Enter to exit now and try again.")
    sys.exit()

import time
ctime = time.time()

def timezone(diff):
    t = time.gmtime(ctime + (0 +diff) * 3600 * 24)
    return time.strftime("%m%d",t)

timezones = [0,1,2]
timezones[0] = timezone(-1)
timezones[1] = timezone(0)
timezones[2] = timezone(+1)

def opt_date(delta):
    t = time.gmtime(ctime + (delta-1) * 3600 * 24)
    return time.strftime("%b. %d (%A)",t)

class CRC32:
    def __init__(self):
            self.gentable()

    def crc32(self, input, crc=0xffffffff):
            count = len(input)
            i = 0
            while count != 0:
                    count -= 1
                    temp1 = (crc >> 8) & 0xFFFFFF
                    temp2 = self.table[(crc ^ ord(input[i])) & 0xFF]
                    crc = temp1 ^ temp2
                    i += 1
            return crc

    def gentable(self):
            self.table = []
            for i in range(256):
                    crc = i
                    for j in range(8):
                            if crc & 1:
                                    crc = (crc >> 1) ^ 0xEDB88320
                            else:
                                    crc >>= 1
                    self.table.append(crc)

def output_code(timezone):
    fullnum = timezone + request_code[4:8]
    crc = CRC32().crc32(fullnum)
    code = ((crc ^ 0xaaaa) + 0x14c1) % 100000
    return str(code).zfill(5)

print ("This program is distributed in the hope that it will be useful,")
print ("but WITHOUT ANY WARRANTY; without even the implied warranty of")
print ("MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the")
print ("GNU General Public License for more details.")
print ("")
print ("You should have received a copy of the GNU General Public License")
print ("along with this program.  If not, see <http://www.gnu.org/licenses/>.")
print ("---------------------------------------------------------------------")
print ("Make sure the Wii and this computer have the correct (same) date set!")
if not only_today:
    print ("Pick the code for your current time zone (date):")
print ("")

for i in range(1 if only_today else 3):
    print ("(" + output_code(timezones[1 if only_today else i]) + ") <- Unlock key for " + opt_date(1 if only_today else i))

if os.name == "nt":
    print ("---------------------------------------------------------------------")
    input ("Press Enter to exit.")
