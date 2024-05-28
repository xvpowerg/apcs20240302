def sortFunc(x):
    return x[1]
v1 = input("請輸入序號")
v2 = input("請輸入重量")

data1 = list( map(int,v1.split(" ")) )
data2 = list( map(int,v2.split(" ") ) )
dataList = list(zip(data1,data2))
#reverse=True
#匿名函數lambda
#sortList = sorted(dataList,key = lambda x : x[1])
sortList = sorted(dataList,key = sortFunc)
for t in sortList:
    print(t)
