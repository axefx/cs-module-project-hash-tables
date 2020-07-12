"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6
sum_cache = {}
diff_cache = {}
def sumdiff(q):
    results = []
    for i in range(len(q)):
        for j in range(len(q)):
            sum_cache[(q[i],q[j])] = f(q[i]) + f(q[j])
            diff_cache[(q[i],q[j])] = f(q[i]) - f(q[j])
    for a in sum_cache:
        for s in diff_cache:
            if sum_cache[a] == diff_cache[s]:
                result = f"{f(a[0])} + {f(a[1])} = {f(s[0])} - {f(s[1])}"
                results.append(result)
    return results
print(sumdiff(q))
