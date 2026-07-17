# a = array
# i = leftmost element of the array 
# h = rightmost element of the array
# k = the element we search for 

def binary_search(a,i,h,k):
	if h >= i: # this is us checking if the list is empty 
		mid = I + (h-i)/2
		if a[mid] == k: # if matched up 
			return "k is found!"
		elif a[mid] > k: # if current is greater than desired num
			return binary_search(a,i,mid-1,k)
		else: # if current is less than than desired num
			return binary_search(a,i,mid+1,k)
	else: # if not found
		return "k is not found"
