# # '''print("123456") #字符串
# # print(2333) 
# # print(2.333)
# # print(True)
# # print("哈哈"+"哈哈")
# # print(2<3)'''
# # a=input("请输入：")
# # print("input内容是：",a)
# # a=input("请输入内容")
# # b=input("请输入内容")
# # print(len(a+b))
# a=input("请输入姓名：")
# b=input("请输入性别：")
# c=input("请输入年龄：")
# d={name:a,sex:b,age:c}
# print(d)
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"x",j,"=",i*j,end=" ")
#     print()
# high = {}
# low = {}
# studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
# a = 0
# while a < len(studentlist):
#     chengji = int(input("请输入"+studentlist[a]+"的成绩:"))
#     if chengji >= 60:
#         high[studentlist[a]] = chengji  
#     else:
#        low[studentlist[a]] = chengji
#     a = a + 1
# print("大于60的",high)
# print("小于60的",low)

a = input("请输入：")
b = input("请输入：")
print("两个字符串长度为：",len(a)+len(b))
