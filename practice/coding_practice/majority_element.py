
def majorityElement(nums):
    count = 0

    for val in nums:
        if count == 0:
            element = val
            count = 1
        elif val == element:
            count += 1
        else:
            count -= 1

    if count > 0:
        return element
