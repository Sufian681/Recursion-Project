def get_subset(items, mask):
    return [items[i] for i in range(len(items)) if (mask >> i) & 1]


def power_set(items):
    return [get_subset(items, m) for m in range(1 << len(items))]


def enumerate_subsets(items):
    n = len(items)
    for m in range(1 << n):
        print(f"Mask: {m:0{n}b} (Dec: {m:2d}) -> {get_subset(items, m)}")


if __name__ == "__main__":
    elements = ['A', 'B', 'C']

    print("Mask 5:", get_subset(elements, 5))
    print("Power Set Size:", len(power_set(elements)))

    print("\nEnumeration:")
    enumerate_subsets(elements)