def dedupe(items):
    """
    从一个序列中移除重复的元素，并保持原有元素的顺序不变 (适用于可哈希元素)。

    :param items: 一个包含可哈希元素的序列 (e.g., list, tuple).
    :yield: 去重后序列中的元素。
    """
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def dedupe_unhashable(items, key=None):
    """
    从一个序列中移除重复的元素，并保持原有元素的顺序不变 (适用于不可哈希元素)。

    :param items: 一个包含不可哈希元素的序列 (e.g., list of dicts).
    :param key: 一个函数，用于将序列中的元素转换为可哈希类型。如果为None，则直接对元素进行操作。
    :yield: 去重后序列中的元素。
    """
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

# ====================================================================
# 1. 对可哈希序列去重
# ====================================================================
print("--- 1. Deduplicating a Sequence of Hashable Items ---")
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(f"Original list: {a}")
deduplicated_list = list(dedupe(a))
print(f"Deduplicated list: {deduplicated_list}")

# ====================================================================
# 2. 对不可哈希序列去重 (例如：字典列表)
# ====================================================================
print("\n--- 2. Deduplicating a Sequence of Unhashable Items (e.g., dicts) ---")
b = [
    {'x': 1, 'y': 2},
    {'x': 1, 'y': 3},
    {'x': 1, 'y': 2},
    {'x': 2, 'y': 4}
]
print(f"Original list of dicts: {b}")
# 根据字典中的'x'和'y'键的值进行去重
deduplicated_list_of_dicts = list(dedupe_unhashable(b, key=lambda d: (d['x'], d['y'])))
print(f"Deduplicated based on ('x', 'y'): {deduplicated_list_of_dicts}")

# 只根据字典中'x'键的值进行去重
deduplicated_list_of_dicts_x = list(dedupe_unhashable(b, key=lambda d: d['x']))
print(f"Deduplicated based on 'x' only: {deduplicated_list_of_dicts_x}")

# ====================================================================
# 3. 使用set进行简单去重 (不保留顺序)
# ====================================================================
print("\n--- 3. Simple Deduplication Using a Set (Order is Not Preserved) ---")
print(f"Original list: {a}")
set_deduplicated = set(a)
print(f"Deduplicated with set: {set_deduplicated}")