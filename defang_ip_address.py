#https://leetcode.com/problems/defanging-an-ip-address/
def defangIPaddr(address,defang):
    address=list(address)
    for i in range(len(address)):
        if address[i]==".":
           address[i]="[.]"
    address="".join(address)     
    assert address==defang
address="127.0.0.1"
defang="127[.]0[.]0[.]1"
defangIPaddr(address,defang)