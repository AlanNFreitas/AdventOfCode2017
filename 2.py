import adventutils

def inv_captcha(n):
    return sum([int(n[i]) for i in range(len(n)) if n[i] == n[i - len(n) // 2]])

captcha = adventutils.input_string()
print(inv_captcha(captcha))
