
    
###############################################################################
# https://www.hackerrank.com/challenges/list-comprehensions/problem
def hr_listcomprehension(x,y,z,n):
    return [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n]


# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem 
def hr_second_max(mylist):
    temp = mylist.copy()
    first_max = max(temp)
    while max(temp) == first_max:
        temp.remove(first_max)
    return max(temp)


# https://www.hackerrank.com/challenges/nested-list/problem
def nested_lists_second_min(marksheet):
    # print([marks for name, marks in marksheet]) # [37.21, 37.21, 37.2, 41.0, 39.0]
    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
    # print('\n'.join([a[0] for a in sorted(marksheet) if a[1] == second_highest]))
     


# def rotate_list(input_list, rotations):
#     n = rotations % len(input_list) 
#     # print(n)    
#     word = input_list[::-1] # reversed
#     # print(input_list[n:] + word[len(input_list) - n:])
#     return input_list[n:] + word[len(input_list) - n:]
    
# def rotate_list_3(l, x):
#   return l[-x:] + l[:-x]



def rotate_list(input_list,rotations):
    import collections
    d = collections.deque(input_list)
    d.rotate(rotations)
    return list(d)



# https://www.hackerrank.com/  -  indices of max elements after n rotations
def max_element_after_rotation(a,rotate):
    '''  
    input_list without duplicates  
    return list of indices of max elements
    '''
    indices_result = []
    for n in rotate:
        # new_a = rotate_list(a,n) # n is the no.of rotations
        new_a = rotate_list(a,-n) # n is the no.of rotations
        # print(new_a)
        indices_result.append(new_a.index(max(new_a)))

    return indices_result 

# 
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem
#    https://www.youtube.com/watch?v=JrzIgYS3SqM&feature=youtu.be 
def minimumSwaps(arr):
    pass
    
    

if __name__ == "__main__":
    a = [1,2,4,3]  
    #reverse - 3421
    # 2431
    # 4312
    # 3124  -- result 
    #input[n:] 3
    # reverse[len(input_list) - n:]
    rotate = [0,1]
    print(max_element_after_rotation(a,rotate)) # # [2, 1]
    # arr = [7, 1, 3, 2, 4, 5, 6]

    # print(rotate_list(a,3))
    # print(rotate_list_2(a,3))
    # print(rotate_list_3(a,3))

        