a , b = 1, 1

fibonacci_seri = [a, b]

while len(fibonacci_seri) < 20:

    yeni_sayi = a + b

    fibonacci_seri.append(yeni_sayi)

    a, b = b, yeni_sayi

print(fibonacci_seri)