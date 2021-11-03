index_sum = 0
def mod_identfy(original:str, mod:str):
    if original == mod:
        return False
    else:
        for i in original:
            if i in mod:
                i = 0
            else:
                i = 1
                index_sum += i
    return index_sum < 2

