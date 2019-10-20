from datetime import datetime, date, timedelta
import math
import operator

biayaSUV = float(25000)
biayaMPV = float(35000)


class Mobil:
    def __init__(self, plat, warna, tipe, dateTime, tempatParkir, didalam, dateTimeK):
        self.plat = plat
        self.warna = warna
        self.tipe = tipe
        self.dateTime = dateTime
        self.tempatParkir = tempatParkir
        self.didalam = didalam
        self.dateTimeK = dateTimeK

class PL:
    def __init__(self, avl, nopl):
        self.avl=avl
        self.nopl=nopl



parkingLotArr = [
    Mobil('B 1 ABC', 'Hitam', 'SUV', datetime(year=2019, month=10, day=19, hour=0, minute=55, second=13), 1, False,
          datetime(year=2019, month=10, day=19, hour=3, minute=55, second=13)),
    Mobil('RI 1', 'Hitam', 'MPV', datetime(year=2019, month=10, day=19, hour=5, minute=55, second=13), 2, True, 0),
    Mobil('B 2 DEF', 'Putih', 'MPV', datetime(year=2019, month=10, day=19, hour=8, minute=55, second=13), 3, True, 0)]
parkingLotAvlArr = []

irt=0
while (irt < 30):
    if (irt<=len(parkingLotArr)-1 and parkingLotArr[irt].didalam == True):
        parkingLotAvlArr.append(PL(1,irt))
    else:
        parkingLotAvlArr.append(PL(0,irt))
    sortedAvlArr = sorted(parkingLotAvlArr, key=lambda x: x.avl, reverse=True)
    #print('no pl: ',parkingLotAvlArr[irt].nopl,' avl: ',parkingLotAvlArr[irt].avl)
    #print(sortedAvlArr[irt].nopl)
    #print(parkingLotAvlArr[irt].avl)
    irt = irt + 1
sortedAvlArr = sorted(parkingLotAvlArr, key=lambda x: x.avl, reverse=True)

