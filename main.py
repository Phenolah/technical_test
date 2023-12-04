from collections import Counter

'''
PROBLEM STATEMENT

Give a list of integers, create a function that returns the nth-rarest item.
The function, should be called nth_most_rate signature and its signature
nth_most_rate signature(list,n) where list is the array of integers and n
is the nth rarest term. For example in ([5,4,5,4,5,4,4,5,3,3,3,2,2,1,5]),
if 2 is supplied as n, the answer is 2 as 2 is the 2nd rarest item.

'''

def nth_most_rate_signature(list, n):
    signature_counts = Counter(list)

    sorted_signatures = sorted(signature_counts.items(), key=lambda x: (x[1], x[0]))
    if 1 <= n <= len(sorted_signatures):
        return sorted_signatures[n - 1][0]
    else:
        return None

signatures = [2,2,2,2,2,5,5,5,5,5,5,5,7,8,8]
n = 2

result = nth_most_rate_signature(signatures, n)
print(f" The {n}nd rarest signature is: {result}")
