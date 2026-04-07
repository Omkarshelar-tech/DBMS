# Pratical 6
import threading

#shared variable
shared_variable = 100

#Mutex lock
lock = threading.Lock()

#Function for incrementing shared_variable
def increment():
    global shared_variable
    with lock:
        old_value = shared_variable
        print("Old value: ",old_value)
        shared_variable = old_value + 1
        print(f"Thread 1: Incremented value to {shared_variable}")
        
# Decrement the shared value
def decrement():
    global shared_variable
    with lock:
        old_value = shared_variable
        shared_variable = old_value - 1
        print(f"Thread 2: Decrement value to {shared_variable}")
        
# Thread creation
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=decrement)

# Start Thread
thread1.start()
thread2.start()

# wait for thread to finish
thread1.join()
thread2.join()

# Printing final value of shared_variable
print("Final value: ",shared_variable)         
            