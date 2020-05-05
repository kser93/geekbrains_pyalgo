import sys


def trace_lines(frame, event, arg):
    print(event)
    if event != 'line':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    print(f'\t{func_name} line {line_no}')


def trace_calls(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    print('Call to %s on line %s of %s' % (func_name, line_no, filename))
    if func_name in mooo:
        # Trace into this function
        return trace_lines
    return


def c(input):
    print('input =', input)
    print('Leaving c()')


def b(arg):
    val = arg * 5
    c(val)
    print('Leaving b()')


def a():
    b(2)
    print('Leaving a()')


mooo = ['b']

sys.settrace(trace_calls)
a()
