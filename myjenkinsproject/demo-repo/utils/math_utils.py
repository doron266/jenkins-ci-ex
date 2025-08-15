
def add_numbers(nums):
    if not isinstance(nums, list):
        raise TypeError('nums must be a list')
    total = 0.0
    for n in nums:
        if not isinstance(n, (int, float)):
            raise TypeError('numbers must be numeric')
        total += n
    return total
