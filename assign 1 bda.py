## Return function
import random
def generate_random_numbers_return(n):
  """Generates a list of n random numbers.

  Args:
    n: The number of random numbers to generate.

  Returns:
    A list of n random numbers.
  """
  return [random.randint(1, 100) for _ in range(n)]
numbers = generate_random_numbers_return(100)
print(numbers)



##  Yield function
import random
def generate_random_numbers_yield(n):
  """Generates n random numbers one at a time.

  Args:
    n: The number of random numbers to generate.

  Yields:
    A random number.
  """
  for _ in range(n):
    yield random.randint(1, 100)
for number in generate_random_numbers_yield(100):
  print(number)