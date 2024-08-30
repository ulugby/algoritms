"""Nollarni orqaga surish masalasi

Berilgan sonlar ro'yxatidagi nollarni ro'yxat orqasiga o'tkazing, lekin boshqa elementlar ketma-ketligi buzilmasin.

Imkon qadar kamroq amal bajaring.

Qo'shimcha xotiradan foydalanmang - amallarni ro'yxat ustida bajaring.

Misol 1:
Kiritish: nums = [0,1,0,3,12]
Natija: [1, 3, 12, 0, 0]
Misol 1:
Kiritish: nums = [0]
Natija: [0]"""


"This is my solution algorithm"
def moveZeroes(nums):
    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

    for i in range(j, len(nums)):
        nums[i] = 0

    return nums



"This is my teacher's solution"
def moveZeroes(nums):
    count = 0
    for i, num in enumerate(nums):
        if num == 0:
            count += 1
            continue
        nums[i], nums[i-count] = nums[i-count], nums[i]
        
    return nums

