t = int(input())
if(t < 1):
	print("Invalid Input")
else:
	arr = input().split(",")
	arr.sort(key = len)
	print(",".join(arr))
	print(arr[0])