# GeneticAlgorithm
Implementasi mencari nilai maksimum f(x,y) 

## Formulasi Masalah
Menggunakan Genetic Algorithm untuk mencari nilai maksimal dari <br>
![Persamaan](https://latex.codecogs.com/gif.latex?%5Cbg_white%20f%28x%2Cy%29%20%3D%20cos%5C%2Cx%5E2%20*%20sin%5C%2Cy%5E2%20&plus;%20%28x%20&plus;%20y%29) <br>
Dengan nilai batas nilai -2 <= x <= 1 dan -1 <= y <= 1

## Skema Umum Genetic Algorithm
![image](https://user-images.githubusercontent.com/57952404/148376749-a7025dcb-7b72-4066-af22-9c6a72ee5114.png)

## Hal yang Diobservasi dan Dibangun
### 1. Desain Kromosom dan Metode Pengkodean
Desain kromosom sepanjang 16 kotak di mana kotak ke-1 sampai ke-8 adalah gen dari x dan kotak ke-9 sampai ke-16 adalah gen dari y. Metode pengkodan dengan representasi biner. <br>
![image](https://user-images.githubusercontent.com/57952404/148377246-9d00c71a-b694-4791-a70a-978c1488cd99.png)

### 2. Pemilihan (Seleksi) Orang Tua
Dengan Roulette Wheel <br>
![image](https://user-images.githubusercontent.com/57952404/148377356-17150550-1d9b-4af6-aa26-adaf40157bd2.png)

### 3. Crossover (Rekombinasi)
Representasi Biner di 2 titik, yaitu titik ke-5 dan titik ke-11 <br>
<b>Sebelum</b> <br>
![image](https://user-images.githubusercontent.com/57952404/148377597-b566a181-10dd-48b5-8a8b-9298da2c1d6e.png) <br>

<b>Setelah</b> <br>
![image](https://user-images.githubusercontent.com/57952404/148377662-dd61e3be-1250-4b66-a55f-aba2909de5a0.png)

### 4. Mutasi
Mutasi Representasi Biner dengan membalik nilai (0 menjadi 1, dan 1 menjadi 0) <br>
![image](https://user-images.githubusercontent.com/57952404/148378003-ce37ef17-52d8-4ac3-a7ca-2cc5c12508f5.png)

### 5. Seleksi Survivor
Generation Replacement dengan Elitism 2 individu terbaik

### 6. Terminasi (Penghentian Evolusi)
Dilakukan perulangan sampai ke-100 generasi

## Nilai Parameter (dalam tabel)
| Nama Parameter | Nilai |
| -- | -- |
| Desain Kromosom | Biner |
| Ukuran Populasi | 20 |
| Pemilihan Orang Tua | Roulette Wheel |
| Peluang Crossover | 70% |
| Peluang Mutasi | 2% |
| Seleksi Survivor | Generation Replacement Elitism 2 individu |
| Terminasi | Perulangan ke-100 |

## Hasil Akhir
![image](https://user-images.githubusercontent.com/57952404/148378904-5966c6e7-2e76-4cf1-8570-d30d43df3ad2.png)

## Lebih Lengkap
Ada pada file Laporan PDF dan Slide PPT

## Video Penjelasan
[Klik untuk melihat video](http://bit.ly/video_1301180469)
