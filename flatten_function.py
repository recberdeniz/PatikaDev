# reverse function
def reverse(r):
    r = r[::-1] # outer list reversing
    reversed_list = [r[i][::-1] for i in range(len(r))] # inner list reversing with list comprehension method
    return reversed_list # return reversed_list

# flatten function
def flatten(l):
    for i in l:
        if isinstance(i, list): # if list index is string, flattened
            flatten(i)
        else: # else append on to output list
            output_list.append(i)

input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5] # input list for flatten
before_reverse = [[1, 2], [3, 4], [5, 6, 7]] # input list for reverse
output_list = list()
flatten(input_list)
print(output_list)
print(reverse(before_reverse))
