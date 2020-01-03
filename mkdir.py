#目标是读取txt的每一行数据创建对应名字的文件夹
#1通过函数调用解决创建固定的文件夹
#2创建一个txt文件输出里面的内容输出
#3将txt输出内容和创建文件夹链接完成任务
#4后续补充检测文本文件是否存在，不在报错
#5后续补充如果已经有了文本中的文件夹跳过这个文件名创建下一个
#结束
#反思：目前创建的文件夹目录固定、文本文档位置固定
#完善功能：
#1.先把文件夹目录改为交互式用户设置
#2.检测txt文件是否存在
#!/usr/bin/python
#-*-coding:utf-8-*-
import os
def mkdir(path):
  folder=os.path.exists(path)
  if not folder:
    os.makedirs(path)
    print(path+"---OK---")
  else:
    print(path+"---There is this folder!---")
 
if __name__=='__main__':
  file = "D:\db\images"
  with open('labels.txt','r', encoding='utf-8') as f:
    lines=f.readlines()
    for line in lines:
      #folder=file+line
      folder=line
      #strip()方法移除字符串头尾指定的字符
      folder=folder.strip()
      mkdir(folder)