# Prtical 7
import threading

#shared variable
shared_variable = 0

#Define a semaphore (binary)
semaphore = threading.Semaphore(1)

#Incrementing value
def increment():
    global shared_variable
    for _ in range(100):
        semaphore.acquire() #Got access to critical section
        shared_variable += 1
        print("Incremented shared value: ",shared_variable)
        semaphore.release()
        
#Decrementing value
def decrement():
    global shared_variable
    for _ in range(100):
        semaphore.acquire() #Got access to critical section
        shared_variable -= 1
        print("Decremented shared value: ",shared_variable)
        semaphore.release()        

# Thread creation
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=decrement)

# Start Thread
thread1.start()
thread2.start()

# wait for thread to finish
thread1.join()
thread2.join()
