#!/usr/bin/python3

print("content-type: text/html/Task7")
print()
import cgi
import subprocess

form = cgi.FieldStorage()
cmd  = form.getvalue("x")
o = subprocess.getoutput("sudo "+ cmd)
print(o)

