while True:
    choose =  input("incode or decode? 0.encrypt 1.decrypt : ")
    
    if choose == "0":
        inp = input("N: ")
        enc = True
        break
    elif choose == "1":
        inp = input("C: ")
        enc = False
        break
    else:
        print("please type correctly.")

key = input("K: ").lower()
result = ""
while len(inp) != len(key):
    if len(inp)>len(key):
        key = key*2
    else:
        key = key[:-1]

converted = [ord(i)-97 for i in key]


while inp:
    if inp[0]==" ":
        result += " "
    else:
        o = ord(inp[0])
        if enc: 
            k = o + converted[0]
            if  o<91 and k>90 or o>96 and k > 122:
                k-=26
        else:
            k = o - converted[0]
            if  o<91 and k<65 or o > 96 and k < 96:
                k += 26
        result += chr(k)
    inp = inp[1:]
    converted = converted[1:]
print(result)