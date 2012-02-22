def startPython(name):
  work = open(name, 'r')
  output = open(name + '.ShowCode', 'w')


def java(input_file, output_file):

  buf = '';
  in_method = False
  in_comment = False
  num_opens = 0;

  for line in input_file:
    if num_opens < 2:
      buf += line + '\\n'
      if line.find('{'):
        num_opens += 1
      elif line.find('}')
        num_opens -= 1
    else
      if not in_comment:
        output.write('System.out.println("' + buf + '");')
      else:
        #Check to see if we are still in a comment.
        if line.find('*/') > -1: #Not in comment.
          in_comment = False


startPython('test.py')
