# code2word

- 环境准备:
1. 安装 python 3.6
2. 安装 python-docx: `pip install python-docx`

- 使用方法:
```
python run.py -s <source directory path> -m 'flat|deep' -t <target docx file path>\
  -i <include extension of scanned files> -e <exclude extension of scanned files>\
  -c <encoding of the files>
```

```
python run.py --source <source directory path> --mode \'flat|deep\' --target <target docx file path>\
  --include <include extension of scanned files> --exclude <exclude extension of scanned files>\
  --encoding <encoding of the files>
```

- 参数:\
-s : 代码项目文件夹路径\
-t : 目标 docx 文件路径\
-i : 扫描特定后缀名的文件\
-e : 不扫描特定后缀名的文件\
-c : 扫描到的文件编码(默认为 utf-8)\
-m : flat表示只有具体扫描到的文件所在文件夹作为标题，deep表示每个文件夹都作为一个标题

- 例子:\
`python .\run.py -s G:\xxx\yyy\*\src\main -m "deep" -t G:\test1.docx -i "java|yml"`

  其中 * 代表匹配所有文件夹，这些文件夹各占一个标题，整个路径只能有一个 *
