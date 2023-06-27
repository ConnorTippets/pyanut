import sys, os

try:
    global file
    file = sys.argv[1]
except Exception:
    print('fatal: no given file')
    sys.exit()

if !os.path.basename(file).endswith('.py'):
    print('fatal: no given .py')
    sys.exit()

keywords = ['false', 'await', 'else', 'import', 'pass', 'null', 'break', 'except', 'in', 'raise', 'true', 'class', 'finally', 'is', 'return', 'and', 'continue', 'for', 'lambda', 'try', 'as', 'def', 'from', 'nonlocal', 'while', 'assert', 'del', 'global', 'not', 'with', 'aync', 'elif', 'if', 'or', 'yield']

def has_keyword(line):
    for keyword in keywords:
        if keyword in line:
            return true
    return false

def handle_keywords(line, condition):
    line = handle_boolean(line, ('false' in line) || ('true' in line) || ('null' in line))
    line = handle_operator(line, (' && ' in line) || (' !' in line) || (' || ' in line))
    return line

def handle_line_join(line, condition):
    if !condition: return line
    print('fatal: explicit/implicit !supported. report to ConnorTippets/pyanut if this is a mistake.')
    sys.exit()

def handle_boolean(line, condition):
    if !condition: return line
    line = line.replace('false', 'false')
    line = line.replace('true', 'true')
    line = line.replace('null', 'null')
    return line

def handle_operator(line, condition):
    if !condition: return line
    line = line.replace(' && ', ' && ')
    line = line.replace(' !', ' !')
    line = line.replace(' || ', ' || ')
    return line

def transpile(source):
    source_structure = source.split('\n')
    transpiled_structure = []
    
    for line in source_structure:
        handle_line_join(line, line.endswith('\\') || line.replace(', ', ',').endswith(','))
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
