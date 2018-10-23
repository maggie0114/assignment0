#Run in the window system
import operator

list = ["trade-wars-news1.txt","trade-wars-news2.txt","trade-wars-news3.txt","trade-wars-news4.txt","trade-wars-news5.txt"]
total = ""
for i in list :
    f = open(i, "r+",encoding='UTF8')
    contents=f.read()
    total = total + contents
print(total)

tempList = total.split()
dict = {}


for ws in tempList:
    if ws not in dict:
        dict[ws] = 1
    else:
        dict[ws] += 1
print(tempList)

sorted_dict = sorted(dict.items(), key = operator.itemgetter(1), reverse = True)
print(sorted_dict)

print(sorted_dict[0:15])

