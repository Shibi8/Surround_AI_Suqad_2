# Framework-Documentation-Part-III
This document is dedicated to explain **Methods** used.

**Methods of Surround (*Python*)**

1. `Method` is called by its name, but is associated to an `object` (dependent).
2. A method is implicitly passed the object on which it is invoked.
3. It may or may not return any data.
4. A method can operate on the data (instance variables) that is contained by the corresponding class.

## Various methods of Python:

1. Python String methods
2. Python List methods
3. Python Dictionary methods
4. Python Tuple methods
5. Python Set methods
6. Python File methods

## The built-in Python methods:

Most of the Python methods are applicable only for a given value type.

Eg. `.upper()` works with strings, but doesn't work with integers, and `.append()` works with lists only and doesn't work with strings, integers or booleans.


**1. Methods for Python Strings**

Python has a set of built-in methods that you can use on strings.
The string methods are usually used during the data cleaning phase of the data project.

**Note:** All string methods returns new values. They do not change the original string.

Method | Description
------ | -----------
capitalize() | Converts the first character to upper case
casefold() | Converts string into lower case
center() | Returns a centered string
count() | Returns the number of times a specified value occurs in a string
encode() | Returns an encoded version of the string
endswith() | Returns true if the string ends with the specified value
expandtabs() | Sets the tab size of the string
find() | Searches the string for a specified value and returns the position of where it was found
format() | Formats specified values in a string
format_map() | Formats specified values in a string
index() | Searches the string for a specified value and returns the position of where it was found
isalnum() | Returns True if all characters in the string are alphanumeric
isalpha() | Returns True if all characters in the string are in the alphabet
isdecimal() | Returns True if all characters in the string are decimals
isdigit() | Returns True if all characters in the string are digits
isidentifier() | Returns True if the string is an identifier
islower() | Returns True if all characters in the string are lower case
isnumeric() | Returns True if all characters in the string are numeric
isprintable() | Returns True if all characters in the string are printable
isspace() | Returns True if all characters in the string are whitespaces
istitle() | Returns True if the string follows the rules of a title
isupper() | Returns True if all characters in the string are upper case
join() | Joins the elements of an iterable to the end of the string
ljust() | Returns a left justified version of the string
lower() | Converts a string into lower case
lstrip() | Returns a left trim version of the string
maketrans() | Returns a translation table to be used in translations
partition() | Returns a tuple where the string is parted into three parts
replace() | Returns a string where a specified value is replaced with a specified value
rfind() | Searches the string for a specified value and returns the last position of where it was found
rindex() | Searches the string for a specified value and returns the last position of where it was found
rjust() | Returns a right justified version of the string
rpartition() | Returns a tuple where the string is parted into three parts
rsplit() | Splits the string at the specified separator, and returns a list
rstrip() | Returns a right trim version of the string
split() | Splits the string at the specified separator, and returns a list
splitlines() | Splits the string at line breaks and returns a list
startswith() | Returns true if the string starts with the specified value
strip() | Returns a trimmed version of the string
swapcase() | Swaps cases, lower case becomes upper case and vice versa
title() | Converts the first character of each word to upper case
translate() | Returns a translated string
upper() | Converts a string into upper case
zfill() | Fills the string with a specified number of 0 values at the beginning

Some the examples are mentioned below:

   1. a.lower()
    This returns the lowercase version of the string.
    
    Example:
      Input: a = "Hello, World!"
             print(a.lower())
             
      Output: hello, world!

   
   2. a.upper()
    It does the opposite of lower()
    
    Example:
      Input: a = "Hello, World!"
             print(a.upper())
          
      Output: HELLO, WORLD!

  
  3. a.strip()
    If the string has whitespaces at the beginning or at the end, it removes them.
    
    Example: 
      Input: a = "Hello, World! "
             print(a.strip())
             
      Output: Hello, World!


   4. a.replace('old', 'new')
    This method replaces a given string with another string. However, it is case sensitive.
    
    Example:
      Input: a = "Hello, World!"
             print(a.replace("H", "J"))
             
      Output: Jello, World!
    
    
   5. a.split('delimeter')
    This splits your string into a list. Your argument specifies the delimeter.
    
    Example:
      Input: a = "Hello, World!"
             b = a.split(",")
             print(b)
             
      Output: ['Hello', 'World!']
      

