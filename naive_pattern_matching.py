#https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/

def search(patt,text):
    ll=[]
    len_pat=len(patt)
    for i in range(0,len(text)):
        if patt==(text[i:i+len_pat]):
            ll.append(i)
    return ll

if __name__ == '__main__': 
    txt = "ABABABCABABABCABABABC"
    pat = "ABABAC"
    print(search(pat, txt))