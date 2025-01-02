import heapq

def merge_k_lists(lists):
    merged = heapq.merge(*lists)
    return list(merged)

# Приклад використання
lists = [[1, 55, 5], [1, 322, 42], [22, 26], [15, 222, 36]]

print("Об'єднані відсортовані списки:", merge_k_lists(lists))  