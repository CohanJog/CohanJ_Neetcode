class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()

            first = stones.pop()
            last = stones.pop()

            if first != last:
                stones.append(first - last)
        if stones:
                return stones[0]
        return 0