s = ' '
ps = ' '
pla = 0
while (s != 'end'):
    print('Input "m" untuk Kendaraan Masuk')
    print('Input "k" untuk Kendaraan Keluar')
    print('Inpur "p" untuk Print Report')
    print('Input "end" untuk keluar dari program')
    #sortedAvlArr.sort(key=lambda x: x.avl, reverse=True)
    s = input(':')
    if (s != 'end'):
        if (s == 'm'):
            p = input('Input Plat Nomor Kendaraan: ')
            w = input('Input Warna Kendaraan: ')
            t = input('Input Tipe Kendaraan ("SUV" / "MPV"): ')
            d = datetime.now()
            tmp = len(parkingLotArr) + 1
            parkingLotArr.append(Mobil(p, w, t, d, tmp, True, 0))
            print('')
            print('==========TIKET==========')
            print('-------------------------')
            print('Plat Nomor Kendaraan: ', parkingLotArr[len(parkingLotArr) - 1].plat)
            inw=0
            while(inw<len(parkingLotAvlArr)-1 and parkingLotAvlArr[inw].avl!=0):
                inw=inw+1
            #print(len(parkingLotAvlArr))
            #print(inw)
            print('Nomor Parking Lot: ', parkingLotAvlArr[inw].nopl+1)
            print('Tanggal dan Waktu Masuk: ', d)
            print(' ')
            print('-------------------------')
            parkingLotAvlArr[inw].avl=1
        elif (s == 'k'):
            klr = input('Nomor Parking Lot: ')
            print('=======Tiket Keluar=======')
            print('-------------------------')
            print('Plat Nomor Kendaraan: ', parkingLotArr[int(klr) - 1].plat)
            print('Nomor Parking Lot: ', klr)
            print('Tipe Kendaraan: ', parkingLotArr[int(klr) - 1].tipe)
            know = datetime.now()
            print('Tanggal dan Waktu Masuk: ', parkingLotArr[int(klr) - 1].dateTime)
            print('Tanggal dan Waktu Keluar: ', know)
            print('-------------------------')
            print(' ')
            fehu=0
            while(fehu<=len(sortedAvlArr) and sortedAvlArr[fehu].nopl!=int(klr)-1):
                fehu=fehu+1
            sortedAvlArr[fehu].avl=0
            print('-------------------------')
            timeDelta = know - parkingLotArr[int(klr) - 1].dateTime
            if (parkingLotArr[int(klr) - 1].tipe == 'SUV'):
                if (timeDelta.total_seconds() // 3600 > 1):
                    hour = math.ceil(float(timeDelta.total_seconds()) / 3600) + 1.0
                    total = biayaMPV + (hour * (biayaMPV * 20 / 100))
                else:
                    total = biayaSUV
            elif (parkingLotArr[int(klr) - 1].tipe == 'MPV'):
                if (timeDelta.total_seconds() // 3600 > 1):
                    hour = math.ceil(float(timeDelta.total_seconds()) / 3600) + 1.0
                    total = biayaMPV + (hour * (biayaMPV * 20 / 100))
                else:
                    total = biayaMPV
            print('Biaya Parkir: ', total)
            print(' ')
            print('-------------------------')
            #print(timeDelta.total_seconds())
            parkingLotArr[int(klr) - 1].didalam = False
            parkingLotArr[int(klr) - 1].dateTimeK = know
        elif (s == 'p'):
            ps = ' '
            print('=========Report==========')
            print('-------------------------')
            while (ps != 'b'):
                ktm = 0
                print('Menu :')
                print('Input "t" untuk print report berdasarkan tipe mobil')
                print('Input "w" untuk print report berdasarkan warna mobil')
                print('Input "d" untuk print report kendaraan didalam tempat parkir')
                print('Input "dl" untuk print report kendaraan yang sudah keluar tempat parkir')
                print('Input "a" untuk print report semua kendaraan')
                print('Input "u" untuk print unavailable parking spot')
                print('Input "av" untuk print unavailable parking spot')
                print('Input "b" untuk kembali')
                print('-------------------------')
                ps = input(':')
                if (ps == 't'):
                    i = 0
                    vt = input('"SUV" / "MPV": ')
                    if (vt == 'SUV'):
                        while (i < len(parkingLotArr)):
                            if (parkingLotArr[int(klr) - 1].tipe == 'SUV'):
                                print('Tipe Kendaraan: ', parkingLotArr[i].tipe)
                                print('Plat Nomor Kendaraan: ', parkingLotArr[i].plat)
                                print('Warna Kendaraan: ', parkingLotArr[i].warna)
                                print('Waktu Masuk: ', parkingLotArr[i].dateTime)
                                if (parkingLotArr[i].didalam == True):
                                    print('Waktu Keluar: Kendaraan Masih Didalam Tempat Parkir')
                                else:
                                    print('Waktu Keluar: ', parkingLotArr[i].dateTimeK)
                                ktm = ktm + 1
                                print('-------------------------')
                            i = i + 1
                    elif (vt == 'MPV'):
                        while (i < len(parkingLotArr)):
                            if (parkingLotArr[i].tipe == 'MPV'):
                                print('Tipe Kendaraan: ', parkingLotArr[i].tipe)
                                print('Plat Nomor Kendaraan: ', parkingLotArr[i].plat)
                                print('Warna Kendaraan: ', parkingLotArr[i].warna)
                                print('Waktu Masuk: ', parkingLotArr[i].dateTime)
                                if (parkingLotArr[i].didalam == True):
                                    print('Waktu Keluar: Kendaraan Masih Didalam Tempat Parkir')
                                else:
                                    print('Waktu Keluar: ', parkingLotArr[i].dateTimeK)
                                ktm = ktm + 1
                                print('-------------------------')
                            i = i + 1
                    print('Jumlah Kendaraan: ', ktm)
                    print('-------------------------')
                elif (ps == 'w'):
                    i = 0
                    wrn = input('Input Warna Mobil: ')
                    ktm = 0
                    while (i < len(parkingLotArr)):
                        if (parkingLotArr[i].warna == wrn):
                            print('Tipe Kendaraan: ', parkingLotArr[i].tipe)
                            print('Plat Nomor Kendaraan: ', parkingLotArr[i].plat)
                            print('Warna Kendaraan: ', parkingLotArr[i].warna)
                            print('Waktu Masuk: ', parkingLotArr[i].dateTime)
                            if (parkingLotArr[i].didalam == True):
                                print('Waktu Keluar: Kendaraan Masih Didalam Tempat Parkir')
                            else:
                                print('Waktu Keluar: ', parkingLotArr[i].dateTimeK)
                            ktm = ktm + 1
                            print('-------------------------')
                        i = i + 1
                    if (ktm == 0):
                        print('Mobil Berwarna "', wrn, '" tidak ditemukan')
                    print('Jumlah Kendaraan: ', ktm)
                    print('-------------------------')
                elif (ps == 'd'):
                    i = 0
                    while (i < len(parkingLotArr)):
                        if (parkingLotArr[i].didalam == True):
                            print('Tipe Kendaraan: ', parkingLotArr[i].tipe)
                            print('Plat Nomor Kendaraan: ', parkingLotArr[i].plat)
                            print('Warna Kendaraan: ', parkingLotArr[i].warna)
                            print('Waktu Masuk: ', parkingLotArr[i].dateTime)
                            if (parkingLotArr[i].didalam == True):
                                print('Waktu Keluar: Kendaraan Masih Didalam Tempat Parkir')
                            else:
                                print('Waktu Keluar: ', parkingLotArr[i].dateTimeK)
                            ktm = ktm + 1
                            print('-------------------------')
                        i = i + 1
                    if (ktm == 0):
                        print('Tidak ada mobil didalam tempat parkir')
                    print('Jumlah Kendaraan: ', ktm)
                    print('-------------------------')
                elif (ps == 'dl'):
                    i = 0
                    while (i < len(parkingLotArr)):
                        if (parkingLotArr[i].didalam == False):
                            print('Tipe Kendaraan: ', parkingLotArr[i].tipe)
                            print('Plat Nomor Kendaraan: ', parkingLotArr[i].plat)
                            print('Warna Kendaraan: ', parkingLotArr[i].warna)
                            print('Waktu Masuk: ', parkingLotArr[i].dateTime)
                            timeDelta = parkingLotArr[i].dateTimeK - parkingLotArr[i].dateTime
                            if (parkingLotArr[i].tipe == 'SUV'):
                                if (timeDelta.total_seconds() // 3600 > 1):
                                    hour = math.ceil(float(timeDelta.total_seconds()) / 3600) + 1.0
                                    totalk = biayaMPV + (hour * (biayaMPV * 20 / 100))
                                else:
                                    totalk = biayaSUV
                            elif (parkingLotArr[i].tipe == 'MPV'):
                                if (timeDelta.total_seconds() // 3600 > 1):
                                    hour = math.ceil(float(timeDelta.total_seconds()) / 3600) + 1.0
                                    totalk = biayaMPV + (hour * (biayaMPV * 20 / 100))
                                else:
                                    totalk = biayaMPV
                        if (parkingLotArr[i].didalam == True):
                            print('Waktu Keluar: Kendaraan Masih Didalam Tempat Parkir')
                        else:
                            print('Waktu Keluar: ', parkingLotArr[i].dateTimeK)
                            print('Jumlah Biaya: ', totalk)
                        ktm = ktm + 1
                        print('-------------------------')
                        i = i + 1
                    if (ktm == 0):
                        print('Semua mobil masih didalam')
                    print('Jumlah Kendaraan: ', ktm)
                    print('-------------------------')
                elif (ps == 'a'):
                    i = 0
                    while (i < len(parkingLotArr)):
                        print('Tipe Kendaraan: ', parkingLotArr[i].tipe)
                        print('Plat Nomor Kendaraan: ', parkingLotArr[i].plat)
                        print('Warna Kendaraan: ', parkingLotArr[i].warna)
                        print('Waktu Masuk: ', parkingLotArr[i].dateTime)
                        if (parkingLotArr[i].didalam == True):
                            print('Waktu Keluar: Kendaraan Masih Didalam Tempat Parkir')
                        else:
                            print('Waktu Keluar: ', parkingLotArr[i].dateTimeK)
                            #print('-------------------------')
                            #print('Jumlah Kendaraan: ', i + 1)
                            #print('-------------------------')
                        print('-------------------------')
                        i = i + 1
                elif (ps =='u'):
                    i=0
                    count=0
                    while (i < len(sortedAvlArr)):
                        if(sortedAvlArr[i].avl==1):
                            print('Parking Spot Unavailable: A',sortedAvlArr[i].nopl+1)
                            print('-------------------------')
                            print(' ')
                            count=count+1
                        i = i + 1
                elif (ps == 'av'):
                    i = 0
                    while (i < len(sortedAvlArr)):
                        if (sortedAvlArr[i].avl == 0):
                            print('Parking Spot Available: A',sortedAvlArr[i].nopl+1)
                            print('-------------------------')
                            print(' ')
                        i = i + 1
            print('-------------------------')
