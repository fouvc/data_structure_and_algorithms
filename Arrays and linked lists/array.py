import random
def random_access(nums):
    """random access elements"""
    # A number is randomly draw in the interval [0,len(nums)-1]
    random_index=random.randint(0,len(nums)-1)
    # Gets and returns random element
    random_num=nums[random_index]
    return random_num

# Please note,Python's lists is a dynamic array that can be extended directly
# For easy of learning,the function treats lists as an array of an immutable length
def extend(nums,enlarge):
    """Initialize an extended length array"""
    res=[0]*(len(nums)+enlarge)
    # Copy all elements from original arrays to a new arrays
    for i in range(len(nums)):
        res[i]=nums[i]
    # Return the new extended arrays
    return res

def insert(nums,num,index):
    """Insert the element at the index index of the array"""
    # Move the index index and all subsequent elements back a bit
    for i in range(len(nums)-1,index,-1):
        nums[i]=nums[i-1]
    # Assign a num to the index element
    nums[index]=num

def remove(nums,index):
    """Delete the element at the index"""
    # Move all elements after index forward one bit
    for i in range(index,len(nums)-1):
        nums[i]=nums[i+1]

def traverse(nums):
    """Traverse the array"""
    count=0
    # Traverse the array by index
    for i in range(len(nums)):
        count+=1
    # Traverse the array directly
    for num in nums:
        count+=1
    # Traverse data index and elements at the same time
    for i,num in enumerate(nums):
        count+=1

def find(nums,target):
    """Finds the specified element in the array"""
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1


"""Driver code"""
if __name__=='__main__':
    # Initialize the array
    arr=[0]*5
    print('arr = ',arr)
    nums=[1,3,2,5,4]
    print('nums = ',nums)

    # Random access
    random_num=random_access(nums)
    print('Get random element in nums : ',random_num)

    # Extended length
    nums=extend(nums,3)
    print('Extended array to 8: ',nums)

    # Insert element
    insert(nums,6,3)
    print('Insert the number 3 at the index 6 to get nums : ',nums)

    # Remove element
    remove(nums,2)
    print('Remove the element at the index 2 to get nums : ',nums)

    # Traverse array
    traverse(nums)

    # Find element
    index=find(nums,3)
    print('Find number 3 in array to get index = ',index)

"""
Advantages of arrays:
Accessing elements is very efficient: elementAddr = firtstElementAddr + elementLength * elementIndex
An index essentially represents an offset from a memory address

Disadvantages of arrays:
The length is immutable after initialization
Inserting or deleting elements is inefficient
"""