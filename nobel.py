# év;     típus; keresztnév; vezetéknév
#  0        1        2           3
# 2017;  fizikai;  Rainer;     Weiss
with open ('nobel.csv','r',encoding='utf-8-sig') as f:
    fejlec = f.readline()
    matrix = [sor.strip().split(';') for sor in f]
    
#3. feladat 
for sor in matrix:
    if sor[2] == 'Arthur B.' and sor[3] == 'McDonald':
        print(f'3. feladat: {sor[1]}')
        
#4. feladat
for sor in matrix:
    if sor[0] == '2017' and sor[1] == 'irodalmi':
        print(f'4. feladat: {sor[2]} {sor[3]}')
        
#5. feladat
print(        f'5. feladat:')
for sor in matrix:
    if sor[3] == '' and sor[1] == 'béke' and sor[0] > '1989':
        print(f'        {sor[0]}: {sor[2]}')
        
#6. feladat
print(        f'6. feladat:')
for sor in matrix:
    if 'Curie' in sor[3]:
        print(f'        {sor[0]}: {sor[2]} {sor[3]} ({sor[1]})')
        
#7. feladat
print(        f'7. feladat:')
tip = []
for sor in matrix:
    tip.append(sor[1])

tip_halmaz = set(tip)
for i in tip_halmaz:
    darab = tip.count(i)
    print(    f'        {i:22} {darab:3} db')
    
#8. feladat
print(        f'8. feladat: orvosi.txt')
with open ('orvosi.txt','w',encoding='utf-8') as f:
    matrix.sort()
    for sor in matrix:
        if sor[1] == 'orvosi':
            print(sor[0],sor[2],sor[3], file=f)