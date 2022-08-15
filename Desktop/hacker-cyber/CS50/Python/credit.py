numerosPares = 0
numerosImpares = 0
tmp =0
number = input("number: ")

def sum(arg):
    sum = 0
    for digit in str(arg):
        sum += int(digit)
    return sum

for i in reversed(range(0,len(number))):
    if (tmp%2 !=0):
        mult = int(number[i])*2
        if(mult/10 >=1):
            numerosImpares += sum(mult)
        else:
            numerosImpares += int(number[i])*2
    else:
        numerosPares += int(number[i])
    tmp +=1
somaFinal = str(numerosPares+numerosImpares)
if((number[0]=='4') and (somaFinal[-1]) == '0'):
    print("VISA")
elif(((number[:2]=='36') or (number[:2]=='37')) and ((somaFinal[-1]) == '0')):
    print("AMEX")
elif(((number[:2]=='51') or (number[:2]=='52')or (number[:2]=='53')or (number[:2]=='54')or (number[:2]=='55')) and ((somaFinal[-1]) == '0')):
    print("MASTERCARD")
else:
    print("INVALID")

