mylist = [21, 5, 8, 52, 21, 87]
r_item = 21

#remove the item for all its occurrences
for item in mylist:
	if(item==r_item):
		mylist.remove(r_item)

print(mylist)