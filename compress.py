text = "abacccaaab"
compresses = ""
c = 1
for i in range(len(text)-1):
    if text[i] == text[i+1]:
        c += 1
    else:
        compresses += text[i] + str(c)
        c += 1
compresses += text[-1] + str(c)
print(compresses)
