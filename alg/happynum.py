# 快乐数判断：各位数字相加能达到1即为快乐数

def isHappy(n):
    """

    :type n: int
    :rtype: bool
    """

    def pfh(n):
        ys = n % 10
        shang = int (n / 10)
        count = ys ** 2
        while shang != 0:
            ys = shang % 10
            shang = int (shang / 10)
            count += ys * ys
        return count

    if n == 1:
        return True
    if n == 0:
        return False
    anser_list = [n]
    num = pfh(n)
    while num != 1:
        if num not in anser_list:
            anser_list.append(num)
            num = pfh(num)
        else:
            return False
    return True

isHappy(7)

"""解法二
def get_next(n):
    total_sum = 0
    while n > 0:
        n, digit = divmod(n, 10)
        total_sum += digit ** 2
    return total_sum


seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    n = get_next(n)

return n == 1
"""
"""解法三：双指针
def get_next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    slow_runner = n
    fast_runner = get_next(n)
    while fast_runner != 1 and slow_runner != fast_runner:
        slow_runner = get_next(slow_runner)
        fast_runner = get_next(get_next(fast_runner))
    return fast_runner == 1

"""
"""

cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}

    def get_next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    while n != 1 and n not in cycle_members:
        n = get_next(n)

    return n == 1

"""
