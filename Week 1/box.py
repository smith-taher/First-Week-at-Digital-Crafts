width = int(raw_input("Width? "))
height = int(raw_input("Height? "))
gap = " "

for i in range(height):
    if i == 0 or i == height - 1:
        print(width * '*')
    else: 
        print('*' + gap * (width - 2) + '*')   


