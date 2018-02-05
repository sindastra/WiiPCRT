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

import sys

print ("WiiPCRT - Wii Parental Control (PIN) Reset Tool")
print ("Copyright (C) 2018 Sindastra <https://github.com/sindastra/WiiPCRT>")
print ("")

if len(sys.argv) < 2:
    print ("Usage: "+sys.argv[0]+" <request code>")
    sys.exit()

request_code = sys.argv[1]

rcerr = 0

try:
    int(request_code)
    if len(request_code) != 8:
        rcerr = 1
except ValueError:
    rcerr = 1

if rcerr :
    print ("Please enter an 8 *digit* code!")
    sys.exit()

import time

timezones = [0,1,2]
timezones[0] = "0109"
timezones[1] = "0110"
timezones[2] = "0111"

ctime = time.time()

def opt_date(delta):
    t = time.gmtime(ctime + (delta-1) * 3600 * 24)
    return time.strftime("%a, %d %b %Y",t)

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
print ("")
print ("Pick the code for your current time zone: (and make sure the Wii has the correct date set!)")
print ("")

for i in range(3):
    print ("-> (" + output_code(timezones[i]) + ") <- " + opt_date(i))
