def print_body(height, arm):
    print(" "*5 + "X"*2)  
    print("#" + str(arm)*4 + "X"*2 + str(arm)*4 + "#")
    for i in range(0, height):
        print(" "*4 + "X"*4)
        

height = int(input('Height of the body: '))
arm = input('Character for the arms: ')

print_body(height, arm)
