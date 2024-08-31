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

def moveZeroes(nums):
    count = 0
    for i, num in enumerate(nums):
        if num == 0:
            count += 1
            continue
        nums[i], nums[i-count] = nums[i-count], nums[i]
        
    return nums


"""Ro'yxatni aylantiring
Berilgan ro'yxatni k qadam o'ng tomonga aylantiring.

Ro'yxatni 1 qadam o'ng tomonga aylantirish, o'ng tomondagi ohirgi elementni, chap tomonning boshiga olib qo'yish degani.

Amalni berilgan ro'yhat ustida bajaring - yangi ro'yxat yaratmang.

Misol 1:
Kiritish: nums = [1,2,3,4,5,6,7], k = 3
Natija: [5,6,7,1,2,3,4]
Tushuntirish:
1-qadam: [7,1,2,3,4,5,6]
2-qadam: [6,7,1,2,3,4,5]
3-qadam: [5,6,7,1,2,3,4]
Misol 2:
Kiritish: nums = [-1,-100,3,99], k = 2
Natija: [3,99,-1,-100]
Tushuntirish: 
1-qadam: [99,-1,-100,3]
2-qadam: [3,99,-1,-100]"""

def reverse(nums, i , j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


def rotate(nums: list, k: int):
    k = k % len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)
    return nums

