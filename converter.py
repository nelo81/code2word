import os
from docx import Document

doc = Document()

def convert(dir, title=None, include=None, exclude=None, encoding='utf-8'):
  print('copy from diretory: ' + dir)

  if title is not None:
    doc.add_heading(title, 1)
  
  if include is not None:
    inc=include.split('|')
  else:
    inc=None
  
  if exclude is not None:
    exc=exclude.split('|')
  else:
    exc=None

  currentdir = ''

  for root, dirs, files in os.walk(dir,False):
    for file in files:
      if (inc is None or os.path.splitext(file)[1][1:] in inc) and (exc is None or os.path.splitext(file)[1][1:] not in exc):
        filepath = os.path.join(root,file).replace('\\','/')
        with open(filepath,encoding=encoding) as f:
          content = f.read()
          thisdir = filepath[len(dir)+1:filepath.rfind('/')]
          if currentdir != thisdir:
            currentdir = thisdir
            doc.add_heading(thisdir, 2)
          doc.add_heading(filepath[filepath.rfind('/')+1:], 3)
          doc.add_paragraph(content)
          doc.add_page_break()