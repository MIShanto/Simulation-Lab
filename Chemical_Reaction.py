import matplotlib.pyplot as plt

k1 = 0.008
k2 = 0.002
a0 = 100
b0 = 50
c0 = 0
delta_t = 0.1
t = 0
n = input()

array_a = []
array_b = []
array_c = []
array_t = []

print("\tTime\t \tA (i)\t \tB(i)\t \tC(i)\t")
print("%12.2f %16.2f %15.2f %15.2f"%(t,a0,b0,c0))

while t <= int(n):
    t += delta_t

    ai = a0 + (k2 * c0 - k1 * a0 * b0) * delta_t
    bi = b0 + (k2 * c0 - k1 * a0 * b0) * delta_t
    ci = c0 + (2 * k1 * a0 * b0 - 2 * k2 * c0) * delta_t

    a0 = ai
    b0 = bi
    c0 = ci

    array_a.append(ai)
    array_b.append(bi)
    array_c.append(ci)
    array_t.append(t)
   
    print("%12.2f %16.2f %15.2f %15.2f"%(t,ai,bi,ci))
    
plt.plot(array_t, array_a, label="a", color="Red")
plt.plot(array_t, array_b, label="b", color="green")
plt.plot(array_t, array_c, label="c", color="blue")

plt.legend()

plt.show()