# shanten-tools

Fast calculation of shanten numbers in Japanese Mahjong.

## Usage

```
>>> from shanten_tools import shanten
>>> hand = [
>>>     3,1,1,1,1,1,1,1,3,
>>>     0,0,0,0,0,0,0,0,0,
>>>     0,0,0,0,0,0,0,0,0,
>>>     0,0,0,0,0,0,0]
>>> shanten(hand)
0
```

## Notes
- `sum(hand)` must be $3n+1$ or $3n+2$ with $n=0,1,2,3,4$.
- 国士無双 and 七対子 is not supported.