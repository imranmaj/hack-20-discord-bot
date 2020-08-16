import os, traceback, sys
import subprocess

from timeout import timeout
from io import StringIO

@timeout(15)
def run_java(content):
    output = open("JavaRunner.java", "w+")

    #Create our file
    createHeader(output)
    output.write(content)
    endFile(output)

    output.close()

    try:
        return runCode()
    except Exception as err:
        return "Time Limit Exceeded"


def runCode():
    #Run the file
    result = subprocess.Popen(['java', 'JavaRunner.java'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    stdout,stderr = result.communicate()
    if(stderr == None):
        return stdout.decode("utf-8")
    else:
        return stderr.decode("utf-8")

def createHeader(output):
    output.write("public class JavaRunner{")


def endFile(output):
    output.write("}");

