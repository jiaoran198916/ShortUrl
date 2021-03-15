def mybin(num):  # 10进制->2进制串
    if num == 0:
        return 0
    res = []
    while num:
        num, rem = divmod(num, 2)  # 2 -> 62
        res.append(str(rem))
    return ''.join(reversed(res))


CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def encode(num):
    if num == 0:
        return CHARS[0]
    res = []
    while num:
        num, rem = divmod(num, len(CHARS))  # 62
        res.append(CHARS[rem])
    return ''.join(reversed(res))


print(encode(1))
print(encode(61))