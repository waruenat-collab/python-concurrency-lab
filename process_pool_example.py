from concurrent.futures import ProcessPoolExecutor

def work(x):
    return x * x

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = executor.map(work, range(5))
        print(list(results))