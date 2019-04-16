Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nested=[[1,2,3], [4,5,6], [7,8,9]]
>>> flat=[]
>>> for x in nested;
SyntaxError: invalid syntax
>>> for x in nested:
	for y in x:
		z=y
		flat.append(z)
		flat

		
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> squares=[]
>>> squares=[x*x for x in flat]
>>> squares
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
>>> for x in flat:
	y=x*x
	squares.append(y)

	
>>> squares
[1, 4, 9, 16, 25, 36, 49, 64, 81, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> 
