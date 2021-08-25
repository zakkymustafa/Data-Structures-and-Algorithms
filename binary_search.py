
# O(log n)

def binarySearch(alist,item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first+last)//2
        # print(alist[midpoint])
        if alist[midpoint] == item:
            return midpoint
        else:
            if item < alist[midpoint]:
                last=midpoint -1
            else:
                first=midpoint+1
    return last + 1




    
if __name__ == "__main__":
    print(binarySearch([0,3,5,7,9],4))
