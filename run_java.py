import os, traceback, sys
import subprocess

from timeout import timeout
from io import StringIO

def run_java(content):
    output = open("JavaRunner.java", "w+")

    #Create our file
    createHeader(output)
    output.write(content)
    endFile(output)

    output.close()

    return runCode()


def runCode():
    output = StringIO()

    sys.stdout = output
    sys.stderr = output

    #Run the file
    result = subprocess.run(['java JavaRunner.java'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # if(result.stdout.decode('utf-8') != ""):
    return result.stdout.decode('utf-8')
    # else:
        # return result.stderr

def createHeader(output):
    output.write("public class JavaRunner{")


def endFile(output):
    output.write("}");

