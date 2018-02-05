#!/usr/bin/python
# Wii parental control password reset tool
#
# Copyright 2008-2009 Hector Martin Cantero <hector@marcansoft.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 or version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import time, urlparse

def application(environ, start_response):
    start_response("200 OK", [("Content-type","text/html")])
    yield """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<title>Wii Parental Control Password Resetter</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<style type="text/css">

.title {
    font-size: 18pt;
    font-family: sans-serif;
}

.response {
    font-size: 16pt;
    font-family: sans-serif;
}

.error {
    color: red;
    font-size: 16pt;
    font-family: sans-serif;
}


</style>
</head>
<body>
<div class="title">Wii Parental Control password reset tool</div>"""

    uri = environ["REQUEST_URI"]
    qs = urlparse.urlparse(uri).query
    form = urlparse.parse_qs(qs)

    ctime = time.time()

    def opt_date(delta):
        t = time.gmtime(ctime + delta * 3600 * 24)
        if delta == 0:
                selected = ' selected="selected"'
        else:
                selected = ""
        return '<option value="%02d%02d" %s>%s</option>'%(t.tm_mon,t.tm_mday,selected,time.strftime("%a, %d %b %Y",t))

    class CRC32:
        def __init__(self):
                self.gentable()


        def crc32(self, input, crc=0xffffffffl):
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
                                        crc = (crc >> 1) ^ 0xEDB88320l
                                else:
                                        crc >>= 1
                        self.table.append(crc)

    def error(s):
        return '<div class="error">%s</div>'%s

    def process():
        try:
                int(form["number"][0]) #validate
                if len(form["number"][0]) != 8 or not all([x in "0123456789" for x in form["number"][0]]):
                        raise ValueError()
        except:
                return error("Please provide a valid 8-digit confirmation number")

        try:
                int(form["date"][0]) #validate
                if len(form["date"][0]) != 4 or not all([x in "0123456789" for x in form["date"][0]]):
                        raise ValueError()
        except:
                return error("Invalid date")

        fullnum = form["date"][0] + form["number"][0][4:8]

        crc = CRC32().crc32(fullnum)
        code = ((crc ^ 0xaaaa) + 0x14c1) % 100000

        return '<div class="response">Your unlock code:<span class="code">%05d</span></div>'%code

    if form.has_key("submit"):
        yield process()

    yield """
<div class="form">
    <form action="/parental">
        <p>Confirmation Number:
                <input name="number" type="text" size="9" maxlength="8" value="" /></p>
        <p>Current Date in your timezone:
                <select name="date" size="1">"""
    yield opt_date(-1)
    yield opt_date(0)
    yield opt_date(1)
    yield """</select><br /></p>
        <p><input name="submit" type="submit" value="Get Reset Code" /></p>
    </form>
</div>
<p>
    <a href="http://validator.w3.org/check?uri=referer"><img
        src="http://www.w3.org/Icons/valid-xhtml10-blue"
        alt="Valid XHTML 1.0 Strict" height="31" width="88" /></a>
    <a href="http://jigsaw.w3.org/css-validator/">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
    <br />
    <a href="parental_src.py">Source code</a>
</p>
      
</body>
</html>"""
