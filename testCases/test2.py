

def cons(num):
    num_set = set(num)
    longest_streak = 0
    for nm in num_set:
        if nm-1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num + 1 in num_set:
                current_num = current_num+1
                current_streak=current_streak+1
            longest_streak = max(longest_streak, current_streak)