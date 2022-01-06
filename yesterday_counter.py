#yesterday 노래에는 yesterday라는 단어가 몇번 나올까?

f = open("yesterday.txt", 'r')
yesterday_lyric = ""
while True:
    line = f.readline()
    if not line:
        break
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"
f.close()

n_or_yesterday = yesterday_lyric.count("Yesterday")   #대소문자 구분 제거
s_or_yesterday = yesterday_lyric.count("yesterday")
nn_or_yesterday = yesterday_lyric.upper().count("YESTERDAY")
print("Number of a Word 'Yesterday'", n_or_yesterday)
print("Number of a Word 'yesterday'", s_or_yesterday)
print("Number of a Word 'YESTERDAY'", nn_or_yesterday)