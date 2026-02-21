from concurrent.futures import ProcessPoolExecutor
import time

def heavy_task(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

if __name__ == "__main__":
    start = time.time()

    with ProcessPoolExecutor() as executor:
        executor.map(heavy_task, [10_000_000] * 3)

    print(f"Total time: {time.time() - start:.2f} seconds")