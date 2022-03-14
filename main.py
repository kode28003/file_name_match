import glob
import shutil
import os

from operator import truediv
from re import I, T
from tkinter import E
from turtle import width
from PIL import Image

allFile=[]
clearFile=[]
shortSizeFile=[]


origin_file='C:\\Users\\elect\\Documents\\Python-same-name\\sample\\*.png' # 170枚
target_file_2x='C:\\Users\\elect\\Documents\\Python-same-name\\sample\\2.0x\\*.png'
target_file_3x='C:\\Users\\elect\\Documents\\Python-same-name\\sample\\3.0x\\*.png'


for x in glob.glob(origin_file):
    fileName1x =  x[x.rfind('\\')+1:x.rfind('')]
    img1x = Image.open(x)
    width1x = img1x.width
    allFile.append(fileName1x)

    for y in glob.glob(target_file_2x): #TODO 対象のファイルを指定
        fileNameTarget = y[y.rfind('\\')+1:y.rfind('')]
        imgTarget = Image.open(y)
        widthTarget=imgTarget.width

        if  fileName1x == fileNameTarget:
            clearFile.append(fileNameTarget)
            width_diff= (widthTarget + 2) - width1x * 2 #TODO 対象のファイルの倍率を指定
            if width_diff <= 0:
                shortSizeFile.append(fileNameTarget)

file_diff = set(allFile) ^ set(clearFile) #全ファイルから同名ファイルがあるものを削除
print('画像は全部で、'+ str(len(allFile))+'個です')
print(str(len(clearFile))+'個の拡大した画像があります')

print('\n')
print(str(len(file_diff))+'個のファイルが不足しています')
print(sorted(file_diff,reverse=False))


print('\n')
print(str(len(shortSizeFile))+'個のサイズ不足のファイルがあります')
print(sorted(shortSizeFile,reverse=False))

