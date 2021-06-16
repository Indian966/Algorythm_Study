import pandas as pd
import numpy as np


class upgrade():
    # 성공 결과와 실패한 횟수를 초기화해주는 함수
    def reset(upgrade, fail) :
        for i in range(len(upgrade)) :
            if fail[i] == 2 :
                upgrade[i] = 0
                fail[i] = 0
    prob = 0.7

    # 성공 횟수와 실패 횟수
    upgradestate = pd.DataFrame({'day0':[0]*100})
    failstate = pd.DataFrame({'day0': [0] * 100})

    for i in range(1,62) :
        # 확률 계산
        attemptresult = np.random.binomial(n=1, p=prob, size=100)

        # 성공 횟수에 확률 계산 결과를 더하되 5를 넘지 않음
        upgradestate['day%s' % i] = np.minimum(upgradestate['day%s' % (i - 1)] + attemptresult, 5)

        # 실패 횟수 계산
        failstate['day%s' % i] = failstate['day%s' % (i - 1)] + (attemptresult == 0) * 1

        # 실패 횟수가 2이상이 되면 강화 결과를 0으로 초기화
        reset(upgradestate['day%s' % i],failstate['day%s' % i])

    print(upgradestate)
    print(failstate)
