#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
========================================
101-safe_function.py
#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        a = fct(*args)
        return a
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
