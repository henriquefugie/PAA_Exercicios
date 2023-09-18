def climbStairs(n, kmax):
    if n==1:
        soma = 1
        return soma
    elif n==2:
        soma = n
        return soma
    elif n==3:
        soma = n + 1
        return soma
    else:
        for i in range(0, n, 1):
            soma = 0
            for k in range(0, kmax, 1):
                if (i - k) > 0:
                    soma = soma + climbStairs(i-k, kmax)
        return soma 

valor = climbStairs(5, 3)
print(valor)
