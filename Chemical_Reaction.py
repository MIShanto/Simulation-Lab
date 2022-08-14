k1 = 0.008
k2 = 0.002
a = 100
b = 50
c = 0
t = 0.1

n = input()

array_a = []
array_b = []
array_c = []

for i in range(int(n)):
    array_a.append(a)
    a = a + (k2 * c - k1 * a * b) * t

    array_b.append(b)
    b = b + (k2 * c - k1 * a * b) * t

    array_c.append(c)
    c = c + (2 * k1 * a * b - 2 * k2 * c) * t

print(array_a, array_b, array_c)