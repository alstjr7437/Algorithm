# 반복문으로 이진탐색하기
def binary_search(nums, target):
    low, high = 0, len(nums) - 1 # 제일 작은 인덱스, 제일 큰 인덱스

    while low <= high:
        mid = (low + high) // 2 # 중간인 인덱스
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return "찾지 못함"

# 재귀로 이진 탐색
def binary(start, end, target):
    if start > end :
        return -1
    mid = (start + end) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binary(start, mid - 1, target)
    else :
        return binary(mid + 1, end, target) 
nums = [0,1,2,3,4,7,2,7,5,9]

nums.sort()
start, end = 0, len(nums) - 1 
target = 5
print(binary(start, end, target))
print(binary_search(nums, target))


