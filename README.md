


# Vücut Kitle İndeksi (BMI) Hesaplayıcı

Bu proje, kullanıcıların vücut kitle indeksini (BMI) hesaplayabilecekleri bir GUI uygulaması sunmaktadır. Uygulama, kullanıcıdan kilo ve boy bilgilerini alır ve ardından bu bilgilere göre BMI hesaplar. Hesaplanan BMI'ya göre, kullanıcıya vücut tipi (Zayıf, Normal, Fazla Kilolu, Obez) hakkında bilgi verir.

### Özellikler:
- Kilo ve boy için kullanıcı dostu giriş alanları.
- Hatalı girişlerde kullanıcıyı bilgilendiren hata mesajları.
- Hesaplanan BMI değeri ve kullanıcıya uygun kategori (Zayıf, Normal, Fazla Kilolu, Obez) hakkında bilgilendirme.

### Kullanıcı Arayüzü:
- Modern ve şık bir GUI tasarımı.
- Kullanıcı dostu yerleşim ve metin düzenlemeleri.
- Arka planda görsel bir öğe kullanımı.

---

## Gereksinimler

Bu projeyi çalıştırabilmek için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

- **PIL** (Python Imaging Library)
- **Tkinter** (Python GUI kütüphanesi)

Bu kütüphaneleri yüklemek için şu komutları kullanabilirsiniz:

```bash
pip install pillow
```

**Tkinter** genellikle Python ile birlikte gelir, ancak yoksa sisteminize göre aşağıdaki komut ile yükleyebilirsiniz:

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

## Geliştirme

Bu projeyi geliştirirken veya katkı sağlarken aşağıdaki adımları izleyebilirsiniz:

1. Bu depoyu çatallayın (fork).
2. Yeni bir branch oluşturun (`git checkout -b feature-name`).
3. Yaptığınız değişiklikleri commit edin (`git commit -am 'Added new feature'`).
4. Branch'ınızı GitHub'da push edin (`git push origin feature-name`).
5. Bir pull request oluşturun.

---

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakabilirsiniz.

---

Bu README, projenizi GitHub'da paylaşırken kullanıcıların nasıl kurulum yapacakları ve kullanacakları hakkında bilgi sağlamanızı amaçlamaktadır. Eğer ek özellikler eklemeyi planlıyorsanız, buraya ek açıklamalar veya geliştirme rehberleri de ekleyebilirsiniz.

