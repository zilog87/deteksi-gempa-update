"""
Aplikasi deteksi gempa terkini
Modularisasi dengan function
"""


def ekstraksi_data():
    """
    Tanggal : 19 Maret 2022
    Waktu : 21:10:16 WIB
    Magnitudo : 4.5
    Kedalaman : 10 km
    Lokasi: LS=6.93 BT=105.37
    Pusat gempa berada di laut 37 km barat daya Sumur
    Dirasakan : Dirasakan (Skala MMI): III-IV Bayah, III-IV Pandeglang, II Anyer, II Lebak
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '19 Maret 2022'
    hasil['waktu'] = '21:10:16 WIB'
    hasil['magnitudo'] = '4.5'
    hasil['kedalaman'] = '10 km'
    hasil['lokasi'] = {'ls' : 6.93, 'bt':105.37}
    hasil['pusat'] = 'Pusat gempa berada di laut 37 km barat daya Sumur'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): III-IV Bayah, III-IV Pandeglang, II Anyer, II Lebak'

    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LS= {result['lokasi']['ls']}, BT= {result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")




if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)
