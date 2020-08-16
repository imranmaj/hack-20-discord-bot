import os, traceback, sys

from timeout import timeout
from io import StringIO

@timeout(15)
def run_python(content):
    output = StringIO()
    
    sys.stdout = output
    sys.stderr = output

    try: 
        exec(content)
    except SyntaxError as err:
        error_class = err.__class__.__name__
        # detail = err.args[0]
        line_number = err.lineno
        return f"{error_class} at line {line_number}"
    except TimeoutError as err:
        return "Time limit reached"
    except Exception as err:
        error_class = err.__class__.__name__
        cl, exc, tb = sys.exc_info()
        line_number = traceback.extract_tb(tb)[-1][1]
        return f"{error_class} at line {line_number}"
    return output.getvalue()

