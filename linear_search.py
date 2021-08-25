
def sequentialSearch(alist,item):
    pos=0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos=pos+1
    return found

    

if __name__ == "__main__":
    print(sequentialSearch([3,4,6,7,9],3))
