values = input("請輸入三個數字用空格隔開")
print(values)
strList = values.split(" ")
print(strList)
intList = []
for v in strList:
    intList.append(int(v))
print(intList)    
