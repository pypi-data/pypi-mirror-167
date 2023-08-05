# 用法
.encode_p1(filename) : 加密一个文件
.decode_p1(filename) ： 解密
.encode(filename, N) ： 加密一个文件，拆成N份
.decode(filename, N) ： 从N份中还原出， 一个文件
## 生成dist目录和egginfo
python setup.py sdist

## 上传pypi
twine upload --skip-existing dist/*

## 安装
pip install --upgrade utils4file -i https://pypi.org/simple


## pypi登录 win10
%homepath%\.pypirc
```
[distutils] 
index-servers=pypi 
 
[pypi] repository = https://upload.pypi.org/legacy/ 
username = your account 
password = your path
```