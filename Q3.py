import random
import threading
import time

def generate_random_numbers():
    return [random.randint(0, 10000) for _ in range(100)]


def multithreading_test(rounds=10):
    results = []

    for round_num in range(rounds):
        sets = [None] * 3
        threads = []

        def worker(index):
            sets[index] = generate_random_numbers()

        t1 = time.time_ns()

        for i in range(3):
            thread = threading.Thread(target=worker, args=(i,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        t2 = time.time_ns()
        T = t2 - t1
        results.append(T)
        print(f"Round {round_num + 1} - Multithreading Time: {T} ns")

    total = sum(results)
    average = total / rounds

    print("\nMultithreading Summary:")
    print(f"Total Time   : {total} ns")
    print(f"Average Time : {average} ns")
    return results, total, average

def non_multithreading_test(rounds=10):
    results = []

    for round_num in range(rounds):
        t1 = time.time_ns()

        for _ in range(3):
            _ = generate_random_numbers()

        t2 = time.time_ns()
        T = t2 - t1
        results.append(T)
        print(f"Round {round_num + 1} - Non-Multithreading Time: {T} ns")

    total = sum(results)
    average = total / rounds

    print("\nNon-Multithreading Summary:")
    print(f"Total Time   : {total} ns")
    print(f"Average Time : {average} ns")
    return results, total, average

def compare_results():
    print("=== Running Multithreading Test ===")
    multi_results, multi_total, multi_avg = multithreading_test()

    print("\n=== Running Non-Multithreading Test ===")
    non_multi_results, non_total, non_avg = non_multithreading_test()

    print("\n\n=== Round-by-Round Comparison ===")
    print(f"{'Round':<6} {'Multithread (ns)':<20} {'Non-Multithread (ns)':<25} {'Difference (ns)':<20}")
    for i in range(10):
        diff = non_multi_results[i] - multi_results[i]
        print(f"{i+1:<6} {multi_results[i]:<20} {non_multi_results[i]:<25} {diff:<20}")

    print("\n=== Summary ===")
    print(f"{'':<20} {'Multithreading':<20} {'Non-Multithreading':<25} {'Difference'}")
    print(f"{'Total Time (ns)':<20} {multi_total:<20} {non_total:<25} {non_total - multi_total}")
    print(f"{'Average Time (ns)':<20} {multi_avg:<20.1f} {non_avg:<25.1f} {non_avg - multi_avg:.1f}")

# Run the test
compare_results()

if __name__ == "__main__":
    compare_results()