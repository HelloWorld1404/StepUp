#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Doubling each element in a list using list comprehension
original_list = [1, 2, 3, 4, 5]
doubled_list = [x * 2 for x in original_list]


# In[3]:


print (doubled_list)


# In[4]:


# Map Function:
#map() applies a specified function to every item in an iterable (like a list) and 
#returns a new iterator that yields the results.
#Doubling each element in a list using map function
original_list = [1, 2, 3, 4, 5]
doubled_list = list(map(lambda x: x * 2, original_list))
print(doubled_list)


# In[5]:


#Filter Function:
#filter() constructs a new iterator from elements of an iterable for which a function returns true.
# Filtering even numbers from a list using filter function
original_list = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, original_list))
print(even_numbers)


# In[6]:


#Reduce Function (from functools in Python 3.x):

#reduce() applies a rolling computation to sequential pairs of values in a list and returns a single result.
from functools import reduce

# Adding all elements in a list using reduce function
original_list = [1, 2, 3, 4, 5]
sum_of_elements = reduce(lambda x, y: x + y, original_list)
print(sum_of_elements)


# In[ ]:




