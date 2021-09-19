# 標準入力を受け付ける。
N = int(input())
A = list(map(int, input().split()))

# 選手の番号情報を格納する。
indices = [*range(len(A))]

# 初期の選手の順番を記憶に残しつつ、スコアの順序を並び替える(降順)。
# 降順とは? : https://www.weblio.jp/content/%E9%99%8D%E9%A0%86
# key optionについて : https://note.nkmk.me/python-key-sort-sorted-max-min/
sorted_indices = sorted(indices, key=lambda i: -A[i])
# sorted関数によって、スコアを降順に並べ替えたので、前から2番目の選手の番号を取得する。
# 最後に+1しているのは、配列の要素の都合上。
print(sorted_indices[1] + 1)
