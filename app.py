import base64

def b16decrypt(a):
    try:
        encryptedText = base64.b16decode(a).decode('utf-8')
        print(f"Decrypted text: {encryptedText}")
    except Exception as e:
        print(f"Error: {e}")
def b32decrypt(a):
    try:
        encryptedText = base64.b32decode(a).decode('utf-8')
        print(f"Decrypted text: {encryptedText}")
    except Exception as e:
        print(f"Error: {e}")
def b64decrypt(a):
    try:
        encryptedText = base64.b64decode(a).decode('utf-8')
        print(f"Decrypted text: {encryptedText}")
    except Exception as e:
        print(f"Error: {e}")
def b85decrypt(a):
    try:
        encryptedText = base64.a85decode(a, adobe=True).decode('utf-8', errors='ignore')
        print(f"Decrypted text: {encryptedText}")
    except Exception as e:
        print(f"Error: {e}")




print("""

            #####
        ######
     ########
   ########             *
  ########
 #########
 #########     *
#########
#########
#########                  *
 ########
  #########      *
   ########
    ########
      ########          *
         ######
             #####

""")
print("=================[Moon Decrypter]=================")
print("""
1. Base16
2. Base32
3. Base64
4. Ascii85
""")
userInput = input("What encrypted type?: ")


if userInput == "1":
    a = input("Type your crypted text: ")
    b16decrypt(a)
elif userInput == "2":
    a = input("Type your crypted text: ")
    b32decrypt(a) 
elif userInput == "3":
    a = input("Type your crypted text: ")
    b64decrypt(a) 
elif userInput == "4":
    a = input("Type your crypted text: ")
    b85decrypt(a)
else:
    print("Invalid format")


