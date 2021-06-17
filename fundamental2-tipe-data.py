#tipe data skalar (sederhana)
anak1 = 'Eko'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'Catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

#tipe data list (array)
anak = ['Eko', 'Dwi', 'Catur', 'Tri']
print(anak)
anak.append('Limo')
print(anak)

print('\nsapa anak ke-2')
print(f'Hai {anak[1]}!')

print('\nsapa semua anak')
for a in anak:
    print(f'Hai {a}!')

print('\nSapa semua anak cara ribet')
for a in range(0, len(anak)):
    print(f'Hai {anak[a]}!')