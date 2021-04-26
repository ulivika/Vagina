def fib1( ):
	ass=[0,0,0,0,0,0,0,0,0,0,0] 
	ass[0]=1
	ass[-1]=1
	print(ass)

def fib2( ):
	ass=[]
	for i in range(10):
		ass.append(i%2)
	print(ass)

def fib3( ):
	ass=[]
	for i in range(1,10,2):
		ass.append(i)
	print(ass)
	
def fib4():
	ass=[]
	x = int(input('Введите первый элемент- '))
	d = int(input('Ведите разность- '))
	for i in range(x,x+100,d):
		ass.append(i)
	print(ass)
		
	
def fib5():
	ass=[]
	for i in range(2,100,2):
		ass.append(i)
	print(ass)
	
def fib6():
	ass=[]
	for i in range(99,1,-3):
		ass.append(i)
	print(ass)
		
def fib8():
	ass=[]
	n = int(input('Введите число - '))
	for i in range(2,n+1,):
		if i%i=0:
			print(i)
	print(ass)

def fib9():
	ass=[]
	

change = input( "Введите  номер задачи - " )
if change== "1" :
		fib1()
elif change== "2" :
		fib2()	
elif change== "3" :
		fib3()	
elif change == '4':
		fib4()
elif change == '5':
		fib5()
elif change == '6':
		fib6()
elif change == '8':
		fib8()	
elif change == '9':
		fib9()	
