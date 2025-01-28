# Why Data Structures Matter

- Computer programs are all about receiving, manipulating and return data to a user.

- Data structures refer to how data is organized.

- Depending on how data is organized, a program may run faster or slower.

## The Array: Foundational Data Structure

- It is the most basic data structure in computer programming.
- Basically a list of data elements
- The index of an array is a number which identifies where a piece of data is located in an array.
- Most programming languages start counting indexes from 0.
- Most data structures have 4 basic ways in which they are used (operations):
    - Read: Finding something from a particular spot with the data structure. In arrays, basically looking up a value at a given index.
    - Search: Looking for a particular value within the data structure. Basically, looking to see if a value exists and if so, where.
    - Insert: Adding another value to the data structure. In arrays, basically adding another value in a given slot.
    - Delete: Removing a value from the data structure. In arrays, it implies removing a value from the array.

#### NB: When Measuring how "Fast" an operation takes, it refers to HOW MANY STEPS IT TAKES, rather than just pure Time.

We can never say with definitiveness that any operation takes, say, five seconds. While the same operation may take five seconds on a particular computer, it may take longer on an older piece of hardware, or much faster on the supercomputers of tomorrow. Measuring the speed of an operation in terms of time is flaky, since it will always change depending on the hardware that it is run on.

However, we can measure the speed of an operation in terms of how many steps it takes. If Operation A takes five steps, and Operation B takes 500 steps, we can assume that Operation A will always be faster than Operation B on all pieces of hardware. Measuring the number of steps is therefore the key to analyzing the speed of an operation.

### NB: Measuring the speed of an operation is known as the TIME COMPLEXITY of the operation.

## READING:
- Reading from an array occurs in just one step, due to the computer's ability to jump through indexes. This is what makes the array very powerful, due to its speed.
## SEARCHING:
- To search an array, the computer begins at index 0, checks value, and if not value, moves to the next index. Until the required value is found.
- Linear search refers to a search operation where the computer checks each cell at a time.
- In an array of N cells, a linear search will take a maximum of N steps. Clearly, searching far less efficient than reading.

## INSERTION:
- The efficiency of inserting data into an array, depends on the location within the array where the data will be inserted.
- Inserting data at the beginning or the middle of an array requires shifting pieces of data in order to make room for the insertion.