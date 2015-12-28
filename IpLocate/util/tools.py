def left_space(key, max_len):
    target_len = len(key)
    if max_len > target_len:
        return max_len - target_len
    else:
        return 0


