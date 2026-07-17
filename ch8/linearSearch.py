# coding a linear search
nlist = [4,2,7,5,12,54,21,64,12,32]

print('list has items:' , nlist)
searchItem = int(input('enter a number to look for:'))

found = False #default case

for i in range(len(nlist)):
	if nlist[i] == searchItem:
		found = True
		print(searchItem, ' was found in the list at index:', i)
		break

if found == False:
	print(searchItem, ' was not in the list :( ')


