import traceback, sys, subprocess

from ..utils.timeout import timeout, TimeoutError
from ..utils.timer import Timer


@timeout(15)
def run_python(content):
    if("import" not in content):
        with open("python_runner.py", "w+") as output:
            output.write("import numpy\n")
            output.write("import time\n")
            output.write("import datetime\n")
            output.write("import math\n")
            output.write("import random\n")
            output.write(content)

        try:
            return runCode()
        except SyntaxError as err:
            error_class = err.__class__.__name__
            # detail = err.args[0]
            line_number = err.lineno
            return f"{error_class} at line {line_number}"
        except TimeoutError as err:
            return "Time Limit Exceeded"
        except Exception as err:
            error_class = err.__class__.__name__
            cl, exc, tb = sys.exc_info()
            line_number = traceback.extract_tb(tb)[-1][1]
            return f"{error_class} at line {line_number}"
    else:
        return "Importing is not allowed right now."


def runCode():
    t = Timer()
    with t:
        result = subprocess.Popen(
            ["python3", "python_runner.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        result.wait()
    duration = t.duration

    stdout, stderr = result.communicate()
    if stderr == None:
        std_out = stdout.decode("utf-8")
        return f"{std_out}Execution Time: {duration}s"
    else:
        return stderr.decode("utf-8")

