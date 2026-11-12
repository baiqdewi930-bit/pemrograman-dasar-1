#operator
#operator aritmatika
a = 12
b = 5
c = 3
penjumlahan = a + b + c
sisabagi = a % b
perkalian = a * b
pembagian = a / c
pengurangan = a - c
perpangkatan = a ** b
pembagian_bulat = c // a
print(f"hasil penjualan {a} + {b} + {c} = {penjumlahan}")
print(f"sisa bagi {a} mod {b} = {sisabagi}") 
print(f"perkalian {a} * {b} {perkalian}")
print(f"pembagian {a} / {c} = {pembagian}") 
print(f"pengurangan {a} - {c} = {pengurangan}")
print(f"hasil perpangkatan {a} ** {b} ** {c} = {perpangkatan}")
print(f"hasil pembagian_bulat {c} // {a} = {pembagian_bulat}")

#Operator assigment

a += 2  # 9
a **= 2 # a = 9 ** 2
print (a)

#operator perbandingan
perbandingan = a >= b #144 >= 2 True

x = 3
y = 2
banding = x <= y #false

print (x != y)
print (perbandingan)

#operator logika AND
opAnd = a >= b and x <= y and x != y
opOr = banding or banding or x != y
opNot = not opOr
opNot = not opAnd
print(opAnd)
print(opOr)
print(opNot)