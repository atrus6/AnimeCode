def startPython(name):
    work = open(name, 'r')
    output = open(name + '.ShowCode', 'w')

    for line in work:
        line.expandtabs(4)
        before = len(line)
        after = len(line.lstrip())

        prefix = ' '*(before - after)
        
        output.write('\n' + line)
        line = line.rstrip()
        line = line.replace('"', '\\"')
        line = line.replace("'", "\\'")
        
        if line.isspace() == False or len(line) != 0:
            mys = prefix + 'print \'' + line + '\''
            if mys.find("print ''") == -1:
                if line.endswith(':') == False:
                    output.write(mys)
                else:
                    output.write('    ' + mys)

startPython('test.py')
