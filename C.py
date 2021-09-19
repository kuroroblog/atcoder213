# 標準入力を受け付ける。
H, W, N = input().split()
# 型変換を行う。
N = int(N)
# 参考 : https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785#%E5%88%97%E3%81%AB%E5%A4%89%E6%95%B0%E3%81%8C%E4%B8%A6%E3%81%B6%E3%81%A8%E3%81%8D
AB = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*AB)]

# Nの値分のindexをリスト化する。
indices = [*range(N)]
# ソートする前のA, Bのindexを記憶しておく。
# key optionについて : https://note.nkmk.me/python-key-sort-sorted-max-min/
sorted_indicesA = sorted(indices, key=lambda i: A[i])
sorted_indicesB = sorted(indices, key=lambda i: B[i])

# ソート済みのAi, Bi座標が、ひとつ以上前のAi, Biの座標と等しいか、確認するために利用する。
tmpA = -1
tmpB = -1

# Ai, Biの転移する座標情報
Aposition = 0
Bposition = 0

# A, Bの転移する座標情報
Ainfo = []
Binfo = []

# A, Bの座標情報をソートする。
A.sort()
B.sort()

for i in range(0, N):
    # 過去に座標Aiが存在する場合、転移する座標Aiを更新しない。
    if not tmpA == A[i]:
        Aposition = Aposition + 1
        tmpA = A[i]

    # 過去に座標Biが存在する場合、転移する座標Biを更新しない。
    if not tmpB == B[i]:
        Bposition = Bposition + 1
        tmpB = B[i]

    # ソートする前のA[i], B[i]のindexを、index keyへ追加する。
    # 転移するA[i], B[i]の座標をpostion keyへ追加する。
    Ainfo.append({
        'index': sorted_indicesA[i],
        'position': Aposition,
    })
    Binfo.append({
        'index': sorted_indicesB[i],
        'position': Bposition,
    })

# ソートする前のA, Bのindex順に並べ替える。
# key optionについて : https://note.nkmk.me/python-key-sort-sorted-max-min/
Ainfo = sorted(Ainfo, key=lambda x:x['index'])
Binfo = sorted(Binfo, key=lambda x:x['index'])

# 出力
for i in range(0, N):
    print(str(Ainfo[i]['position']) + ' ' + str(Binfo[i]['position']))
