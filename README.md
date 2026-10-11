# ag-kesif-ve-zafiyet-raporlama
Yapılan ağ keşif taramalarının otomatik olarak analiz edilmesi daha sonra tespit edilen açık portların ve servis versiyonlarının CVE veritabanıyla karşılaştırılarak risk skorunun hesaplanması, hesaplanan sonuçların ise Türkçe PDF rapor ile web tabanlı dashboard aracılığıyla sunulması amaçlanmaktadır. Bu proje bitirme projesidir. 

# Önemli
-projeyi çalıştırmadan önce tarama.py dosyasındaki kodlarda metasploit ip kısmına hedef metasploitable2 sanal makinesinin ip si, ve dosya yolu yazılmalıdır. 
-projede kullanılan dejavu fonts 2.37 dosyaları ve nvdcve-2.0-2022(2023,2024,2025,2026).json dosyaları boyutları nedeniyle depoya eklenememiştir. doğru sonuçlar için bu dosyaların eklenmesi gerekmektedir.

# Eksikler
şu anki durumunda versiyon bilgisi tespit edilemeyen servisler için CVE eşleştirmesi yerel veritabanındaki servis adı bazında gerçekleştirilmektedir. Bu durum sistemin hatalı veri vermesine sebep olabilir.

### Uyarı ve Sorumluluk Reddi
Bu proje eğitim ve test amaçlı geliştirilmiştir. Gerçek sistemlerde veya üretim ağlarında, uygun yetkilendirme ve gerekli güvenlik önlemleri olmadan kullanılması önerilmez. İzinsiz ağ taramaları hizmet kesintilerine, güvenlik ihlallerine veya hukuki sonuçlara yol açabilir.
Testler yalnızca size ait olan veya açıkça tarama izniniz bulunan sistemlerde, kontrollü bir laboratuvar ortamında gerçekleştirilmelidir.
Bu projenin geliştiricisi, yetkisiz veya uygunsuz kullanım sonucunda oluşabilecek zararlardan sorumlu değildir.
