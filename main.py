'''
PROBLEM STATEMENT

Give a list of integers, create a function that returns the nth-rarest item.
The function, should be called nth_most_rate signature and its signature
nth_most_rate signature(list,n) where list is the array of integers and n
is the nth rarest term. For example in ([5,4,5,4,5,4,4,5,3,3,3,2,2,1,5]),
if 2 is supplied as n, the answer is 2 as 2 is the 2nd rarest item.

'''



def nth_most_rare_signature(list, n):
    # count of each number in the list it gets stored in num_counts dictonary
    num_counts = {}
    for num in list:
        num_counts[num] = num_counts.get(num, 0) + 1

    # a list of numbers in num_counts in ascending order
    sorted_num = sorted(num_counts.keys(), key=lambda x: num_counts[x])

    # Return the nth rarest number
    if 1 <= n <= len(sorted_num):
        return sorted_num[n - 1]
    else:
        return None  


num_list = [2,2,2,2,2,5,5,5,5,5,5,10,10,10,5,7,8,8]
nth_rarest = 3
result = nth_most_rare_signature(num_list, nth_rarest)

print(f"The {nth_rarest} rarest signature is: {result}")
