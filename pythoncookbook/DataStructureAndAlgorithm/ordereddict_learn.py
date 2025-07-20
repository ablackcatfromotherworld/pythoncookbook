from collections import OrderedDict
import json

# ====================================================================
# 1. 基本的 OrderedDict 使用
# ====================================================================
print("--- 1. Basic OrderedDict Usage ---")

# 在 Python 3.7+ 中，常规的 dict 也会保持插入顺序。
# 但在之前的版本中，只有 OrderedDict 能保证这一点。
# 为了演示，我们假设在旧版 Python 环境中。

# 创建一个常规字典
print("Regular dict:")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
for key, value in d.items():
    print(key, value)

print("\nOrderedDict:")
# 创建一个 OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)

print("\n" + "="*40 + "\n")

# ====================================================================
# 2. 控制元素的顺序
# ====================================================================
print("--- 2. Controlling Item Order ---")

print(f"Original OrderedDict: {od}")

# popitem(last=True) -> 后进先出 (LIFO)
od.popitem() # 移除 'd'
print(f"After popitem(last=True): {od}")

# popitem(last=False) -> 先进先出 (FIFO)
od.popitem(last=False) # 移除 'a'
print(f"After popitem(last=False): {od}")

# move_to_end(key, last=True) -> 将键移动到末尾
od.move_to_end('b')
print(f"After move_to_end('b'): {od}")

# move_to_end(key, last=False) -> 将键移动到开头
od.move_to_end('c', last=False)
print(f"After move_to_end('c', last=False): {od}")

print("\n" + "="*40 + "\n")

# ====================================================================
# 3. 在 JSON 序列化中的应用
# ====================================================================
print("--- 3. Usage in JSON Serialization ---")

# OrderedDict 在需要生成有特定顺序的 JSON 时非常有用

json_data = OrderedDict()
json_data['name'] = 'John Doe'
json_data['age'] = 30
json_data['isStudent'] = False
json_data['courses'] = [
    OrderedDict([('title', 'History'), ('credits', 3)]),
    OrderedDict([('title', 'Math'), ('credits', 4)])
]

# 当序列化为 JSON 字符串时，键的顺序将被保留
json_string = json.dumps(json_data, indent=4)
print("Serialized JSON with OrderedDict:")
print(json_string)

# 如果使用常规字典（在 Python < 3.7 中），顺序可能不会被保留
# 注意：在 Python 3.7+ 中，dict 也有序，所以差异不明显
plain_dict_for_json = {
    'name': 'John Doe',
    'age': 30,
    'isStudent': False,
    'courses': [
        {'title': 'History', 'credits': 3},
        {'title': 'Math', 'credits': 4}
    ]
}
print("\nSerialized JSON with regular dict:")
print(json.dumps(plain_dict_for_json, indent=4))

print("\n" + "="*40 + "\n")