list = [13,6,10,21,30,50,4,89,2]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]> list[j]:
            list[i],list[j] = list[j],list[i]
print(list)
key = 10
center = int(len(list)/2)
if key in list:
    while True:
        if list[center] > key:
            center = center-1
        elif list[center] < key:
            center = center+1
        elif list[center] ==key:
            print("要找的数字是%d在索引的%d"%(key,center))
            break
