import sys, os

try:
    global file
    file = sys.argv[1]
except Exception:
    print('fatal: no given file')
    sys.exit()

if not os.path.basename(file).endswith('.py'):
    print('fatal: no given .py')
    sys.exit()

keywords = ['False', 'await', 'else', 'import', 'pass', 'None', 'break', 'except', 'in', 'raise', 'True', 'class', 'finally', 'is', 'return', 'and', 'continue', 'for', 'lambda', 'try', 'as', 'def', 'from', 'nonlocal', 'while', 'assert', 'del', 'global', 'not', 'with', 'aync', 'elif', 'if', 'or', 'yield']

def has_keyword(line):
    for keyword in keywords:
        if keyword in line:
            return True
    return False

def handle_keywords(line, condition):
    line = handle_boolean(line, ('False' in line) or ('True' in line) or ('None' in line))
    line = handle_operator(line, (' and ' in line) or (' not ' in line) or (' or ' in line))
    return line

def handle_line_join(line, condition):
    if not condition: return line
    print('fatal: explicit/implicit not supported. report to ConnorTippets/pyanut if this is a mistake.')
    sys.exit()

def handle_boolean(line, condition):
    if not condition: return line
    line = line.replace('False', 'false')
    line = line.replace('True', 'true')
    line = line.replace('None', 'null')
    return line

def handle_operator(line, condition):
    if not condition: return line
    line = line.replace(' and ', ' && ')
    line = line.replace(' not ', ' !')
    line = line.replace(' or ', ' || ')
    return line

def transpile(source):
    source_structure = source.split('\n')
    transpiled_structure = []
    
    for line in source_structure:
        handle_line_join(line, line.endswith('\\') or line.replace(', ', ',').endswith(','))
        line = handle_keywords(line, has_keyword(line))
        transpiled_structure.append(line)
    
    return '\n'.join(transpiled_structure)

def main():
    python = open(file).read()
    squirrel = transpile(python)
    
    name = os.path.basename(file)
    output_path = os.path.join(*(os.path.split(file)[:-1] + (name.replace('.py', '.nut'),)))
    output = open(output_path, 'w')
    output.write(squirrel)
    print(f'success: {output_path}')

main()