**2. Methods for Python Lists**

Python has a set of built-in methods that you can use on lists/arrays.

**Note:** Python does not have built-in support for Arrays, but Python Lists can be used instead.

Method | Description
------ | -----------
append() | Adds an element at the end of the list
clear() | Removes all the elements from the list
copy() | Returns a copy of the list
count() | Returns the number of elements with the specified value
extend() | Add the elements of a list (or any iterable), to the end of the current list
index() | Returns the index of the first element with the specified value
insert() | Adds an element at the specified position
pop() | Removes the element at the specified position
remove() | Removes the first item with the specified value
reverse() | Reverses the order of the list
sort() | Sorts the list

Let's consider an example to demonstrate some the above mentioned methods:

    dog = ['name', age, birthyear, ['toy1', 'toy2']]
    
    dog = ['Fluffy', 6, 2015, ['bone', 'ball']]
    
   1. a.append(arg)
   We can modify this list by using a.append(arg)
    
   The `.append()` method adds an element to the end of the list. In this case, let's say we want to add the number of legs Fluffy has (which is 4).
   
    Example: 
       Input: dog = ['Fluffy', 6, 2015, ['bone', 'ball']]
              dog.append(4)
              print(dog)
   
       Output: ['Fluffy', 6, 2015, ['bone', 'ball'], 4]
       
   2. a.remove(arg)
   If we want to remove the birth year, we can do it using `.remove()` method.
   We have to specify the element that we want to remove, and Python will remove the first item with that value from the list.
   
    Example:
       Input: dog = ['Fluffy', 6, 2015, ['bone', 'ball']]
              dog.remove(2015)
              print(dog)
              
       Output: ['Fluffy', 6, ['bone', 'ball'], 4]
       
   3. a.count(arg)
   This returns the number of the specified value in the list.
   
    Example:
       Input: dog = ['Fluffy', 6, 2015, ['bone', 'ball'], 4]
              dog.count('Fluffy')
              print(dog)
       
       Output: 1
   
   4. a.clear()
   Removes all elements of the list. It will basically delete Fluffy. 
   
    Example: 
       Input: dog = ['Fluffy', 6, 2015, ['bone', 'ball'], 4]
              dog.clear()
              print(dog)
              
       Output: []
       
       
**3. Methods for Python Dictionaries**      

Python has a set of built-in methods that you can use on dictionaries.

Method | Description
------ | -----------
clear() | Removes all the elements from the dictionary
copy() | Returns a copy of the dictionary
fromkeys() | Returns a dictionary with the specified keys and values
get() | Returns the value of the specified key
items() | Returns a list containing a tuple for each key value pair
keys() | Returns a list containing the dictionary's keys
pop() | Removes the element with the specified key
popitem() | Removes the last inserted key-value pair
setdefault() | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update() | Updates the dictionary with the specified key-value pairs
values() | Returns a list of all the values in the dictionary

Some of the above methods are demonstrated below with examples:

  1. values()
  
         Input: thisdict =	{
                  "brand": "Ford",
                  "model": "Mustang",
                  "year": 1964
                }
                for x in thisdict.values():
                  print(x)
                  
         Output: Ford
                 Mustang
                 1964
                 
   2. keys()
            
          Input: thisdict = {
                   "brand": "Ford",
                   "model": "Mustang",
                   "year": 1964
                 }
                 if "model" in thisdict:
                   print("Yes, 'model' is one of the keys in the thisdict dictionary")
            
          Output: Yes, 'model' is one of the keys in the thisdict dictionary



