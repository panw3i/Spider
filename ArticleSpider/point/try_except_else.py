# _*_ coding: utf-8 _*_
__date__ = "2017/8/28 14:16"

try:
    # 尝试打开一个文件
    txt = open("1.txt", "r+")

    # 如果无法执行"try"里面的语句,那么就执行except里面的语句  另外需要注意的是,"error"相当于是一个变量,用于存储错误信息的
except IOError as e:

    print("*** file open error", e)

    # 如果try里面的语句成功执行,那么就执行else里面的语句
else:
    for eachline in txt.read():
        print("成功打开"+eachline)

        txt.close()
