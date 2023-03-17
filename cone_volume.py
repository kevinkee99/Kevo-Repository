radius = float(input('Type the radius of the cone: ', ))
height = float(input('Type the height of the cone: ', ))
pi = 3.142

v = pi*radius**2*(height/3)
print('The volume of the cone is: ', end=' ')
print(f'{v:.2f}')