**4. Methods for Python Tuples**

Python has two built-in methods that you can use on tuples.

Method | Description
------ | -----------
count() | Returns the number of times a specified value occurs in a tuple
index() | Searches the tuple for a specified value and returns the position of where it was found

Some of other methods' examples are given below:

 1. Using the `tuple()` constructor to create a tuple

        Example: 
           Input: thistuple = tuple(("apple", "banana", "cherry"))
                  print(thistuple)
              
           Output: ('apple', 'banana', 'cherry')
           
  2. access()
  
         Example:
            Input: thistuple = ("apple", "banana", "cherry")
                   print(thistuple[1])
                   
            Output: banana


**5. Methods for Python Sets**

Python has a set of built-in methods that you can use on sets.

Method | Description
------ | -----------
add() | Adds an element to the set
clear() | Removes all the elements from the set
copy() | Returns a copy of the set
difference() | Returns a set containing the difference between two or more sets
difference_update() | Removes the items in this set that are also included in another, specified set
discard() | Remove the specified item
intersection() | Returns a set, that is the intersection of two other sets
intersection_update() | Removes the items in this set that are not present in other, specified set(s)
isdisjoint() | Returns whether two sets have a intersection or not
issubset() | Returns whether another set contains this set or not
issuperset() | Returns whether this set contains another set or not
pop() | Removes an element from the set
remove() | Removes the specified element
symmetric_difference() | Returns a set with the symmetric differences of two sets
symmetric_difference_update() | inserts the symmetric differences from this set and another
union() | Return a set containing the union of sets
update() | Update the set with the union of this set and others

Some of the examples are demonstrated below:

  1. Using the `set()` constructor to create a set
  
         Input:  thisset = set(("apple", "banana", "cherry"))
                 print(thisset)
                 
         Output: {'cherry', 'banana', 'apple'}
         
      **Note:** The set list is unordered, so the result will display the items in a random order.
      
   2. Remove the last item in a set by using the pop() method
   
           Input: thisset = {"apple", "banana", "cherry"}
                  x = thisset.pop()
                  print(x) #removed item
                  print(thisset) #the set after removal
                  
           Output: banana
                   {'apple', 'cherry'}
                 

**6. Methods for Python Files**

Python has a set of methods available for the file object.

Method | Description
------ | -----------
close() | Closes the file
detach() | Returns the separated raw stream from the buffer
fileno() | Returns a number that represents the stream, from the operating system's perspective
flush() | Flushes the internal buffer
isatty() | Returns whether the file stream is interactive or not
read() | Returns the file content
readable() | Returns whether the file stream can be read or not
readline() | Returns one line from the file
readlines() | Returns a list of lines from the file
seek() | Change the file position
seekable() | Returns whether the file allows us to change the file position
tell() | Returns the current file position
truncate() | Resizes the file to a specified size
writeable() | Returns whether the file can be written to or not
write() | Writes the specified string to the file
writelines() | Writes a list of strings to the file

Examples of the above mentioned methods:

   1. read()
          
          Input: f = open("demofile.txt", "r")
                 print(f.read())
                 
          Output: Hello! Welcome to demofile.txt
                  This file is for testing purposes.
                  Good Luck!
                  
   2. readline()
   
          Input: f = open("demofile.txt", "r")
                 print(f.readline())
                 
          Output: Hello! Welcome to demofile.txt


 # Some of the methods' examples from Surround project:
 
 `1. stage.split(".") and ".".join()`
          
          if not isinstance(result, list):
                result = [result]
            for stage in filter(None, result):
                parts = stage.split(".")
                module = import_module("." + parts[-2], ".".join(parts[:-2]))
                klass = getattr(module, parts[-1])
                self.surround_stages.append(klass())
                
`2. .append()`
          
`3. datetime.now()`

