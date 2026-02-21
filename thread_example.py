import threading
import time

def task(name):
    print(f"Start {name}")
    time.sleep(2)
    print(f"End {name}")

threads = []

start = time.time()

for i in range(3):
    t = threading.Thread(target=task, args=(f"Task {i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Total time: {time.time() - start:.2f} seconds")