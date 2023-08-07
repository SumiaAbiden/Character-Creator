def print_head(hair, eye):
    print(str(hair)*12)
    print(str(hair) + "|" + " "*8 + "|" + str(hair))
    print(str(hair) + "|" + " "*2 + str(eye) + " "*2 + str(eye) + " "*2 + "|" + str(hair))
    print(" " + "|" + " "*3 + "/" + "\\" + " "*3 + "|")
    print(" " + "|" + " "*8 + "|")
    print(" " + "\\" + " "*2 + "'--'" + " "*2 + "/")
    print(" "*3 + "-"*6 + " "*3)


def print_body(height, arm):
    print(" "*5 + "X"*2)  
    print("#" + str(arm)*4 + "X"*2 + str(arm)*4 + "#")
    for i in range(0, height):
        print(" "*4 + "X"*4)


def print_legs(height, shoe_string):
    reverse = shoe_string[::-1]
    print(" "*4 + "="*4)
    for i in range(0, height):
        print(" " + (" "*2 + "||")*2)
    print(" " + str(shoe_string) + " "*2 + reverse)


def main():
    print('Welcome to the custom character creator tool!')
    height = int(input('Overall character height: '))
    hair = input('Character for the hair: ')
    eye = input('Character for the eyes: ')
    arm = input('Character for the arms: ')
    shoe = input('4-character string for the shoes: ')
    segment = int((height - 11) / 2)
    print()
    print_head(hair, eye)
    print_body(segment, arm)
    print_legs(segment, shoe)


main()
