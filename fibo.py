def fibonacci(n):
    r = [0, 1]
    for x in range(n):
        r.append(r[-2] + r[-1])
    return r[:-2]

print(fibonacci(1))


