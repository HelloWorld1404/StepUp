#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Creating tuples
tuple1 = (1, 2, 3)
tuple2 = ("apple", "banana", "cherry")
tuple3 = (1, "hello", 3.14)


# In[2]:


print(tuple1[0])  # Output: 1
print(tuple2[1])  # Output: "banana"


# In[3]:


concatenated_tuple = tuple1 + tuple2
# Output: (1, 2, 3, "apple", "banana", "cherry")


# In[4]:


repeated_tuple = tuple1 * 3
# Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)



# In[5]:


print(len(tuple1))  # Output: 3


# In[6]:


print(2 in tuple1)  # Output: True
print("orange" in tuple2)  # Output: False


# In[7]:


tuple1 = (1, 2, 2, 3, 4, 2)
count = tuple1.count(2)
print(count)  # Output: 3


# In[8]:


tuple1 = (1, 2, 3, 4, 5)
index = tuple1.index(3)
print(index)  # Output: 2


# In[9]:


# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements of a tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])


# In[10]:


# Slicing a tuple
my_tuple = (1, 2, 3, 4, 5)
sliced_tuple = my_tuple[1:4]
print("Sliced tuple:", sliced_tuple)  # Output: (2, 3, 4)


# In[11]:


# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)


# In[12]:


# Repeating tuples
my_tuple = (1, 2)
repeated_tuple = my_tuple * 3
print("Repeated tuple:", repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)


# In[13]:


# Finding the length of a tuple
my_tuple = (1, 2, 3, 4, 5)
length = len(my_tuple)
print("Length of the tuple:", length)  # Output: 5


# In[14]:


# Counting occurrences of an element in a tuple
my_tuple = (1, 2, 2, 3, 4, 2)
count = my_tuple.count(2)
print("Count of 2 in the tuple:", count)  # Output: 3


# In[15]:


# Finding the index of an element in a tuple
my_tuple = (1, 2, 3, 4, 5)
index = my_tuple.index(3)
print("Index of 3 in the tuple:", index)  # Output: 2


# In[16]:


# Tuple unpacking
coordinates = (3, 4)
x, y = coordinates
print("x:", x)  # Output: 3
print("y:", y)  # Output: 4


# In[17]:


# Checking if an element is in a tuple
my_tuple = (1, 2, 3, 4, 5)
print(3 in my_tuple)  # Output: True
print(6 in my_tuple)  # Output: False


# In[ ]:




