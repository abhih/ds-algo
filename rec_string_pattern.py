#https://www.techiedelight.com/find-binary-strings-can-formed-given-wildcard-pattern/

pattern= "1?1?1?"#11?00?1?"

def rec_comb_binary(arg,i=0):
    if i==len(arg):
        print(arg)
        return
    list_args=list(arg)
    if list_args[i]=="?":
        list_args[i]="0"
        arg="".join(list_args)
        rec_comb_binary(arg,i+1)
        list_args[i]="1"
        arg="".join(list_args)
        rec_comb_binary(arg,i+1)
    else:
        arg="".join(list_args)
        rec_comb_binary(arg,i+1)

print(rec_comb_binary(pattern))