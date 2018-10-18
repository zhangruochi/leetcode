## 思路

```Python
if char_s in char_map and char_map[char_s] != char_t:
    return False

if char_s not in char_map and char_t in value_set:
    return False
```

- Isomorphic String 是一一映射的关系
- 上述两个条件，第一个检查是否存在一对多的关系，第二个检查是否存在多对一的关系

