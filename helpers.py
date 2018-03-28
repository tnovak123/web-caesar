def alphabet_position(letter):
    lower_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
    location = 0
    if letter.isupper() == True:
        letter = letter.lower()
        location = lower_list.index(letter)
    else:
        location = lower_list.index(letter)
    
    return(location)

def rotate_character(char, rot):
    lower_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
    startlocation = 0
    newlocation = 0
    if char.isalpha() == True:
        startlocation = alphabet_position(char)
        newlocation = (startlocation + int(rot)) % 26
        newchar = lower_list[newlocation]
    else:
        print("That character is not a letter.")

    if char.isupper() == True:
        newchar = newchar.upper()
    
    return(newchar)

def main():
    inputcharacter = input("Enter a letter.")
    inputletterdisplacement = input("Enter a displacement value.")
    print(rotate_character(inputcharacter, inputletterdisplacement))

if __name__ == "__main__":
    main()