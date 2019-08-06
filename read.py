#coding: utf-8
from pyzbar.pyzbar import decode
from PIL import Image
import os
# QRコード(test.png)の指定
image = 'test.png'
# QRコードの読取り
data = decode(Image.open(image))
# コード内容テキストファイル(output.txt)に出力
f = open('output.txt','a')
f.write(data[0][0].decode('utf-8', 'ignore'))
f.close()
