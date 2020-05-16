def rec_rev_str(var):
    if len(var)==1:
        return var
    return var[-1:] + (rec_rev_str(var[:-1]))
val="Techie Delight"
print(rec_rev_str(val))