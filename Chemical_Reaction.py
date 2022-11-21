import matplotlib.pyplot as plt

k1 = 0.008
k2 = 0.002
a = 100
b = 50
c = 0
delta_t = 0.1
t = 0
n = input()

array_a = []
array_b = []
array_c = []
array_t = []

while t < int(n):

    t += delta_t

    array_a.append(a)
    a = a + (k2 * c - k1 * a * b) * delta_t

    array_b.append(b)
    b = b + (k2 * c - k1 * a * b) * delta_t

    array_c.append(c)
    c = c + (2 * k1 * a * b - 2 * k2 * c) * delta_t

    array_t.append(t)
    
print(array_a, array_b, array_c)

plt.plot(array_t, array_a, label="a", color="red")
plt.plot(array_t, array_b, label = "b", color = "green")
plt.plot(array_t, array_c, label = "c", color = "blue")

plt.legend()

plt.show()
