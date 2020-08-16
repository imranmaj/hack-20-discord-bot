import os, traceback, sys

from timeout import timeout
from io import StringIO

@timeout(15)
def run_python(content):
    file = open("JavaSkeleton.java","r")

    for x in range(0,3):
        file.readlines()
    file = open("JavaSkeleton.java", "a")
    file.write(content)
    # run the java somehow?!?!?

    return file.read()