def totalFruit(fruits):
    from collections import defaultdict

    count = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(fruits)):
        count[fruits[right]] += 1

        # Shrink the window until we have at most 2 types of fruits
        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1

        # Update max length
        max_len = max(max_len, right - left + 1)

    return max_len
