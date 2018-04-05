import os, sys, getopt
from converter import convert, doc

if __name__ == '__main__':

  src = None
  mode = 'flat'
  target = None
  include = None
  exclude = None
  encoding = 'utf-8'
  myhelp = 'run.py -s <source directory path> -m \'flat|deep\' -t <target docx file path>\
  -i <include extension of scanned files> -e <exclude extension of scanned files>\
  -c <encoding of the files>'
  argv = sys.argv[1:]

  try:
    opts, args = getopt.getopt(argv,'hs:m:t:i:e:c:',['source=','mode=','target=','include=','exclude=','encoding='])
  except expression as identifier:
    print(myhelp)
    sys.exit(2)

  for opt, arg in opts:
    if opt == '-h':
      print(myhelp)
      sys.exit(2)
    elif opt in ('-s','--source'):
      src = arg
    elif opt in ('-m','--mode'):
      mode = arg
    elif opt in ('-t','--target'):
      target = arg
    elif opt in ('-i','--include'):
      include = arg
    elif opt in ('-e','--exclude'):
      exclude = arg
    elif opt in ('-c','--encoding'):
      exclude = arg

  if src is None or target is None:
    print('source and target is needed')
    sys.exit(2)

  pos = src.find('*')
  if pos == -1:
    convert(src, mode=mode, include=include, exclude=exclude, encoding=encoding)
  else:
    presrc = src[0:pos]
    dirs = os.listdir(presrc)
    for dir in dirs:
      convert(presrc + dir + src[pos+1:], mode=mode, title=dir, include=include, exclude=exclude, encoding=encoding)

  doc.save(target)