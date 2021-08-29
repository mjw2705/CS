import re

filess = [["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],
["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"],
          ["img000012345", "img1.png", "img2", "IMG02"]]

# 정답 o, 런타임 에러, len(number) > 5일 때의 처리 필요
def solution1(filess):
    for files in filess:
        idx = 0
        ans = []
        for file in files:
            file = file.lower()
            head, number, tail = "", "", ""
            for i in range(len(file)):
                if file[i].isdigit():
                    head = file[:i]
                    file = file[i:]
                    break

            for i in range(len(file)):
                if not file[i].isdigit():
                    number = file[:i]
                    tail = file[i:]
                    break

            ans.append([head, number, tail, idx])
            idx += 1
        ans.sort(key=lambda x: (x[0], int(x[1]), x[3]))

        answer = []
        for i in ans:
            answer.append(files[i[3]])

        print(answer)
    # return answer

# print(solution1(filess))


# 정확도 100
def solution2(filess):
    for files in filess:
        ans = []
        for f in files:
            spl = re.split(r"([0-9]{1,5})", f)
            # ['img', '12', '.png']로 split
            ans.append(spl)

        ans = sorted(ans, key=lambda x: (x[0].lower(), int(x[1])))
        answer = [''.join(s) for s in ans]
        print(answer)

print(solution2(filess))