The datetime.now is a class method that returns the current time. It uses the time.localtime without the timezone info (if not given, otherwise see timezone aware below). It has a representation (which would allow you to recreate an equivalent object) echoed on the shell, but when printed (or coerced to a str), it is in human readable (and nearly ISO) format, and the lexicographic sort is equivalent to the chronological sort
          
          def _execute_stage(self, stage, stage_data):
        stage_start = datetime.now()
        stage.operate(stage_data, self.config)

        if self.config["surround"]["enable_stage_output_dump"]:
            stage.dump_output(stage_data, self.config)

        # Calculate and log stage duration
        stage_execution_time = datetime.now() - stage_start
        stage_data.stage_metadata.append({type(stage).__name__: str(stage_execution_time)})
        LOGGER.info("Stage %s took %s secs", type(stage).__name__, stage_execution_time)
        
`4. dump_output()`

This method of the Stage class in surround by writing the outputs of two stages (WriteHello and WriteWorld) in their respective output files.

             import subprocess

             process = subprocess.Popen(['python3', 'examples/dump-output/dump_output.py', '-c=examples/dump-output/config.yaml'])
             process.wait()
             if not (process.returncode is None) and process.returncode > 0:
             raise Exception('Failed to run sample dump output app. Error code: ' + str(process.returncode))

- The surround object configuration is set in the FileSystemRunner class constructor, instantiated as adapter in dump_output.py.
- Through surround.process(), stages WriteHello and Write�World are executed, setting the text value of BasicData to "Hello" and "World" in each stage's operate() method.
- Since enable_stage_output_dump is set to True in config.yaml, surround automatically calls the dump_output() method of each stage after operate().
- A folder stages/<StageName> is created for each stage, each with an Output.txt file, containing the value of BasicData.text.
          
`5. __init__() and surround.process()`

This example takes a csv file as input, whose path is specified in the argument -f0 and extracts the word count of a client's complaint (column 'Consumer complaint narrative'). If specified in the config file (argument -c), the company's name (column 'Company') is extracted as well. The word count and (optionally) the company's name are saved in a file created in the folder specified in the -o (output folder) argument.

             import subprocess

             process = subprocess.Popen(['python3', 'examples/file-adapter/file_adapter.py', '-f0=examples/file-adapter/data/input.csv',                        '-c=examples/file-adapter/config.yaml', '-o', 'examples/file-adapter/data/'])
             process.wait()
             if not (process.returncode is None) and process.returncode > 0:
                raise Exception('Failed to run sample file adapter app. Error code: ' + str(process.returncode))


- The command line arguments are parsed and validated in the FileSystemRunner constructor (i.e., the __init__() method). The settings specified in the config file are assigned to the surround object.
- The transform() method of the same class pre-processes the input data. In this case, the method is implemented in the CustomFileSystemRunner class to read each row of the csv file, create an instance of BasicData, call the surround.process() method and save the output of all processed rows in output.txt.
- BasicData inherits from SurroundData and consists of three fields: row_dict (the row as read from the csv file), word_count and company.
- The surround.process() method calls the operate() method of the stage ProcessCSV, where the word_count and company values are extracted from the row_dict field, and set on their corresponding fields in the BasicData object.


`6. .init_stage() and operate()`

In this example, values are loaded to a data object in each stage and printed to screen.

- In each of the two stages defined (HelloSurround and HelloWorld), the constructor initialises a variable self.data.
- In the init_stage() method, the file with the text to be loaded is read by accessing the path set in config.yaml for the corresponding stage, the file contents are saved in the data variable.
- In each stage's operate() method, the contents of the stage's data are printed to screen.

import logging
from surround import Stage, SurroundData, Surround, Config

    class HelloSurround(Stage):

       def __init__(self):
             self.data = None

       def init_stage(self, config):
           file_ = open(config.get_path("surround.path_to_HelloSurround"), "r")
           self.data = file_.read()

       def operate(self, surround_data, config):
           print(self.data)

**Note:** Although a BasicData object is initialised, it is not modified throughout this example. Instead, internal data objects are used in each stage.


