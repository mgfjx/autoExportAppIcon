#!/usr/bin/env python
# coding: utf-8

# 简介: iOS app图标生成脚本, 生成后直接拖入xcode中就行
# 用法: python autoExportAppIcon.py /path/xxx.png

import sys
import os

try:
    from PIL import Image
except:
    print ('\033[31m' + '缺少Image模块，正在安装Image模块，请等待...' + '\033[0m')
    success = os.system('python -m pip install Image')
    if success == 0:
      print('\033[7;32m' + 'Image模块安装成功.' + '\033[0m')
      from PIL import Image
    else:
      print ('\033[31m' + 'Image安装失败，请手动在终端执行：\'python -m pip install Image\'重新安装.' + '\033[0m')
      quit()

outPutPath = os.path.expanduser('~') + '/Desktop/AppIcon/'

if not os.path.exists(outPutPath):
    os.mkdir(outPutPath)

if len(sys.argv) <= 1:
    print ('\033[31m' + '请输入图片路径,eg: python autoExportAppIcon.py /path/xxx.png' + '\033[0m')
    quit()

ImageName = sys.argv[1]
# print('图片名字为：' + ImageName)
originImg = ''
try:
    originImg = Image.open(ImageName)
except:
    print ('\033[31m' + '\'' + ImageName + '\'' + '，该文件不是图片文件，请检查文件路径.' + '\033[0m')
    quit()

# 20x20
img0 = originImg.resize((20,20), Image.ANTIALIAS)
img1 = originImg.resize((40,40), Image.ANTIALIAS)
img2 = originImg.resize((60,60), Image.ANTIALIAS)
img0.save(outPutPath + 'AppIcon20x20.png',"png")
img1.save(outPutPath + 'AppIcon20x20@2x.png',"png")
img2.save(outPutPath + 'AppIcon20x20@3x.png',"png")

# 29x29
img3 = originImg.resize((29,29), Image.ANTIALIAS)
img4 = originImg.resize((58,58), Image.ANTIALIAS)
img5 = originImg.resize((87,87), Image.ANTIALIAS)
img3.save(outPutPath + 'AppIcon29x29.png',"png")
img4.save(outPutPath + 'AppIcon29x29@2x.png',"png")
img5.save(outPutPath + 'AppIcon29x29@3x.png',"png")

# 40x40
img6 = originImg.resize((40,40), Image.ANTIALIAS)
img7 = originImg.resize((80,80), Image.ANTIALIAS)
img8 = originImg.resize((120,120), Image.ANTIALIAS)
img6.save(outPutPath + 'AppIcon40x40.png',"png")
img7.save(outPutPath + 'AppIcon40x40@2x.png',"png")
img8.save(outPutPath + 'AppIcon40x40@3x.png',"png")

# 60x60
img9 = originImg.resize((120,120), Image.ANTIALIAS)
img10 = originImg.resize((180,180), Image.ANTIALIAS)
img9.save(outPutPath + 'AppIcon60x60@2x.png',"png")
img10.save(outPutPath + 'AppIcon60x60@3x.png',"png")

# ipad
img11 = originImg.resize((76,76), Image.ANTIALIAS)
img12 = originImg.resize((152,152), Image.ANTIALIAS)
img13 = originImg.resize((167,167), Image.ANTIALIAS)
img11.save(outPutPath + 'AppIcon76x76.png',"png")
img12.save(outPutPath + 'AppIcon76x76@2x.png',"png")
img13.save(outPutPath + 'AppIcon83.5x83.5@2x.png',"png")


# 1024x1024 xcode10
img14 = originImg.resize((1024,1024), Image.ANTIALIAS)
img14.save(outPutPath + 'AppIcon1024x1024.png',"png")

# 创建Contents.json文件

content = '''
{
  "images" : [
    {
      "idiom" : "iphone",
      "size" : "20x20",
      "filename" : "AppIcon20x20@2x.png",
      "scale" : "2x"
    },
    {
      "idiom" : "iphone",
      "size" : "20x20",
      "filename" : "AppIcon20x20@3x.png",
      "scale" : "3x"
    },
    {
      "size" : "29x29",
      "idiom" : "iphone",
      "filename" : "AppIcon29x29.png",
      "scale" : "1x"
    },
    {
      "size" : "29x29",
      "idiom" : "iphone",
      "filename" : "AppIcon29x29@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "29x29",
      "idiom" : "iphone",
      "filename" : "AppIcon29x29@3x.png",
      "scale" : "3x"
    },
    {
      "size" : "40x40",
      "idiom" : "iphone",
      "filename" : "AppIcon40x40@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "40x40",
      "idiom" : "iphone",
      "filename" : "AppIcon40x40@3x.png",
      "scale" : "3x"
    },
    {
      "size" : "60x60",
      "idiom" : "iphone",
      "filename" : "AppIcon60x60@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "60x60",
      "idiom" : "iphone",
      "filename" : "AppIcon60x60@3x.png",
      "scale" : "3x"
    },
    {
      "idiom" : "ipad",
      "size" : "20x20",
      "filename" : "AppIcon20x20.png",
      "scale" : "1x"
    },
    {
      "idiom" : "ipad",
      "size" : "20x20",
      "filename" : "AppIcon20x20@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "29x29",
      "idiom" : "ipad",
      "filename" : "AppIcon29x29.png",
      "scale" : "1x"
    },
    {
      "size" : "29x29",
      "idiom" : "ipad",
      "filename" : "AppIcon29x29@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "40x40",
      "idiom" : "ipad",
      "filename" : "AppIcon40x40.png",
      "scale" : "1x"
    },
    {
      "size" : "40x40",
      "idiom" : "ipad",
      "filename" : "AppIcon40x40@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "76x76",
      "idiom" : "ipad",
      "filename" : "AppIcon76x76.png",
      "scale" : "1x"
    },
    {
      "size" : "76x76",
      "idiom" : "ipad",
      "filename" : "AppIcon76x76@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "83.5x83.5",
      "idiom" : "ipad",
      "filename" : "AppIcon83.5x83.5@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "1024x1024",
      "idiom" : "ios-marketing",
      "filename" : "AppIcon1024x1024.png",
      "scale" : "1x"
    }
  ],
  "info" : {
    "version" : 1,
    "author" : "xcode"
  }
}
'''
f = open(outPutPath + 'Contents.json', 'w')
f.write(content)

print('\033[7;32m' + '文件输出文件夹：' + outPutPath + '\033[0m')
os.system('open ' + outPutPath)
