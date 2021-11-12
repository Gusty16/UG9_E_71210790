a = 1 #angka awal
r = 3 #rasio
n = 11 #suku yang dituju
rs = a*(r**(n-1)) #rumus
for n in range(1,12):
    s = 1*(3**(n-1))
    print(s)
print ("jadi jumlah suku ke-11 dari deret 1,3,9,27,81,...! adalah =",rs)
