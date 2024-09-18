from collections import Counter
import string


def calculate_ic(text):
    """计算文本的重合指数"""
    text = text.upper()
    frequency = Counter(text)
    total_letters = sum(frequency.values())

    if total_letters <= 1:
        return 0

    ic = sum(count * (count - 1) for count in frequency.values())
    ic /= total_letters * (total_letters - 1)

    return ic


def find_key_length_and_ic(ciphertext, expected_ic=0.065, max_key_length=20):
    """估算密钥长度并计算对应的重合指数"""
    best_key_length = None
    min_diff = float('inf')
    key_length_ic = {}

    for key_length in range(1, max_key_length + 1):
        ic_values = []

        # 分组计算每个组的重合指数
        for i in range(key_length):
            group = ciphertext[i::key_length]
            ic = calculate_ic(group)
            ic_values.append(ic)

        # 平均重合指数
        average_ic = sum(ic_values) / len(ic_values)
        diff = abs(average_ic - expected_ic)

        key_length_ic[key_length] = average_ic

        if diff < min_diff:
            min_diff = diff
            best_key_length = key_length

    return best_key_length, key_length_ic


# 示例数据
ciphertext = ("IYMYSIKNMQEMAOVOHCAPEYRFXYFQVXJGALTNWBUNJYJZJCXCFYFPROYYXNWJKAKBZGPROZZYCOOVUYRZGNSTYWHDPAAIYPSPUJXUPCTROAZEPPWDFQUWOTYAPVECWMOBUZZAOJTSEASPUNNTBYNSFABAESNMPBJKJOAVHVORCNTTOKYZOVSZNQVWWKPHWXCYUAXCYGLSYSATDAYCWEAAWGTZMAHCBCEXCPNDTWFSOCYQGUGGPHDYEQ")
# 估算密钥长度和计算对应的重合指数
estimated_key_length, key_length_ic = find_key_length_and_ic(ciphertext)

# 输出结果
print("Estimated key length:", estimated_key_length)
print("Key length and corresponding IC values:")
for length, ic in key_length_ic.items():
    print(f"Key length {length}: IC = {ic:.4f}")
