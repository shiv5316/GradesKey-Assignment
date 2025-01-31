import random

def generate_numbers(count):
  """Generates a list of random numbers.

  Args:
      count: The number of random numbers to generate.

  Returns:
      A list of random numbers.
  """
  return [random.randint(1, 1000) for _ in range(count)]
numbers = generate_numbers(100)
sorted_numbers = sorted(numbers)
def batch_sort(numbers, batch_size):
  """Sorts numbers in batches.

  Args:
      numbers: The list of numbers to sort.
      batch_size: The size of each batch.

  Returns:
      A sorted list of numbers.
  """
  sorted_batches = []
  for i in range(0, len(numbers), batch_size):
    batch = numbers[i:i + batch_size]
    sorted_batches.append(sorted(batch))
  return sorted_batches 

batch_size = 10
sorted_batches = batch_sort(numbers, batch_size)
import multiprocessing

def mapper( numbers):
    """Sorts a batch of numbers."""
    return sorted(numbers)

def reducer(sorted_batches):
    """Merges sorted batches into a single sorted list."""
    sorted_list = []
    for batch in sorted_batches:
        sorted_list.extend(batch)
    return sorted(sorted_list)

if __name__ == "__main__":
    numbers = generate_numbers(100)
    batch_size = 10
    batches = [numbers[i:i + batch_size] for i in range(0, len(numbers), batch_size)]
        with multiprocessing.Pool() as pool:
        sorted_batches = pool.map(mapper, batches)
        final_sorted_list = reducer(sorted_batches)
    
    print(final_sorted_list)
    