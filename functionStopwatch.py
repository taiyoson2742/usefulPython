#written 11.3.26
#this function takes another function and calculates how much time it takes for it to run
import time

def timer(func):
    def wrapper(*args, **kwargs):
        # Record start time
        time_start = time.time()
        # Call the original function
        result = func(*args, **kwargs)
        # Record end time
        time_end = time.time()
        # Calculate elapsed time
        elapsed_time = time_end - time_start
        # Print the time
        print(f"Elapsed time: {elapsed_time} seconds")
        # Return the original result
        return result
    return wrapper

@timer
def f(n):
    time.sleep(n)
f(1)
