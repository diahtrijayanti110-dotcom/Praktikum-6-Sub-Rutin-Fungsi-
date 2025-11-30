import math

# Fungsi a(x) → lambda
a = lambda x: x**2

# Fungsi b(x, y) → lambda
b = lambda x, y: math.sqrt(x**2 + y**2)

# Fungsi c(*args) → lambda
c = lambda *args: sum(args) / len(args)

# Fungsi d(s) → lambda
d = lambda s: "".join(set(s))


# ===============================
# Contoh penggunaan masing-masing
# ===============================

print("a(5) =", a(5))                     # 5^2 = 25
print("b(3, 4) =", b(3, 4))               # sqrt(3² + 4²) = 5
print("c(2, 4, 6) =", c(2, 4, 6))         # rata-rata = 4
print("d('hello') =", d("hello"))         # kombinasi huruf unik
