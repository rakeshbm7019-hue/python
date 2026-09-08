import multiprocessing as mp
import random
import time


def worker(task):
    task_id, value = task
    time.sleep(1)  # simulate heavy work
    return (task_id, value ** 2)

def producer(queue, n=10):
    for i in range(n):
        val = random.randint(1, 100)
        print(f"Produced {val}")
        queue.put((i, val))
    queue.put(None)  # sentinel to signal end

def consumer(queue, pool):
    results = []
    tasks = []
    while True:
        task = queue.get()
        if task is None:
            break
        tasks.append(pool.apply_async(worker, (task,)))
    for t in tasks:
        results.append(t.get())
    return results

def main():
    queue = mp.Queue()
    pool = mp.Pool(processes=4)

    p = mp.Process(target=producer, args=(queue, 12))
    p.start()

    
    results = consumer(queue, pool)
    print("Final Results:", results)

    p.join()
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
