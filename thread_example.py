import threading
import time

def download_file(file_id):
    print(f"Start downloading file {file_id}")
    time.sleep(2)
    print(f"Finished downloading file {file_id}")

threads = []

start_time = time.time()

for i in range(5):
    t = threading.Thread(target=download_file, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()
print(f"Total time: {end_time - start_time:.2f} seconds")