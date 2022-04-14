from typing import List


def two_sum_hashed(arr: List, num: int):
    "An O(1) implementation using hashing"
    hashes = {}
    for elem in arr:
        diff = num - elem
        if hashes.get(diff):
            return [diff, elem]
        else:
            hashes[elem] = True
    return []
