def print_legs(height, shoe_string):
    reverse = shoe_string[::-1]
    print(" "*3 + "="*4)
    for i in range(0, height):
        print((" "*2 + "||")*2)
    print(str(shoe_string) + " "*2 + reverse)
    
height = int(input("Height of legs: "))
shoe_string = input("4-character string for the shoes: ")

print_legs(height, shoe_string)
