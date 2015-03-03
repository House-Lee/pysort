
def quick_sort(src , l, r):
    if l >= r:
        return src
    pidx = r - 1
    pivot = src[pidx]
    curidx = l
    for i in range( l , pidx):
        if src[i] < pivot:
            tmp = src[i]
            src[i] = src[curidx]
            src[curidx] = tmp
            curidx += 1
    tmp = src[curidx]
    src[curidx] = src[pidx]
    src[pidx] = tmp
    quick_sort(src, l, curidx - 1)
    quick_sort(src , curidx + 1 , r)
    return src

def bubble_sort(src):
    n = len(src)
    for i in range(0 , n):
        isSorted = True
        for j in range(0 , n - i):
            if (src[j] > src[j + 1]):
                isSorted = False
                tmp = src[j]
                src[j] = src[j + 1]
                src[j + 1] = tmp
        if isSorted:
            break
    return src
    
    
if (__name__ == "__main__"):
    src = [1,5,2,3,7,6,4]
    print quick_sort(src, 0, len(src))
    