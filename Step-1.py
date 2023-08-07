  print(str(hair)*12)
    print(str(hair) + "|" + " "*8 + "|" + str(hair))
    print(str(hair) + "|" + " "*2 + str(eye) + " "*2 + str(eye) + " "*2 + "|" + str(hair))
    print(" " + "|" + " "*3 + "/" + "\\" + " "*3 + "|")
    print(" " + "|" + " "*8 + "|")
    print(" " + "\\" + " "*2 + "'--'" + " "*2 + "/")
    print(" "*3 + "-"*6 + " "*3)
    

hair = input('Character for the hair: ')
eye = input('Character for the eyes: ')

print_head(hair, eye)
