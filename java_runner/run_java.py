import os, traceback, sys
import subprocess
from ..utils.timer import Timer

from ..utils.timeout import timeout, TimeoutError
from io import StringIO

@timeout(15)
def run_java(content):
    with open("JavaRunner.java", "w+") as output:
        #Create our file
        createHeader(output)
        output.write(content)
        endFile(output)

    try:
        return runCode()
    except TimeoutError as err:
        return "Time Limit Exceeded"


def runCode():
    #Run the file
    t = Timer()
    with t:
        result = subprocess.Popen(['java', 'JavaRunner.java'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result.wait()
    duration = t.duration


    stdout,stderr = result.communicate()
    if(stderr == None):
        std_out = stdout.decode("utf-8")
        return f"{std_out}Execution Time: {duration}s"
    else:
        return stderr.decode("utf-8")

def createHeader(output):
    output.write("public class JavaRunner{")


def endFile(output):
    output.write("}")


