import random
## 活动选择问题
def get_max_activities(activities):
    activities.sort(key = lambda x:x[1])

    result = []
    for act in activities:
        if not result:
            result.append(act)

        if act[0] > result[-1][1]:
            result.append(act)

    return result

if __name__ == '__main__':
    activities = [(1,2),(3,4),(0,6),(5,7),(8,9),(5,9)]
    random.shuffle(activities)
    print(get_max_activities(activities))




def gcd(a,b):
    if b == 0:
        return a
    q,r = divmod(a,b)
    return gcd(b,r)

def lcm(a,b):
    return a*b//gcd(a,b)


def recursion(nr,dr,result):
    if nr == 1:
        return result + "{}/{}".format(nr,dr)

    prev = dr
    dr2 = dr//nr + 1
    dr = lcm(dr,dr2)
    nr = nr*(dr//prev) - dr//dr2

    return recursion(nr,dr,result + "{}/{} + ".format(1,dr2))




def egyptian_fraction(nr,dr):
    if dr%nr == 0:
        return "1/{}".format(dr%nr)

    return recursion(nr,dr,"")


if __name__ == '__main__':
    result = egyptian_fraction(12,13)
    print(result)

    
