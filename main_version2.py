# -*- coding: utf-8 -*-

import glob
import shutil
import os

from operator import truediv
from re import I, T
from tkinter import E
from turtle import width
from PIL import Image

allFile=[]
clearFile2x=[]
shortSizeFile2x=[]
clearFile3x=[]
shortSizeFile3x=[]


origin_file='C:\\Users\\elect\\Documents\\lion-toothquest-app\\assets\\images\\*.png'
target_file_2x='C:\\Users\\elect\\Documents\\lion-toothquest-app\\assets\\images\\2.0x\\*.png'
target_file_3x='C:\\Users\\elect\\Documents\\lion-toothquest-app\\assets\\images\\3.0x\\*.png'


for x in glob.glob(origin_file):
    #fileName1x =  x[x.rfind('\\')+1 : x.rfind('')]
    img1x = Image.open(x)
    width1x = img1x.width
    fileName1x = os.path.basename(x)
    allFile.append(fileName1x)

    for y in glob.glob(target_file_2x): #TODO 対象のファイルを指定
        #fileNameTarget2x = y[y.rfind('\\')+1 : y.rfind('')]
        imgTarget2x = Image.open(y)
        widthTarget2x = imgTarget2x.width
        fileName2x = os.path.basename(y)

        if  fileName1x == fileName2x:
            clearFile2x.append(fileName2x)
            width_diff_2x = widthTarget2x - width1x * 2 #倍率指定
            if width_diff_2x <= 0:
                shortSizeFile2x.append(fileName2x)

    for z in glob.glob(target_file_3x):
        #fileNameTarget3x = z[z.rfind('\\')+1 : z.rfind('')]
        imgTarget3x = Image.open(z)
        widthTarget3x = imgTarget3x.width
        fileName3x = os.path.basename(z)

        if  fileName1x == fileName3x:
            clearFile3x.append(fileName3x)
            width_diff_3x = widthTarget3x - width1x * 3 #倍率指定
            if width_diff_3x <= 0:
                shortSizeFile3x.append(fileName3x)



file_diff_2x = set(allFile) ^ set(clearFile2x)
file_diff_3x = set(allFile) ^ set(clearFile3x)  
#全ファイルから同名ファイルがあるものを削除
print('\n')
print('1倍の画像は全部で、'+ str(len(allFile))+'個です')
print('--------------------------------')
print('### 2倍の画像 ###')
print(str(len(clearFile2x))+'個の2倍に拡大された画像があります')
print(str(len(file_diff_2x))+'個のファイルが不足しています')
print(sorted(file_diff_2x,reverse=False))

print('\n')
print(str(len(clearFile2x))+'個の2倍に拡大された画像の内、'+str(len(shortSizeFile2x))+'個のサイズ不足のファイルがあります')
print(sorted(shortSizeFile2x,reverse=False))

print('--------------------------------')
print('### 3倍の画像 ###')
print(str(len(clearFile3x))+'個の3倍に拡大された画像があります')
print(str(len(file_diff_3x))+'個のファイルが不足しています')
print(sorted(file_diff_3x,reverse=False))

print('\n')
print(str(len(clearFile3x))+'個の3倍に拡大された画像の内、'+str(len(shortSizeFile3x))+'個のサイズ不足のファイルがあります')
print(sorted(shortSizeFile3x,reverse=False))
print('\n')


