# Making Change

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

## Usage

```python
makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

## Prototype
```python
def makeChange(coins, total)
```

## Return
- Fewest number of coins needed to meet total
- 0 if total is 0 or less
- -1 if total cannot be met by any number of coins

## Notes
- `coins` is a list of coin values (integers > 0)
- You have an infinite number of each denomination
- Uses dynamic programming for optimal solution