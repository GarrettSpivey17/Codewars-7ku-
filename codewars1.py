# 1 Band name generator
#https://www.codewars.com/kata/59727ff285281a44e3000011/train/python

def band_name_generator(name: str) -> str:
      name = name.lower()
      if name[0] == name[-1]:
          return name.title() + name[1:]
      else:
        return "The " + name.title()
#the second line makes sure that any input will become lowercase, next i used an if else
#statement, so if the name has the same first and last letter it adds the name with the name minus the first letter while also capitalizing the first letter.  
#If the name does not include the same first and last letter the else statment returns the name with "the" before the name and still capitalizes it. 

# 2 Sum of two lowest positive integers
# https://www.codewars.com/kata/558fc85d8fd1938afb000014/solutions/python
def sum_two_smallest_numbers(numbers):
    numbers_sorted = sorted(numbers)
    return numbers_sorted[0] + numbers_sorted[1]
print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))  

# line one defines the function then line two sorts the numbers smallest to largest 
# Then line three adds the first and second number of the sorted list

# 3 Easy Time Convert
# https://www.codewars.com/kata/5a084a098ba9146690000969/solutions/python

def convert_minutes(total_minutes: int) -> str:
    if total_minutes <= 0:
        return "00:00"
    
    hours = total_minutes // 60           
    minutes = total_minutes % 60          
    return f"{hours:02d}:{minutes:02d}" 

#the code defines the function and the second line checks if the number is positive or negative
#the next to lines devid the input into minutes.
#the return line turns the output into a HH:mm format

# 4 Highest and Lowest
# https://www.codewars.com/kata/554b4ac871d6813a03000035/solutions/python

def high_and_low(numbers: str) -> str:
    nums = list(map(int, numbers.split()))
    return f"{max(nums)} {min(nums)}"

# the function is defined then the second line converts the strings into substrings and intp integers
#then returns the min and max of the inputs


# 5 Descending Order
# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/solutions/python

def descending_order(num: int) -> int:
    return int("".join(sorted(str(num), reverse=True)))

# uses sorted to rearrange the digits then reverses the order in decending order