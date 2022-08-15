try:
    tamanho = int(input(("Height: ")))
except:
    tamanho = int(input(("Height: ")))
while 8<tamanho or tamanho<1:
    tamanho = int(input(("Height: ")))

for i in (n+1 for n in range(tamanho)):
    print((" "*(tamanho-i)) + ("#"*i) + "  " + ("#"*i))