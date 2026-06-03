import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result= func(*args, **kwargs)
        end_time = time.time()
        print(f"éxicution time: {end_time - start_time:.4f}seconds")   
        return result
    return wrapper()
@timer
def count_numbers():
  for i in range (1, 1000001):
        pass
# count_numbers() 