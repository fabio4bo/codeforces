"""
2010/B - Three Brothers - Difficulty 800
"""

brothers = [1, 2, 3]

t = [int(x) for x in input().strip().split(" ")]

for i in t:
    brothers.remove(i)

print(brothers[0])