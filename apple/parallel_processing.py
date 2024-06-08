import multiprocessing
import concurrent.futures

# def worker(num):
#     print(f"Worker {num} is working")

# if __name__ == "__main__":
#     jobs = []
#     for i in range(5):
#         p = multiprocessing.Process(target=worker, args=(i,))
#         jobs.append(p)
#         p.start()

def worker(num):
    print(f"Worker {num} is working")

if __name__ == "__main__":
    with multiprocessing.Pool(5) as pool:
        pool.map(worker, range(5))

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(worker, range(5))        
