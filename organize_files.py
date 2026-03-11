import os
import shutil

folder = "test_folder"

for file in os.listdir(folder):

    if file.endswith(".jpg") or file.endswith(".png"):
        target = "images"

    elif file.lower().endswith(".pdf"):
        target = "pdf"

    elif file.endswith(".xlsx"):
        target = "excel"

    else:
        target = "others"

    os.makedirs(target, exist_ok=True)

    shutil.move(os.path.join(folder, file), os.path.join(target, file))

"""
import os #导入和调用操作文件的文件夹、路径、系统信息的标准库
import shutil #导入和调用可移动、复制、删除文件的标准库

folder1 = "test_folder" #定义要整理的文件夹

for file in os.listdir(folder): #遍历文件夹里所有文件 os.listdir()是列出括号里文件夹里所有的文件
    if file.lower().endswith(".jpg") or file.endswith(".png"): #用lower()把文件夹里所有文件名字符串变成小写。然后用.endswith判断文件名字符串是否以jpg或png为结尾，如果是，此类文件都进入images文件夹
        target = "AA"
    else:
        target = "BB"

    os.makedirs(target, exist_ok=True) #创建分类文件夹，如果已经存在也不会报错（exist_ok=True）
    shutil.move(os.path.join(folder1, file), os.path.join(target, file)) #移动文件到新文件夹
"""
    
    
    

