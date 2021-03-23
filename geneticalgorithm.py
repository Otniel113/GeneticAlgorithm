import math
import random

#=====================FUNGSI-FUNGSI UTAMA=====================

#1. Decode Kromosom
def binaryDecodeToReal_X(indv):
    #Decode 8 kotak pertama dari biner menjadi nilai X berupa bil. real
    yang_dibagi = 0
    pembagi = 0
    for i in range (0, 8):
        dua_pangkat = 2 ** (-1 * (i+1))
        yang_dibagi += indv[i] * dua_pangkat
        pembagi += dua_pangkat

    return -1 + (((2 - (-1))/pembagi) * yang_dibagi)

def binaryDecodeToReal_Y(indv):
    #Decode 8 kotak terakhir dari biner menjadi nilai Y berupa bil. real
    yang_dibagi = 0
    pembagi = 0
    for i in range (0, 8):
        dua_pangkat = 2 ** (-1 * (i+1))
        yang_dibagi += indv[i+8] * dua_pangkat
        pembagi += dua_pangkat

    return -1 + (((1 - (-1))/pembagi) * yang_dibagi)

#2. Perhitungan Fitness
def hitungFitness(x,y):
    #Maksimasi
    return (math.cos(x) ** 2) * (math.sin(y) ** 2) + (x + y)

#3. Pemilihan Orang Tua
def parentSelection(populasi_fitness):
    #Dengan Roullete Wheel
    total_fitness = 0
    for i in range (0, len(populasi_fitness)):
        total_fitness += populasi_fitness[i]

    roullete = random.uniform(0, total_fitness)

    for i in range (0, len(populasi_fitness)):
        roullete -= populasi_fitness[i]
        if (roullete <= 0):
            return i

#4. CrossOver
def crossOver(kromosom1, kromosom2):
    #Rekombinasi Biner di 2 titik, yaitu di 5 dan 11
    rekombinasi_1 = []
    rekombinasi_2 = []
    if (mesinGacha(70)):    #Peluang CrossOver 70%
        for i in range(0, 16):
            if (5 <= i <= 11):
                rekombinasi_1.append(kromosom2[i])
                rekombinasi_2.append(kromosom1[i])
            else:
                rekombinasi_1.append(kromosom1[i])
                rekombinasi_2.append(kromosom2[i])
    else:
        for i in range(0, 16):
            rekombinasi_1.append(kromosom1[i])
            rekombinasi_2.append(kromosom2[i])

    return rekombinasi_1, rekombinasi_2

#5. Mutasi
def mutasi(anak):
    #Mutasi Biner 0 --> 1 dan 1 --> 0
    hasil_mutan = []
    if (mesinGacha(2)):     #Peluang Mutasi 2%
        gen = random.randint(0, len(anak))
        for i in range(0, len(anak)):
            if (i == gen):
                if (anak[i] == 1):
                    hasil_mutan.append(0)
                else:
                    hasil_mutan.append(1)
            else:
                hasil_mutan.append(anak[i])
    else:
        for i in range(0, len(anak)):
            hasil_mutan.append(anak[i])
    
    return hasil_mutan

#6. Pergantian Generasi
def survivorSelection(populasi_fitness):
    #Ambil 2 individu dengan nilai fitness terbaik (elitism)
    maks = 0
    for i in range(0, len(populasi_fitness)):
        if (populasi_fitness[i] >= maks):
            maks = populasi_fitness[i]
            elit1 = i

    maks = 0
    for i in range(0, len(populasi_fitness)):
        if ((populasi_fitness[i] >= maks) and (i != elit1)):
            maks = populasi_fitness[i]
            elit2 = i

    return elit1, elit2

#=====================FUNGSI-FUNGSI PEMBANTU=====================

def createRandomIndividu():
    #Membuat kromosom individu dengan 16 gen yang masing-masing berupa biner
    indv = []
    for i in range(0,16):
        indv.append(random.randint(0,1))
    return indv

def createPopulasi():
    #Menciptakan populasi awal sebanyak 20
    populasi_kromosom = []
    populasi_fitness = []
    for i in range (0,20):
        while True: #Menjamin nilai fitness tidak negatif
            indv = createRandomIndividu()

            x = binaryDecodeToReal_X(indv)
            y = binaryDecodeToReal_Y(indv)

            nilai_fitness = hitungFitness(x,y)
            if (nilai_fitness >= 0):
                populasi_fitness.append(nilai_fitness)
                populasi_kromosom.append(indv)
                break

    return populasi_kromosom, populasi_fitness

def mesinGacha(peluang):
    #Menentukan apakah bisa masuk ke peluang atau tidak
    gacha = random.randint(1,100)
    if (1 <= gacha <= peluang):
        return True
    else:
        return False


#=====================PROGRAM UTAMA=====================
#Membuat 2 array populasi, yang 1 menampung kromosomnya dan 1 lagi menampung nilai fitnessnya
populasi_kromosom, populasi_fitness = createPopulasi()

for i in range(1, 100): #Dihentikan sampai generasi ke-100
    #Menampung generasi berikutnya
    next_fitness = [] 
    next_kromosom = []  

    #Pembuatan generasi berikutnya
    while (len(next_kromosom) < 18):
        #Parent Selection
        parent1 = parentSelection(populasi_fitness)
        parent2 = parentSelection(populasi_fitness)
        
        #CrossOver
        anak1, anak2 = crossOver(populasi_kromosom[parent1], populasi_kromosom[parent2])
        
        #Mutasi
        anak1 = mutasi(anak1)
        anak2 = mutasi(anak2)
        
        #Memasukkan ke bakal generasi berikutnya (untuk kromosomnya)
        next_kromosom.append(anak1)
        next_kromosom.append(anak2)

        #Memasukkan ke bakal generasi berikutnya (untuk nilai fitnessnya)
        #Anak1
        x = binaryDecodeToReal_X(anak1)
        y = binaryDecodeToReal_Y(anak1)
        nilai_fitness = hitungFitness(x,y)
        if (nilai_fitness >= 0):    #Menjamin nilai fitness tidak negatif
            next_fitness.append(nilai_fitness)
        else:
            next_fitness.append(0)

        #Anak2
        x = binaryDecodeToReal_X(anak2)
        y = binaryDecodeToReal_Y(anak2)
        nilai_fitness = hitungFitness(x,y)
        if (nilai_fitness >= 0):
            next_fitness.append(nilai_fitness)
        else:
            next_fitness.append(0)

    #SurvivorSelection dengan Generation Replacement Elitism
    elit1, elit2 = survivorSelection(populasi_fitness)

    #Memasukkan nilai Fitnessnya
    next_fitness.append(populasi_fitness[elit1])
    next_fitness.append(populasi_fitness[elit2])

    #Memasukkan Kromosomnya
    next_kromosom.append(populasi_kromosom[elit1])
    next_kromosom.append(populasi_kromosom[elit2])

    #Mengganti generasi yang lama dengan generasi berikutnya
    populasi_fitness.clear()
    populasi_fitness = next_fitness

    populasi_kromosom.clear()
    populasi_kromosom = next_kromosom

#Pemilihan individu terbaik sebagai solusi akhir
elit1, elit2 = survivorSelection(populasi_fitness)
x = binaryDecodeToReal_X(populasi_kromosom[elit1])
y = binaryDecodeToReal_Y(populasi_kromosom[elit1])

print("Kromosom terbaik adalah : ")
print(populasi_kromosom[elit1])
print("\nDengan hasil decode x = ", x, " dan y = ", y)
print("Yang menghasilkan nilai maksimasi, yaitu ", hitungFitness(x,y))