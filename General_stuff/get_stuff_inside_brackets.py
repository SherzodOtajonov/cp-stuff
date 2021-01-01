# used this for google kickstart 2020 round B problem C

def match_brackets():
    s = input()
    flag = False
    opens = 0
    start_idx = end_idx = 0
    for i in range(len(s)):
        if s[i] == '(' and not flag:
            opens += 1
            flag = True
            start_idx = i+1
        elif s[i] == '(' and flag:
            opens += 1
        elif s[i] == ')':
            opens -= 1

        if flag and opens == 0:
            flag = False
            end_idx = i
    return s[start_idx: end_idx]

print(match_brackets())
