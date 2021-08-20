ss = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]

for s in ss:

    answer = len(s)
    for uint in range(1, len(s)):
        ans = ''
        cnt = 1
        char = s[:uint]

        for i in range(uint, len(s), uint):
            # 문자열 반복될 때
            if char == s[i : i + uint]:
                cnt += 1
            else:
                if cnt == 1:
                    ans += char
                else:
                    ans += str(cnt) + char
                char = s[i : i + uint]
                cnt = 1

        # 남은 문자열
        if cnt == 1:
            ans += char
        else:
            ans += str(cnt) + char

        answer = min(answer, len(ans))

    print(answer)



