n = int(input("請輸入次數"))
dataDict={}
for i in range(n):
   data = input("請輸入姓名成績用空白開")
   dataList = data.split(" ")
   k = dataList[0]
   v = int(dataList[1])
   tmpList = []
   if k in dataDict:
      tmpList = dataDict[k] 
   tmpList.append(v)
   dataDict[k] = tmpList

for k in dataDict:
    print(k,dataDict[k])
