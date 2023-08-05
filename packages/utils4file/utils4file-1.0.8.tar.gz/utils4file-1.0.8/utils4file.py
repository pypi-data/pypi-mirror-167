import base64
import hashlib

def add(a,b):
    return a+b

# 编码 70M1秒完成
def encode_p1(filename):
    with open(filename , 'rb') as f:
        text = f.read()
    ttt =  base64.b64encode(text)
    with open(filename+'.b64.txt','wb' ) as f:
        f.write(ttt)

def decode_p1(filename,piece=1):
    with open(filename , 'r') as f:
        text = f.read()
    de = base64.b64decode(text)
    # print(de)
    with open(filename+'.decode','wb' ) as f:
        f.write(de)
        
# 编码 70M1秒完成
def encode(filename, piece=1):
    with open(filename , 'rb') as f:
        text = f.read()
    ttt =  base64.b64encode(text)
    index = int (len(ttt) / piece)
    for i in  range(piece):
        with open(filename+ '_' + str(i) +'.b64.txt','wb' ) as f:
            f.write(ttt[index * i : index*(1+i)])

def decode(filename,piece=1):
    sss = ''
    for i in  range(piece):
        with open(filename + '_' + str(i) +'.b64.txt', 'r') as f:
            sss += f.read()     
    de = base64.b64decode(sss)
    with open(filename+'.decode','wb' ) as f:
        f.write(de)


 
def md5(file_name):
    """
    计算文件的md5
    :param file_name:
    :return:
    """
    m = hashlib.md5()   #创建md5对象
    with open(file_name,'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)  #更新md5对象
 
    return m.hexdigest()    #返回md5对象


if __name__ == '__main__':
    a = decode(r'C:\Users\Administrator\Desktop\ernie.bz2', 3)
    print(a)