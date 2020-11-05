from sympy.abc import *
from sympy import solve
from sympy.parsing.sympy_parser import parse_expr

def solve_meThis(string_):
    try:
        lhs =  parse_expr(string_.split("=")[0])
        rhs =  parse_expr(string_.split("=")[1])
        solution = solve(lhs-rhs)
        return solution
    except:
        print("invalid equation")

def solver(operation):
    def operate(fb, sb, op):
        result = 0
        if operator == '+':
            result = int(first_buffer) + int(second_buffer)
        elif operator == '-':
            result = int(first_buffer) - int(second_buffer)
        elif operator == 'x':
            result = int(first_buffer) * int(second_buffer)
        return result

    if not operation or not operation[0].isdigit():
        return -1

    operator = ''
    first_buffer = ''
    second_buffer = ''

    for i in range(len(operation)):
        if operation[i].isdigit():
            if len(second_buffer) == 0 and len(operator) == 0:
                first_buffer += operation[i]
            else:
                second_buffer += operation[i]
        else:
            if len(second_buffer) != 0:
                result = operate(first_buffer, second_buffer, operator)
                first_buffer = str(result)
                second_buffer = ''
            operator = operation[i]

    result = int(first_buffer)
    if len(second_buffer) != 0 and len(operator) != 0:
        result = operate(first_buffer, second_buffer, operator)

    return result

def calculate(operation):
    string,head = '', None
    temp = string = str(operation)
    if 'D' in string:
        string = string.replace('D', '0')
    if 'G' in string:
        string = string.replace('G', '6')
    if 'b' in string:
        string = string.replace('b', '6')
    if 'B' in string:
        string = string.replace('B', '8')
    if 'Z' in string:
        string = string.replace('Z', '2')
    if 'S' in string:
        string = string.replace('S', '=')
    if 't' in string:
        string = string.replace('t', '+')
    if 'f' in string:
        string = string.replace('f', '7')
    if 'M' in string:
        string = string.replace('M', '-')
    if 'W' in string:
        string = string.replace('W', '-')
    if 'L' in string:
        string = string.replace('L', '/')
    if 'g' in string:
        string = string.replace('g', '9')
    if '=' not in string:
        if 'x' in string:
            string = string.replace('x', '*')
        if 'X' in string:
            string = string.replace('X', '*')
        return string, eval(string)
        
    operation = string
    string = ''
    for k in operation:
        if head is None:
            head = k
            string += head
        if k in ['+', '-', '*', '/', '%', '^', '='] or head in ['+', '-', '*', '/', '%', '^', '=']:
            head = k
            string += head
        elif k.isnumeric() and not head.isnumeric():
            head = k
            added = '**' + k
            string += added
        elif not k.isnumeric() and head.isnumeric():
            head = k
            added = '*' + k
            string += added
        
    
    print(string)
    if '=' not in string:
        return string, solver(string)
    else:
        return string, solve_meThis(string)
