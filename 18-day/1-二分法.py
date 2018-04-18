"""
list = [1,3,5,8,10,20,21,30,34,47,89]

key = 21

center = int(len(list)/2)

#第一步 判断要找的在不在

if key in list:
    while True:
        if list[center] > key:
            center = center -1
        elif list[center] < key:
            center = center +1
        elif list[center] == key:
            print("要找的数字是%d在索引%d"%(key,center))
            break
"""


list = [1,3,5,8,10,20,21,30,34,47,89]
key = 30
center = int(len(list)/2)
if key in list:
    while True:
        if list[center] > key:
            center = center-1
        elif list[center] < key:
            center = center+1
        elif list[center] == key:
            print("要找的数字是%d在索引%d"%(key,center))
            break
