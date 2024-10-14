# 主函數，呼叫 permNext 開始生成排列
def perm(n):
    permNext(n, [])

# 遞迴生成排列
def permNext(n, p):
    i = len(p)  # 已經排好 p[0..i-1]，i 是目前排列的長度
    if i == n:  # 如果已經排好了 (p 的長度等於 n)
        print(p)  # 印出排列
        return

    # 還沒排滿，繼續遞迴生成下一個排列
    for x in range(n):  # 對於每一個 x（範圍是 0 到 n-1）
        if x not in p:  # 如果 x 還不在當前排列中
            p.append(x)  # 把 x 放入當前排列
            permNext(n, p)  # 繼續遞迴尋找下一個排列
            p.pop()  # 遞迴回來之後，將 x 從排列中移除以嘗試其他可能

# 測試 perm 函數
perm(2)  # 列出 2 個元素的排列
perm(3)  # 列出 3 個元素的排列
perm(4)  # 列出 4 個元素的排列
perm(5)  # 列出 5 個元素的排列
