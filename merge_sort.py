def merge_sort(arr):
    size = len(arr)
    if size > 1:
        left_arr = merge_sort(arr[:size // 2])
        right_arr = merge_sort(arr[size // 2:])
        index_l = 0
        index_r = 0
        while index_l + index_r != size:
            if index_l == len(left_arr):
                arr[index_l + index_r] = right_arr[index_r]
                index_r += 1
            elif index_r == len(right_arr):
                arr[index_l + index_r] = left_arr[index_l]
                index_l += 1
            elif left_arr[index_l] > right_arr[index_r]:
                arr[index_l + index_r] = right_arr[index_r]
                index_r += 1
            else:
                arr[index_l + index_r] = left_arr[index_l]
                index_l += 1
        return arr
    else:
        return arr