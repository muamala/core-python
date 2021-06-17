"""
Tipe data dictionary sekedar menghubungkan antara key dan value
(KVP = Key Value Pair)
"""

kamus_ind_eng = {'anak': 'child', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print(kamus_ind_eng)
print(kamus_ind_eng['anak'])
print(kamus_ind_eng['istri'])
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('Data ini dikirimkan oleh server Gojek untuk memberikan info driver di sekitar pemakai aplikasi')
data_gojek = {
    'tanggal': '2021/06/17',
    'driver_list': [{'nama': 'Eko', 'jarak': 10},
                    {'nama': 'Dwi', 'jarak': 30},
                    {'nama': 'Catur', 'jarak': 100},
                    {'nama': 'Tri', 'jarak': 1000}
                    ]
}
print(data_gojek)
print(f"Driver di sekitar sini: {data_gojek['driver_list'][0]}")
print(f"Driver di sekitar sini: {data_gojek['driver_list'][3]}")
print(f"Jarak driver 1{data_gojek['driver_list'][0]['jarak']} meter")
