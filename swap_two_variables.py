#python swap program
x=input('Enter value of x: ')
y=input('Enter value of y: ')

#create temporary variable and swap
temp = 0
temp = x
x = y
y = temp
 #print the result
print('The value of x after swapping:{}'.format(x))
print('The value of y after swapping:{}'.format(y))