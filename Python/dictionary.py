#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}


# In[2]:


print(my_dict["name"])  # Output: "Alice"


# In[3]:


my_dict["job"] = "Engineer"
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'job': 'Engineer'}


# In[4]:


#pop(key): Removes the key-value pair specified by the key.
my_dict.pop("age")
# Output: {'name': 'Alice', 'city': 'New York', 'job': 'Engineer'}


# In[5]:


#popitem(): Removes and returns an arbitrary key-value pair as a tuple.
removed_pair = my_dict.popitem()
# Output: ('job', 'Engineer')


# In[6]:


#del dict[key]: Removes a key-value pair from the dictionary.
del my_dict["city"]
# Output: {'name': 'Alice', 'job': 'Engineer'}


# In[7]:


#clear(): Removes all key-value pairs from the dictionary.
my_dict.clear()
# Output: {}


# In[8]:


#copy(): Creates a shallow copy of the dictionary.
new_dict = my_dict.copy()


# In[9]:


#update(dictionary): Updates the dictionary with key-value pairs from another dictionary or from an iterable of key-value pairs.
other_dict = {"gender": "Female", "age": 31}
my_dict.update(other_dict)
# Output: {'name': 'Alice', 'job': 'Engineer', 'gender': 'Female', 'age': 31}


# In[10]:


#keys(): Returns a view object that displays a list of all the keys in the dictionary.
keys = my_dict.keys()


# In[11]:


#values(): Returns a view object that displays a list of all the values in the dictionary.
values = my_dict.values()


# In[12]:


#items(): Returns a view object that displays a list of key-value tuples in the dictionary.
items = my_dict.items()


# In[13]:


# Creating an empty dictionary
empty_dict = {}

# Adding key-value pairs to the dictionary
empty_dict["name"] = "Alice"
empty_dict["age"] = 30
empty_dict["city"] = "New York"

# Printing the dictionary
print("Dictionary with key-value pairs:", empty_dict)


# In[14]:


# Initializing a dictionary with key-value pairs
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
print("Name:", my_dict["name"])  # Output: Name: Alice
print("Age:", my_dict["age"])    # Output: Age: 30


# In[15]:


# Initializing a dictionary using the dict() constructor
my_dict = dict(name="Bob", age=25, city="London")

# Accessing values
print("Name:", my_dict["name"])  # Output: Name: Bob
print("Age:", my_dict["age"])    # Output: Age: 25


# In[16]:


# Initializing a dictionary from a list of tuples
key_value_pairs = [("name", "Charlie"), ("age", 35), ("city", "Paris")]
my_dict = dict(key_value_pairs)

# Accessing values
print("Name:", my_dict["name"])  # Output: Name: Charlie
print("Age:", my_dict["age"])    # Output: Age: 35



# In[17]:


# Initializing a dictionary using dictionary comprehension
keys = ["name", "age", "city"]
values = ["David", 40, "Berlin"]
my_dict = {keys[i]: values[i] for i in range(len(keys))}

# Accessing values
print("Name:", my_dict["name"])  # Output: Name: David
print("Age:", my_dict["age"])    # Output: Age: 40


# In[18]:


# Initializing a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing dictionary items
print("Name:", my_dict["name"])  # Output: Name: Alice
print("Age:", my_dict.get("age"))  # Output: Age: 30

# Iterating through dictionary keys and values
print("Dictionary Items:")
for key, value in my_dict.items():
    print(key, ":", value)


# In[19]:


# Merging dictionaries
dict1 = {"name": "Alice", "age": 30}
dict2 = {"city": "New York", "job": "Engineer"}

merged_dict = dict1.copy()  # Creating a copy of the first dictionary
merged_dict.update(dict2)    # Updating the copy with the second dictionary

print("Merged Dictionary:", merged_dict)



# In[20]:


# Deleting items from the dictionary
del my_dict["age"]  # Deleting a specific key-value pair
print("Dictionary after deleting 'age':", my_dict)
# Output: Dictionary after deleting 'age': {'name': 'Alice', 'city': 'New York'}

my_dict.pop("city")  # Removing a key-value pair using the pop() method
print("Dictionary after popping 'city':", my_dict)
# Output: Dictionary after popping 'city': {'name': 'Alice'}

my_dict.clear()  # Clearing all items in the dictionary
print("Empty Dictionary:", my_dict)
# Output: Empty Dictionary: {}


# In[21]:


# Initializing a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Using keys() method to get keys
print("Keys:", my_dict.keys())  # Output: Keys: dict_keys(['name', 'age', 'city'])

# Using values() method to get values
print("Values:", my_dict.values())  # Output: Values: dict_values(['Alice', 30, 'New York'])

# Using items() method to get key-value pairs
print("Items:", my_dict.items())  # Output: Items: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])



# In[22]:


# Using copy() method to create a shallow copy of the dictionary
original_dict = {"a": 1, "b": 2}
copied_dict = original_dict.copy()

# Modifying the copied dictionary
copied_dict["c"] = 3

print("Original Dictionary:", original_dict)  
print("Copied Dictionary:", copied_dict)      


# In[23]:


# Using update() method to merge dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)

print("Merged Dictionary:", dict1)  


# In[27]:


# Using pop() method to remove a key-value pair
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
removed_value = my_dict.pop("age")

print("Dictionary after removing 'age':", my_dict)  
print("Removed Value:", removed_value)              


# In[25]:


# Dictionary comprehension to create a dictionary of squares
numbers = [1, 2, 3, 4, 5]
squared_dict = {num: num**2 for num in numbers}

print("Squared Dictionary:", squared_dict)  


# In[26]:


# Importing the datetime module
from datetime import datetime, date, time, timedelta

# Getting the current date and time
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

# Getting the current date
current_date = date.today()
print("Current Date:", current_date)

# Getting the current time
current_time = datetime.now().time()
print("Current Time:", current_time)

# Formatting Dates and Times
formatted_date = current_datetime.strftime("%Y-%m-%d")
formatted_time = current_datetime.strftime("%H:%M:%S")
print("Formatted Date:", formatted_date)
print("Formatted Time:", formatted_time)

# Parsing Dates and Times
date_string = "2023-10-18"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d").date()
print("Parsed Date:", parsed_date)

# Performing Date Arithmetic
future_date = current_date + timedelta(days=7)
print("Date 7 days from now:", future_date)

# Calculating the Difference Between Dates
date1 = date(2023, 10, 1)
date2 = date(2023, 10, 18)
date_difference = date2 - date1
print("Number of days between two dates:", date_difference.days)


# In[ ]:




