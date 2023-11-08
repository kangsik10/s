import webbrowser
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
url = "https://news.naver.com/main/list.naver?mode=LPOD&sid2=140&sid1=001&mid=sec&oid=001&isYeonhapFlash=Y&date=2023080"        
for i in number:
    URL = url+str(i)
    webbrowser.open(URL)
    print(URL)
    for g in range(1, 20):
        U=URL+"&page="+str(g)
        webbrowser.open(U)
        print(U)

numbe = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
ur = "https://news.naver.com/main/list.naver?mode=LPOD&sid2=140&sid1=001&mid=sec&oid=001&isYeonhapFlash=Y&date=202308"        
for h in numbe:
    UR = ur+str(h)
    webbrowser.open(UR)
    print(UR)
    for f in range(1, 20):
        U=UR+"&page="+str(f)
        webbrowser.open(U)
        print(U)
