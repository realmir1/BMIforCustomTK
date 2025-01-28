


# Vücut Kitle İndeksi (BMI) Hesaplayıcı

Bu proje, kullanıcıların vücut kitle indeksini (BMI) hesaplayabilecekleri bir GUI uygulaması sunmaktadır. Uygulama, kullanıcıdan kilo ve boy bilgilerini alır ve ardından bu bilgilere göre BMI hesaplar. Hesaplanan BMI'ya göre, kullanıcıya vücut tipi (Zayıf, Normal, Fazla Kilolu, Obez) hakkında bilgi verir. 

## Yazılım ve Kütüphaneler

### Kullanılan Yazılım:

Bu proje Python programlama dili ile geliştirilmiştir.
<br>
<p align="center"> <img src="https://robokodlama.com/wp-content/uploads/2022/09/Python.svg_.png" width=200, height=200></p>

### Geliştirildiği Ortam:



Bu proje Visual Studio Code ortamında geliştirildi.

<br>
<p align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/2048px-Visual_Studio_Code_1.35_icon.svg.png" width=200, height=200></p>


### Kullanılan Kütüphaneler:


- Custom Tkinter <img src="https://styles.redditmedia.com/t5_8tx64t/styles/communityIcon_kbz7e49k7obb1.png" width="35" align="left">
<br>


- PIL<img src="https://python-pillow.github.io/assets/images/pillow-logo-248x250.png" width="35" align="left">
<br>

- Tkinter <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiI0t0Y9CTxpGbvzomIpNd5bb4e-8lny0qrPJLBygCDMTNroCdk7FH9icIGwHPO7-SdPYBZWnvs7-I7aSf1F03kmFlFsCMdKNBMFd7B8_VGkxMQgKYhYHXJy76TxjdJERo_tNuoxkn3QgU/s200/tkinter-pluma.png" width="35" align="left">
<br>

- itertools <img src="https://mblogthumb-phinf.pstatic.net/MjAyMjA5MjFfMjAy/MDAxNjYzNzQ1MDYyMjcx.z7s3EiUTtxU1b2QJKhm5vb-hjrnY0GEhbXBaM0T8JXwg.UVRvOE9qXushbX1qU73LYz7JTHSCsz7LWbRoknhKQM4g.PNG.dldudcks1779/Python.png?type=w800" width="35" align="left">
<br>




### Özellikler:
- Kilo ve boy için kullanıcı dostu giriş alanları.
- Hatalı girişlerde kullanıcıyı bilgilendiren hata mesajları.
- Hesaplanan BMI değeri ve kullanıcıya uygun kategori (Zayıf, Normal, Fazla Kilolu, Obez) hakkında bilgilendirme.

### Kullanıcı Arayüzü:
- Modern ve şık bir GUI tasarımı.
- Kullanıcı dostu yerleşim ve metin düzenlemeleri.
- Arka planda görsel bir öğe kullanımı.

### Arayüz Görüntüsü:

<p align="center"> <img src="https://github.com/realmir1/BMIforCustomTK/blob/main/Ekran%20Resmi%202025-01-28%2013.08.31.png?raw=true" width=600, height=700></p>

---

## Gereksinimler

- **Windows**: Tkinter genellikle Python ile birlikte gelir.
- **macOS/Linux**: Tkinter yüklemek için `brew install python-tk` veya sisteminizin paket yöneticisini kullanabilirsiniz.

---

## Kullanım

Projeyi çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. Proje dosyasını bilgisayarınıza indirin.
2. Uygulama dosyasını bir Python ortamında çalıştırın.

```bash
python app.py
```

Uygulama açıldığında, aşağıdaki adımları izleyebilirsiniz:

1. Kilonuzu (kg) ve boyunuzu (m) girin.
2. "BMI Hesapla" butonuna tıklayın.
3. BMI değeri hesaplanacak ve uygun kategori (Zayıf, Normal, Fazla Kilolu, Obez) hakkında bilgi mesajı görüntülenecektir.

---

## Kod Açıklamaları

**`hesapla()` Fonksiyonu:**
- Kullanıcıdan alınan kilo ve boy bilgileri ile BMI hesaplanır.
- Hatalı girişler için hata mesajı gösterilir.
- Hesaplanan BMI değeri, uygun kategorilerle birlikte bir bilgi mesajı olarak gösterilir.

**Tkinter ile GUI Oluşturma:**
- Kullanıcı arayüzü için `CTk` (Custom Tkinter) kullanılmıştır.
- Giriş alanları (`CTkEntry`) ve butonlar (`CTkButton`) kullanılarak şık bir GUI tasarlanmıştır.
- Arka plan resmi ve metin renkleri özelleştirilmiştir.

---





