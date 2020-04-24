# év;     típus; keresztnév; vezetéknév
#  0        1        2           3
# 2017;  fizikai;  Rainer;     Weiss
import sqlite3, pprint
con =  sqlite3.connect('nobel.db')
c   =  con.cursor()

c.execute("DROP TABLE IF EXISTS tabla")
c.execute('''
        CREATE TABLE IF NOT EXISTS tabla
        (év INTEGER,
         típus TEXT,
         keresztnév TEXT,
         vezetéknév TEXT)
         ''')
con.commit()

with open ('nobel.csv','r',encoding='utf-8-sig') as f:
    fejlec = f.readline()
    for sor in f:
        év, típus, keresztnév, vezetéknév = sor.strip().split(';')
        c.execute("INSERT INTO tabla VALUES(?,?,?,?)",(év,típus,keresztnév,vezetéknév))
con.commit()

#3. feladat 
c.execute("SELECT típus FROM tabla WHERE keresztnév LIKE 'Arthur B.' AND vezetéknév LIKE 'McDonald'")
típus = c.fetchall()[0][0]
print(f'3. feladat: {típus}')
        
#4. feladat
c.execute("SELECT keresztnév,vezetéknév FROM tabla WHERE év == 2017 AND típus LIKE 'irodalmi'")
keresztnév,vezetéknév = c.fetchall()[0]
print(f'4. feladat: {keresztnév} {vezetéknév}')
        
#5. feladat
print(        f'5. feladat:')
c.execute("SELECT év,keresztnév FROM tabla WHERE év > 1989 AND típus LIKE 'béke' AND vezetéknév LIKE ''")
adat = c.fetchall()
for év,szervezet in adat:
    print(    f'       {év} {szervezet}')
        
#6. feladat
print(        f'6. feladat:')
c.execute("SELECT év,keresztnév,vezetéknév,típus FROM tabla WHERE vezetéknév LIKE '%Curie%'")
adat = c.fetchall()
for év,keresztnév,vezetéknév,típus in adat:
    print(    f'       {év} {keresztnév} {vezetéknév} {típus}')
        
#7. feladat
print(        f'7. feladat:')
c.execute("SELECT típus,COUNT(típus) FROM tabla GROUP BY típus")
adat = c.fetchall()
for típus,darab in adat:
    print(    f'       {típus:22} {darab:3} db')

    
#8. feladat
print(f'8. feladat: orvosi.txt')
c.execute("SELECT év,keresztnév,vezetéknév FROM tabla WHERE típus LIKE 'orvosi' ORDER BY év ASC")
adat = c.fetchall()
with open ('orvosi.txt','w',encoding='utf-8') as f:
    for év,keresztnév,vezetéknév in adat:
            print(f'{év}:{keresztnév} {vezetéknév}',file=f)

con.commit()
con.close()