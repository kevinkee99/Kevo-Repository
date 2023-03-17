def get_highway_number():
    while True:
        number = int(input("Please enter a highway number (1 to 999): "))
        if number > 0 and number < 1000:
            return number
        else:
            print( number, "is not a valid highway number. Try again.")


    
def print_highway_info(n):
    while True:
        info = input("would you like to know about the highway type or direction? ")
        if info == 'type':
            if n > 0 and n < 100:
                print('I-' + str(n) + ' is primary highway.')
                break
            else:
                print('I-' + str(n) + ' is auxiliary highway.')
                break
        elif info == "direction":
            if n % 2 == 0:
                print(str(n) + ' goes east/west.')
                break
            else:
                print(str(n) + ' goes north/south.')
                break
                
        else:
            print('Please type a valid answer.')
            
           

if __name__ == "__main__":
    n = get_highway_number()
    print_highway_info(n)

from time import *

sleep(20)
    
        
    
    
    
        
  
