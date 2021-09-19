import sys

# 再起の上限をつけるために利用する。
# 参考 : https://note.nkmk.me/python-sys-recursionlimit/
sys.setrecursionlimit(10**6)

# 標準入力を受け付ける。
N = int(input())

# 都市の番号情報を格納する。
edge = [[] for _ in range(N + 1)]

# 標準入力を受け付ける。
for _ in range(N - 1):
    a, b = map(int, input().split())
    # 都市の番号情報と次の都市の番号情報を紐付ける。
    edge[a].append(b)
    edge[b].append(a)

# 答えを格納する。
ans = []

def dfs(now, last=-1):
    # 再起を利用して、番号が最も小さい都市を出力する。
    ans.append(now)
    # 次の都市の番号情報をソートする。
    edge[now].sort()
    for to in edge[now]:
        # 前の都市の番号を次の都市の番号として、選ばれないようにする。
        if to == last:
            continue
        dfs(to, now)
        # 再起から戻ってきた時の都市の番号を出力する。
        ans.append(now)

dfs(1)

print(*ans)
