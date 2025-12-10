#!/usr/bin/python3
def weight_average(my_list=[]):
    # list[i] = (score, weight) tuple
    score = []
    weight = []
    if my_list:
        for i in my_list:
            score.append(i[0])
            weight.append(i[1])
        # result = (score + weight) / weight
        weight_sum = 0
        for a in weight:
            weight_sum +=a
        score_weight = list(map(lambda x,y: x*y, score, weight))
        score1 = 0
        for b in score_weight:
            score1 +=b
        result = score1 / weight_sum
        return result
    else:
        return 0
