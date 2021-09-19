# 標準入力を受け付ける。
A, B = map(int, input().split())

# 整数(10進数)を二進表記へ変更する。
# 参考 : https://note.nkmk.me/python-bin-oct-hex-int-format/
A = list(format(A, 'b'))
B = list(format(B, 'b'))

lenA = len(A)
lenB = len(B)

# A, Bの値を二進表記に変換する際に、ビットの桁数を合わせるように調整する。
# insert関数参考 : https://note.mokuzine.net/python-list-append-extend-insert/#insert%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E8%A6%81%E7%B4%A0%E3%82%92%E6%8C%BF%E5%85%A5%E3%81%99%E3%82%8B
if lenA > lenB:
    N = lenA
    for j in range(0, lenA - lenB):
        B.insert(0, '0')
else:
    N = lenB
    for j in range(0, lenB - lenA):
        A.insert(0, '0')

C = []
for i in range(0, N):
    # 二進表記したA, Bの各ビット単位で以下の確認を行う。
    # 各ビットの値がA = 1, B = 1の場合、Cを0とする。
    # 各ビットの値がA = 1, B = 0の場合、Cを1とする。
    # 各ビットの値がA = 0, B = 1の場合、Cを1とする。
    # 各ビットの値がA = 0, B = 0の場合、Cを0とする。
    if A[i] == B[i]:
        C.append('0')
    else:
        C.append('1')

print(int("".join(C), 2))
