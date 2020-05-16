def encrypt(message,inkey):
    lmsg=[" "]+list(message)
    for i in str(inkey):
        i=int(i)
        lmsg[i]=lmsg[i]*i
    return "".join(lmsg)

def decrypt(encryptmsg,inkey):
    dict={}
    count=1
    encryptmsg=" "+encryptmsg
    for i in encryptmsg:
        if i not in dict.keys():
            dict[i]=count  
        else:
            dict[i]=dict[i]+1
    print(dict)
    


inmsg="Open"
inkey=123
outmsg="Oppeeen"
#assert encrypt(inmsg,inkey),outmsg
#print(encrypt(inmsg,inkey))
print(decrypt(outmsg,inkey))