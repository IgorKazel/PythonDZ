example = '12 - 4 * 2 + 6 / 3'

result = example.split()
for i in range(0, len(result), 2):
    result[i] = int(result[i])

def calc_priority_1(res):
    for i in range(1, len(res), 2):
        if res[i] == '*':
            res[i-1] = res[i-1] * res[i+1]
            res.pop(i)
            res.pop(i)
            return calc_priority_1(res)
        elif res[i] == '/':
            res[i-1] = res[i-1] / res[i+1]
            res.pop(i)
            res.pop(i)
            return calc_priority_1(res)     
    return res

def calc_priority_2(res):
    for i in range(1, len(res), 2):
        if res[i] == '+':
            res[i-1] = res[i-1] + res[i+1]
            res.pop(i)
            res.pop(i)
            return calc_priority_2(res)
        elif res[i] == '-':
            res[i-1] = res[i-1] - res[i+1]
            res.pop(i)
            res.pop(i)
            return calc_priority_2(res)     
    return res

result = calc_priority_1(result)
result = calc_priority_2(result)
print(example,'=',result[0])
