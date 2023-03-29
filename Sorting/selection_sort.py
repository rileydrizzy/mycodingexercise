'''
Explain selection sort
'''
import random

def selection_sort(arr):
    


#TEST CASE AREA
sample = [[random.randint(1,30)for j in range(15)] for n in range(5)]
for n in sample:
    print (n)
    selection_sort(n)
    print(n)
