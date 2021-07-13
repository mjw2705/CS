import re

word = "blind"
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]


weburl = []
webname = []
webgraph = dict() # 나를 가리키는 외부 링크

for page in pages:
    url = re.search('<meta property="og:url" content="https://(\S+)"', page).group(1)

    basicscore = 0
    for body in re.findall(r'[a-zA-Z]+', page.lower()):
        if body == word.lower():
            basicscore += 1

    outlink = re.findall('<a href="https://(\S+)"', page)
    for out in outlink:
        if out not in webgraph.keys():
            webgraph[out] = [url]
        else:
            webgraph[out].append(url)
    # {'b.com': ['a.com'], 'a.com': ['b.com', 'c.com'], 'c.com': ['b.com']}

    webname.append(url) # ['a.com', 'b.com', 'c.com']
    weburl.append([url, basicscore, len(outlink)])
    # [['a.com', 3, 1], ['b.com', 1, 2], ['c.com', 1, 1]]

scores = []
for i in range(len(weburl)):
    linkscore = 0
    url = weburl[i][0]
    score = weburl[i][1]

    if url in webgraph.keys():
        for link in webgraph[url]:
            a, b, c = weburl[webname.index(link)]
            linkscore = b / c
            score += linkscore
    scores.append([score, i])

answer = sorted(scores, key=lambda x:[-x[0], x[1]])
# [[4.5, 0], [4.0, 1], [1.5, 2]]

print(answer[0][1])