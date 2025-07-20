prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# ====================================================================
# 1. 对字典的值进行计算 (min, max, sorted)
# ====================================================================
print("--- 1. Calculations on Dictionary Values ---")

# 为了在字典的值上执行计算，通常需要使用 zip() 将键和值反转或配对。
# zip() 会创建一个迭代器，其中的每个元素都是一个 (值, 键) 的元组。

# 使用 zip() 创建 (值, 键) 对的迭代器
min_price_pair = min(zip(prices.values(), prices.keys()))
max_price_pair = max(zip(prices.values(), prices.keys()))
sorted_price_pairs = sorted(zip(prices.values(), prices.keys()))

print(f"Original prices: {prices}")
print(f"Minimum price pair (value, key): {min_price_pair}")
print(f"Maximum price pair (value, key): {max_price_pair}")
print(f"Sorted price pairs (value, key): {sorted_price_pairs}")

# 注意：zip() 创建的迭代器只能被消费一次。
# 如果你需要多次使用它，最好先将其转换为列表。
price_pairs_list = list(zip(prices.values(), prices.keys()))
print(f"\nRe-checking min after converting to list: {min(price_pairs_list)}")

print("\n" + "="*40 + "\n")

# ====================================================================
# 5. 在两个字典中寻找相同点
# ====================================================================
print("--- 5. Finding Commonalities in Two Dictionaries ---")

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# 查找共同的键 (使用集合操作)
common_keys = a.keys() & b.keys()  # & 是集合的交集操作
print(f"Common keys: {common_keys}")

# 查找a中存在但b中不存在的键
keys_in_a_not_b = a.keys() - b.keys() # - 是集合的差集操作
print(f"Keys in a but not in b: {keys_in_a_not_b}")

# 查找共同的(键, 值)对
common_items = a.items() & b.items()
print(f"Common (key, value) pairs: {common_items}")

# 基于共同的键构建一个新的字典
common_dict_from_a = {key: a[key] for key in a.keys() & b.keys()}
print(f"New dictionary with common keys (values from a): {common_dict_from_a}")

print("\n" + "="*40 + "\n")

# ====================================================================
# 2. 对字典的键进行计算
# ====================================================================
print("--- 2. Calculations on Dictionary Keys ---")

# 当对字典直接进行计算时（如 min(prices)），操作的是键。

min_key = min(prices)
max_key = max(prices)

print(f"Minimum key: {min_key}")
print(f"Maximum key: {max_key}")

print("\n" + "="*40 + "\n")

# ====================================================================
# 3. 根据值来获取对应的键
# ====================================================================
print("--- 3. Getting Key Corresponding to Value ---")

# 如果你想找到拥有最小/最大值的键，可以这样做：

# 方法一：使用 lambda 函数作为 key
min_val_key = min(prices, key=lambda k: prices[k])
max_val_key = max(prices, key=lambda k: prices[k])

print(f"Key with min value: {min_val_key}")
print(f"Key with max value: {max_val_key}")

# 你还可以获取对应的值
min_value = prices[min_val_key]
print(f"Minimum value itself: {min_value}")

# 如果有多个条目具有相同的最小/最大值，min/max 只会返回第一个找到的键。
prices_with_ties = {'x': 1, 'y': 2, 'z': 1}
print(f"\nWith ties {prices_with_ties}, min key is: {min(prices_with_ties, key=lambda k: prices_with_ties[k])}")

print("\n" + "="*40 + "\n")

# ====================================================================
# 4. 根据值对字典排序
# ====================================================================
print("--- 4. Sorting Dictionary by Value ---")

# 使用 sorted() 和 lambda 函数来根据值对字典的键进行排序
sorted_keys_by_value = sorted(prices, key=lambda k: prices[k])

print("Keys sorted by value:")
for key in sorted_keys_by_value:
    print(f"  {key}: {prices[key]}")

# 如果想得到排序后的 (key, value) 对，可以对 .items() 进行排序
sorted_items_by_value = sorted(prices.items(), key=lambda item: item[1])
print("\nItems sorted by value:")
print(sorted_items_by_value)

print("\n" + "="*40 + "\n")