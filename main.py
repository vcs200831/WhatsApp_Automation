import pywhatkit

print("\n")
print("Enter a number to message:")
number = input()

print("\n")
print("Enter a message:")
message = input()

pywhatkit.sendwhatmsg(number,message, 1, 00)
