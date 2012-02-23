def startPython(name):
  work = open(name, 'r')
  output = open(name + '.ShowCode', 'w')

  if name.endswith('.java'):
    java(work, output)

def java_count_braces(line, current_amount):
  if line.find('{') != -1:
    current_amount = current_amount + 1
  elif line.find('}') != -1:
    current_amount = current_amount - 1

  return current_amount

def java(input_file, output_file):

  buf = '';
  in_method = False
  in_comment = False
  num_opens = 0;

  for line in input_file:
    output_file.write(line) #Obviously we need to write every line.

    num_opens = java_count_braces(line, num_opens)

    buf = line.rstrip() + '\\n'

    if num_opens > 1:
      #Check to see if we have entered in a comment.
      if line.find('/*') != -1:
        in_comment = True

      if not in_comment:
        output_file.write('System.out.println("' + buf + '");' + '\n')
        buf = ''
      else:
        #Check to see if we are still in a comment.
        if line.find('*/') > -1: #Not in comment.
          in_comment = False


startPython('Voronoi.java')
