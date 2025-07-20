import heapq

# --- 1. 查找最大或最小的N个元素 ---
print("--- 1. Finding the N largest/smallest items ---")
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# 查找最大的3个元素
print("Largest 3:", heapq.nlargest(3, nums))  # Outputs: [42, 37, 23]

# 查找最小的3个元素
print("Smallest 3:", heapq.nsmallest(3, nums)) # Outputs: [-4, 1, 2]

# 对于更复杂的数据结构，可以提供 key 参数
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]


cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print("3 cheapest stocks:", cheap)
print("3 most expensive stocks:", expensive)


# --- 2. 实现优先级队列 ---
print("\n--- 2. Implementing a Priority Queue ---")

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # heapq是最小堆，所以我们把priority取负数，来实现按优先级从大到小排序
        # (priority, index, item)元组可以保证：
        # 1. 首先按优先级排序
        # 2. 如果优先级相同，则按插入顺序（index）排序
        # 3. item本身不会被比较，避免了当item不支持比较时出错
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # heappop总是返回最小的元素
        return heapq.heappop(self._queue)[-1]

# 优先级队列使用示例
class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'Item({self.name!r})'

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print("Popping items from priority queue:")
# 应该按优先级 5, 4, 1, 1 的顺序弹出 bar, spam, foo, grok
# foo 和 grok 优先级相同，按插入顺序弹出
print(q.pop()) # Item('bar')
print(q.pop()) # Item('spam')
print(q.pop()) # Item('foo')
print(q.pop()) # Item('grok')