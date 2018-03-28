from helpers import rotate_character, alphabet_position

def encrypt(text, rot):
    newtext = ""
    for char in text:
	    if char.isalpha() == True:
	        newtext += rotate_character(char, rot)
	    else:
	        newtext += char
	
    return(newtext)

def main():
    inputtext = ""
    displace = 0
    inputtext = input("What do you want to encrypt?")
    displace = input("What encryption value do you want to use?")
    if displace.isdigit() == True:
        print(encrypt(inputtext, displace))
    else:
        pass

if __name__ == "__main__":
    main()