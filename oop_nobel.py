# év;     típus; keresztnév; vezetéknév
#  0        1        2           3
# 2017;  fizikai;  Rainer;     Weiss
class Nobel:
    def __init__(self,row):
        r = row.strip().split(';')
        self.év         = int(r[0])
        self.típus      =     r[1]
        self.keresztnév =     r[2]
        self.vezetéknév =     r[3]

with open ('nobel.csv','r',encoding='utf-8-sig') as f:
    fejlec = f.readline()
    matrix = [Nobel(sor) for sor in f]
    
#3. feladat 
for sor in matrix:
    if sor.keresztnév == 'Arthur B.' and sor.vezetéknév == 'McDonald':
        print(f'3. feladat: {sor.típus}')
        
#4. feladat
for sor in matrix:
    if sor.év == 2017 and sor.típus == 'irodalmi':
        print(f'4. feladat: {sor.keresztnév} {sor.vezetéknév}')
        
#5. feladat
print(        f'5. feladat:')
for sor in matrix:
    if sor.vezetéknév == '' and sor.típus == 'béke' and sor.év > 1989:
        print(f'        {sor.év}: {sor.keresztnév}')
        
#6. feladat
print(        f'6. feladat:')
for sor in matrix:
    if 'Curie' in sor.vezetéknév:
        print(f'        {sor.év}: {sor.keresztnév} {sor.vezetéknév} ({sor.típus})')
        
#7. feladat
print(        f'7. feladat:')
tip = []
for sor in matrix:
    tip.append(sor.típus)

tip_halmaz = set(tip)
for i in tip_halmaz:
    darab = tip.count(i)
    print(    f'        {i:22} {darab:3} db')
    
#8. feladat
print(        f'8. feladat: orvosi.txt')
with open ('orvosi.txt','w',encoding='utf-8') as f:
    matrix.sort(key=lambda x:x.év)
    for sor in matrix:
        if sor.típus == 'orvosi':
            print(sor.év,sor.keresztnév,sor.vezetéknév, file=f)