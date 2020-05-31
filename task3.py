



def partition(arr, start, end):

    if arr[start] > arr[end]:
        arr[start], arr[end] = arr[end],arr[start]

    lp_pos = start + 1
    rp_pos = end - 1
    k = start + 1
    lp = arr[start]
    rp = arr[end]

    while k <= rp_pos:
        if arr[k] < lp:
            arr[k], arr[lp_pos] = arr[lp_pos], arr[k]
            lp_pos += 1
        elif arr[k] >= rp:
            while arr[rp_pos] > rp and k < rp_pos:
                rp_pos -= 1
            arr[k], arr[rp_pos] = arr[rp_pos], arr[k]
            rp_pos -= 1
            if arr[k] < lp:
                arr[k], arr[lp_pos] = arr[lp_pos], arr[k]
                lp_pos += 1
        k += 1
    lp_pos -= 1
    rp_pos += 1

    arr[start], arr[lp_pos] = arr[lp_pos], arr[start]
    arr[end], arr[rp_pos] = arr[rp_pos], arr[end]

    return lp_pos, rp_pos


def qsort(arr, start, end):
    if start < end:
        lp, rp = partition(arr, start, end)
        qsort(arr, start, lp - 1)
        qsort(arr, lp+1, rp - 1)
        qsort(arr, rp+1, end)


def main():
    arr = [4, 3, 7, 65, 23, 100, 1, 8, 2]
    qsort(arr, 0, len(arr)-1)
   
    for x in arr:
        print(x)


main()



