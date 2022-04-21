# N, K = map(int, input().split())
# weights = []
# values = []
# for i in range(N) :
#     W, V = map(int, input().split())
#     weights.append(W)
#     values.append(V)
# print(weights, values)
import pprint
N = 4
K = 7
weights = [6, 4, 3, 5]
values = [13, 8, 6, 2]


def sum_of_value(max_weight, weight, value):
    n = len(value)
    # 가로 : 최대 무게, 세로 : 물건의 갯수
    ans = [[0 for x in range(max_weight + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(max_weight + 1):
            if i == 0 or w == 0:
                ans[i][w] = 0
            elif weight[i - 1] <= w:
                ans[i][w] = max(value[i - 1] + ans[i - 1][w - weight[i - 1]], ans[i - 1][w])
            else:
                ans[i][w] = ans[i - 1][w]
    pprint.pprint(ans)
    return ans[n][max_weight]


print(sum_of_value(K, weights, values))

