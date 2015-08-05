counter = 0

def swap(a,x,y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp

def QuickSort(a):
    '''
    Unstable, Worst Case n^2, average/best case nlogn
    '''
    if len(a) <= 1:
        return a

    p = a.pop(len(a) / 2)
    # p = input_list.pop(0)
    less = [i for i in a if i < p]
    greater = [i for i in a if i >= p]

    return QuickSort(less) + [p] + QuickSort(greater)


def Partition(a, lo, hi, p):
    cur = lo
    for i in range(lo,hi):
        if a[i] <= p:
            swap(a, cur, i)
            cur += 1
    swap(a, cur, hi)
    return cur


def QuickSortInPlace(a, lo, hi):
    '''
        Can be stable
        watch out the list slicing is not inclusive
        Need lo, hi indices to reference element in place
    '''

    if len(a[lo:hi+1]) <= 1:
        return

    p = a[hi]
    cur = Partition(a, lo, hi, p)

    if cur > lo:
        QuickSortInPlace(a, lo, cur-1)
    if cur < hi:
        QuickSortInPlace(a, cur+1, hi)


def Merge(l, r):
    mergedList = []

    while l or r :
        if l and r:
            if l[0] < r[0]:
                mergedList.append(l.pop(0))
            else:
                mergedList.append(r.pop(0))
        elif l:
            mergedList.extend(l)
            break
        else:
            mergedList.extend(r)
            break
    return mergedList

def MergeSort(a):
    '''
    Merge should compare each element in the sublist
    pop items from list if it's not needed
    '''
    if len(a) <= 1:
        return a

    middle = len(a) / 2

    left = MergeSort(a[:middle])
    right = MergeSort(a[middle:])

    return Merge(left, right)

def InsertionSort(a):
    '''
    Best case O(n) if list is already sorted, in place - O(1) storage, stable, Online
    The inner loop walks from the current position backward
    '''
    if len(a) < 2:
        return a

    for i, n in enumerate(a):
        cur = i
        while n < a[cur - 1] and cur > 0 :
            swap(a, cur, cur - 1)
            cur -= 1
    return a

def SelectionSort(a):
    '''
    Not stable, always O(n^2)
    '''
    min = 0
    for i in xrange(0, len(a)-1):
        min = i
        for j in xrange(i+1, len(a)):
            if a[j] < a[min]:
                min = j

        if i != min:
            swap(a, i, min)
    return a


def pp(dictMsg):
    pass

def main():
    import copy
    input_list = [1, 2, 3, 3, 4, 5]
    input_list = [2, 1, 4, 3, 5, 3]
    # input_list = [2, 1]

    print "QuickSort"
    print QuickSort(copy.copy(input_list))
    # QuickSortInPlace(input_list, 0, len(input_list)-1)
    # print input_list

    print "MergeSort"
    print MergeSort(input_list)

    print "InsertionSort"
    print InsertionSort(input_list)

    # print "SelectionSort"
    # print SelectionSort(input_list)
if __name__ == '__main__':
    main()