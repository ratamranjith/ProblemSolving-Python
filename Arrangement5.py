'''Given an array of size n, write a function to rearrange the numbers of the array in such a way that even and odd numbers are arranged alternatively in increasing order.
Input Format
Array size i.e. n

Constraints
5<=n<=10^8

Output Format
Array elements (separated by comma)

Sample Input 0
5
9,12,23,8,5

Sample Output 0
5,8,9,12,23

Explanation 0
As the numbers are to be arranged in increasing order hence we start with 5 in the given array, also the starting number is odd therefore the next number has to be even and has to be smallest in even number i.e. 8....and so on. Hence the output is (5,8,9,12,23)

Sample Input 1
5
47,49,36,98,90

Sample Output 1
36,47,90,49,98

Explanation 1
In the given array, 36 is the smallest number hence we start with it and arrange the series as even-odd alternatively'''

from itertools import chain, zip_longest
even = []
odd  = []
n = int(input().strip())
val = ""
ele = input().split(',')
ele = [eval(i) for i in ele]
for i in sorted(ele):
    if(i % 2 == 0):
       even.append(i)
    else:
       odd.append(i)
even = sorted(even)
odd = sorted(odd)
if(even[0] > odd[0]):
   val = chain.from_iterable(zip_longest(odd,even))
else:
   val = chain.from_iterable(zip_longest(even,odd))
val = [str(i) for i in val if i is not None]
print(",".join(val))
