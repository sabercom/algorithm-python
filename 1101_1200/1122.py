class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        orders = {n: i for i, n in enumerate(arr2)}
        return sorted(arr1, key=lambda n: (orders.get(n, 10000), n))
