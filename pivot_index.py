def Pivot(nums):
    prefix = []
    current = 0
    for n in nums:
        current += n
        prefix.append(current)
    
    total = prefix[-1]
    
    for i in range(len(nums)):
        left = 0 if i == 0 else prefix[i-1]
        right = total - prefix[i]
        if left == right:
            return i
    
    return -1
