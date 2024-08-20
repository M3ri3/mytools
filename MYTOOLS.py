from mpmath import mp

# Define a precisão desejada (em dígitos decimais)
mp.dps = 102  # 100 casas decimais + 2 casas para a parte inteira "3."
pi_value = str(mp.pi)
PI_INT = pi_value[2:102]

"print(PI_INT)"
# Define a precisão desejada (em dígitos decimais)
mp.dps = 102  # 100 casas decimais + 2 casas para a parte inteira "2."
e_value = str(mp.e)
E_INT = e_value[2:102]


"print(E_INT)"

def pi_real(N):
    if N> 0 and  N<=100:
        PI_INT = pi_value[2:N+2]
        return f"3,{PI_INT}"
    else:
        return "número fora do intervalo"
    
def e_real(N):
    if N> 0 and  N<=100:
        E_INT = e_value[2:N+2]
        return f"2,{E_INT}"
    else:
        return "número fora do intervalo"
    
'print(pi_real(5))'
'print(e_real(4))'
