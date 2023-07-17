def Fact(n):
   if n <= 1:
      return 1
   return n * Fact(n - 1)

for n in range(0, 21):
    print(f'Factorial({n}) = {Fact(n)}')
