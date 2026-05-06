text = "hello"
encr = ""
for ch in text:
    encr += chr(ord(ch)+ 3)
print(encr)
