# code2word

使用方法:
```
python run.py -s <source directory path> -t <target docx file path>\
  -i <include extension of scanned files> -e <exclude extension of scanned files>\
  -c <encoding of the files>
```

例子:\
`python .\run.py -s G:\xxx\yyy\*\src\main -t G:\test1.docx -i "java|py|yml"`

- 其中 * 代表匹配所有文件夹，整个路径只能有一个 *
