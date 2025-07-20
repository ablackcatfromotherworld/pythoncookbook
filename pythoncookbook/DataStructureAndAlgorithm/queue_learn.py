from collections import deque

# 1. 创建一个双端队列 (deque)
print("--- 1. 创建 deque ---")
d = deque(['c', 'd', 'e'])
print(f"初始 deque: {d}")

# 2. 从两端添加元素
print("\n--- 2. 添加元素 ---")
d.append('f')
print(f"append('f') 后: {d}")
d.appendleft('b')
print(f"appendleft('b') 后: {d}")

# 3. 从两端弹出元素
print("\n--- 3. 弹出元素 ---")
print(f"pop() -> {d.pop()}")
print(f"pop() 后: {d}")
print(f"popleft() -> {d.popleft()}")
print(f"popleft() 后: {d}")

# 4. 扩展 deque
print("\n--- 4. 扩展 deque ---")
d.extend(['f', 'g'])
print(f"extend(['f', 'g']) 后: {d}")
d.extendleft(['a', 'b'])
print(f"extendleft(['a', 'b']) 后: {d}") # 注意 extendleft 的顺序

# 5. 旋转 deque
print("\n--- 5. 旋转 deque ---")
print(f"原始 deque: {d}")
d.rotate(2) #向右旋转2位
print(f"rotate(2) 后: {d}")  # d.rotate(2) 向右移动2位
d.rotate(-3) #向左旋转3位
print(f"rotate(-3) 后: {d}")  # d.rotate(3) 向左移动3位

# 6. 固定长度的 deque (maxlen)
print("\n--- 6. 使用 maxlen ---")
d_fixed = deque(maxlen=3)
print(f"创建 maxlen=3 的 deque: {d_fixed}")
d_fixed.append(1)
d_fixed.append(2)
d_fixed.append(3)
print(f"添加 1, 2, 3 后: {d_fixed}")
d_fixed.append(4) # 添加新元素，左边的元素会自动移除
print(f"append(4) 后: {d_fixed}")
d_fixed.appendleft(0) # 从左边添加新元素，右边的元素会自动移除
print(f"appendleft(0) 后: {d_fixed}")

# 7. 使用 deque 实现历史记录功能
print("\n--- 7. 使用 deque 实现历史记录功能 ---")
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# 示例: 在一个文件中查找包含 'python' 的行，并打印其前5行的历史记录
# example_file_content = [f'Line {i}' for i in range(10)] + ['Line 10 contains python'] + [f'Line {i}' for i in range(11, 20)]
example_file_content = []
for i in range(10):
    example_file_content.append(f"Line {i}")
example_file_content.append("Line 10 contains python")
for i in range(11, 20):
    example_file_content.append(f"Line {i}")

print("在一个虚拟文件中查找 'python':")
for line, prev_lines in search(example_file_content, 'python', 5):
    print(f"找到匹配: {line}")
    print(f"历史记录: {list(prev_lines)}")