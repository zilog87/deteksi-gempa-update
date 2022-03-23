import requests
from bs4 import BeautifulSoup

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
    try:
        content = requests.get('https://www.bmkg.go.id/', 'html.parser')
    except Exception:
            return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class' : 'waktu'})
        result = result.text.split(',')
        tanggal = result[0]
        waktu =  result[1]

        result = soup.find('div', {'class' : 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        ls = None
        bt = None
        koordinat = None
        lokasi = None
        dirasakan = None

        for res in result:
            print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu # '21:10:16 WIB'
        hasil['magnitudo'] = magnitudo # '4.5'
        hasil['kedalaman'] = kedalaman # '10 km'
        hasil['koordinat'] = {'ls' : ls, 'bt':bt}
        hasil['lokasi'] = lokasi # 'Pusat gempa berada di laut 37 km barat daya Sumur'
        hasil['dirasakan'] = dirasakan # 'Dirasakan (Skala MMI): III-IV Bayah, III-IV Pandeglang, II Anyer, II Lebak'

        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menemukan data gempa terkini")
        return

    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Koordinat: LS= {result['koordinat']['ls']}, BT= {result['koordinat']['bt']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Dirasakan {result['dirasakan']}")