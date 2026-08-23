class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        # Not enough flowers to make m bouquets
        if m * k > len(bloomDay):
            return -1

        low = 1
        high = max(bloomDay)

        while low <= high:

            mid = (low + high) // 2

            count = 0
            bouquets = 0

            for day in bloomDay:

                if day <= mid:
                    count += 1

                    if count == k:
                        bouquets += 1
                        count = 0

                else:
                    # Consecutive sequence is broken
                    count = 0

            if bouquets >= m:
                # Enough bouquets → try fewer days
                high = mid - 1
            else:
                # Not enough bouquets → need more days
                low = mid + 1

        return low