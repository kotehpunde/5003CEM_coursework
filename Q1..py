import random

# Folding Hash Function
def fold_hash(ic_number, table_size):
    """Hash function using folding technique (3 parts of 4 digits)"""
    part1 = int(ic_number[0:4])
    part2 = int(ic_number[4:8])
    part3 = int(ic_number[8:12])
    hash_code = (part1 + part2 + part3) % table_size
    return hash_code

# Generate random 12-digit IC number
def generate_random_ic():
    return ''.join([str(random.randint(0, 9)) for _ in range(12)])

# Insert IC numbers into hash table with separate chaining and display contents
def insert_and_display(ic_numbers, table_size):
    hash_table = [[] for _ in range(table_size)]
    collisions = 0

    for ic in ic_numbers:
        index = fold_hash(ic, table_size)
        if hash_table[index]:
            collisions += 1
        hash_table[index].append(ic)

    print(f"\nHash Table with size {table_size}:")
    for i, bucket in enumerate(hash_table):
        if bucket:
            print(f"table[{i}] --> {' --> '.join(bucket)}")
        else:
            print(f"table[{i}]")

    return collisions

# Run simulation for 10 rounds
def run_simulation(rounds=10, num_ics=1000):
    table_sizes = [1009, 2003]
    total_collisions = {size: [] for size in table_sizes}

    for r in range(rounds):
        print(f"\n======== ROUND {r+1} ========")
        ic_list = [generate_random_ic() for _ in range(num_ics)]
        for size in table_sizes:
            collisions = insert_and_display(ic_list, size)
            total_collisions[size].append(collisions)
            print(f"Total collisions for table size {size}: {collisions}\n")

    print("\nAverage Collisions:")
    for size in table_sizes:
        avg = sum(total_collisions[size]) / rounds
        print(f"Table {size}: {avg:.1f} average collisions")

# Run the program
if __name__ == "__main__":
    run_simulation()

