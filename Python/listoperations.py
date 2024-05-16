#!/usr/bin/env python
# coding: utf-8

# In[7]:


'''
Problem Statement 1: List Manipulation

Problem Description:

You are given a list of integers, and your task is to create a 
Python function called modify_list that takes this list as input and performs the following operations:

Remove all even numbers from the list.
Square each remaining number in the list.

'''

l1=[1,4,3,7,5,3]
l2=[]
for i in l1:
    if i%2!=0:
        i=i**2
        l2.append(i)
print(l2)


# In[8]:


# opeations on list

list1=[1,2,3,4,5,6,7]
list2= [10,20,30,40,50]

list1.append(8)                                  #append() operation
print(list1)

#extend() operation

list1.extend(list2)
print(list1)

#insert() operation : When we have to insert at some particular position
list1.insert(2,"hello")
print(list1)



# index() operation: when we have to fetch some value of some particular index
print(list1.index(2))


#count() operation: when we have to count the repeted entry in list, i.e. we have to check how many times 1 is encountring in the list
print(list1.count(2))

#sort(): this is used to sort the list
list2.sort()
print(list2)

#reverse(): if we have to reverese the list
list2.reverse()
print(list2)


#we can also reverse the list without using reverse() operation. write list2.sort(reverse=True): this will also reverse the list

#pop(): It is used to pop the last value of list

print(list2.pop())


# In[9]:


print(list2)


# In[15]:


'''
You are given two lists of integers, and your task is to create a Python function called 
find_common_elements that takes these two lists as input and returns a new list containing the common 
elements present in both input lists.

'''
def find_common_elements(list1, list2):
    common_elements = []
    
    for item in list1:
        if item in list2 and item not in common_elements:
            common_elements.append(item)
    
    return common_elements

# Example usage:
list3 = [1, 2, 3, 4, 5]
list4 = [3, 4, 5, 6, 7]
result = find_common_elements(list3, list4)
print("Common elements:", result)




# In[29]:


''' You are given a list of integers and an integer k. Your task is to create a Python function called rotate_list 
that takes this list and k as input and rotates the 
list to the right by k positions.'''


def rotate(a,b):
    if not a:
        return
    else:
        a[:]= a[-b:] + a[:-b]
        return a
a=[1,2,3,4,5]
print(rotate(a,3))


# In[12]:


'''  Problem Statement 1: Finding Missing Numbers

Problem Description:

You are given two lists of integers. One list contains all the numbers from 1 to N, and the other 
list is missing a few numbers. Your task is to create a Python function called 
find_missing_numbers that takes these two lists as input and returns a list of missing numbers.'''
l1=[1,2,3,4,5,6,7,8,9,10]
l2=[1,3,5,7,9]
def missing(l1,l2):
    l3=[]
    for i in l1:
        if i in l1 and i not in l2:
            l3.append(i)
    return l3
print(missing(l1,l2))


# In[13]:


'''

List Partitioning

Problem Description:

You are given a list of integers and a pivot element. Your task is to create a Python 
function called partition_list that takes this list and the pivot as input and partitions the list into 
two sublists: one containing elements less 
than the pivot and the other containing elements greater than or equal to the pivot.'''


def partition(a,b):
        x= a[0:3]
        y= a[3:5]
        return x, y
      
a=[1,2,3,4,5]
print(partition(a,2))


# In[17]:


def partition_list(input_list, pivot):
    # Initialize two empty lists for elements less than pivot and greater than or equal to pivot
    less_than_pivot = []
    greater_than_equal_to_pivot = []

    # Iterate through the input_list and categorize elements based on the pivot
    for element in input_list:
        if element < pivot:
            less_than_pivot.append(element)
        else:
            greater_than_equal_to_pivot.append(element)

    return less_than_pivot, greater_than_equal_to_pivot

# Example usage:
input_list = [4, 7, 2, 9, 1, 5, 8]
pivot = 5
result = partition_list(input_list, pivot)
print("Elements less than pivot:", result[0])
print("Elements greater than or equal to pivot:", result[1])


# In[26]:


#slicing
list1=[1,2,3,4,'hello',6]
list1[2:5]


# In[19]:


list1[-1]


# In[27]:


list1[-2:]


# In[23]:


list1[:-2]


# In[28]:


list1[:-3]


# In[ ]:


list1.insert(2,'hi')
print(list1)

