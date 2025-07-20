from collections import defaultdict

# ====================================================================
# 1. 使用 defaultdict(list) 对项目进行分组
# ====================================================================
print("--- 1. Grouping with defaultdict(list) ---")

# 假设我们有一个元组列表，表示一系列的键值对
pairs = [('a', 1), ('b', 2), ('a', 3), ('c', 4), ('b', 5), ('a', 1)]

# 传统方法（使用普通字典）
d_plain = {}
for key, value in pairs:
    if key not in d_plain:
        d_plain[key] = []
    d_plain[key].append(value)
print(f"Plain dict: {d_plain}")

# 使用 defaultdict 的方法
# 当我们首次访问一个不存在的键时，default_factory (这里是 list)
# 会被调用来提供一个默认值（一个空的列表 []），然后这个值会被赋给该键。
d_default_list = defaultdict(list)
for key, value in pairs:
    d_default_list[key].append(value) # 无需检查键是否存在

print(f"defaultdict(list): {d_default_list}")
print(f"Accessing 'a': {d_default_list['a']}")
print(f"Accessing 'b': {d_default_list['b']}")
print("\n" + "="*40 + "\n")

# ====================================================================
# 2. 使用 defaultdict(int) 进行计数
# ====================================================================
print("--- 2. Counting with defaultdict(int) ---")

some_list = ['apple', 'orange', 'apple', 'banana', 'orange', 'apple']

# default_factory 为 int，它会返回 0
d_default_int = defaultdict(int)
for item in some_list:
    d_default_int[item] += 1 # 如果 item 不存在，它会被初始化为 0，然后 +1

print(f"defaultdict(int): {d_default_int}")
print(f"Count of 'apple': {d_default_int['apple']}")
print(f"Count of 'grape' (not in list): {d_default_int['grape']}") # 访问不存在的键，返回默认值 0
print(f"Dict after accessing 'grape': {d_default_int}") # 注意：访问后，'grape' 被添加到了字典中
print("\n" + "="*40 + "\n")

# ====================================================================
# 3. 使用 defaultdict(set) 存储唯一值
# ====================================================================
print("--- 3. Storing unique values with defaultdict(set) ---")

# 我们使用之前的 pairs 列表，但这次我们想为每个键存储一组唯一的值
d_default_set = defaultdict(set)
for key, value in pairs:
    d_default_set[key].add(value) # 使用 .add() 方法添加到集合中

print(f"defaultdict(set): {d_default_set}")
print(f"Unique values for 'a': {d_default_set['a']}") # 注意，重复的 1 被自动去除了
print("\n" + "="*40 + "\n")