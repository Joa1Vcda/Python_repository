"""Second Test(IMC)"""

name = "Joao Vitor"
height = 1.76
weight = 69.5
imc = weight / height**2

# print(name,'have',height,'of height,')
# print('your weight is',weight,'and your IMC is')
# print(imc)

"""formatation of strings(f-strings)"""

# print(f'{name} have {height:.2f} of height,')
# print(f'your weight is {weight} and your IMC is')
# print= (imc)

linha_1 = f"{name} have {height:.2f} of height,"
linha_2 = f"your weight is {weight:.3f} and your IMC is"
linha_3 = imc

# print(linha_1,linha_2,linha_3,sep='\r')
print(linha_1, linha_2, linha_3, sep=" ")

"""formatation of strings(format)"""

a = "A"
b = "B"
c = 1.1

string = "{} {} {:.2f} {}"
format_1 = string.format(a, b, c, 3)

print(format_1)
