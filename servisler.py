
servis_bilgileri = {
    "ftp": {
        "tanim": "Dosya transfer protokolüdür. Port 21 üzerinden çalışır.",
        "risk": "Kullanıcı adı ve parola şifresiz iletilir. Saldırgan ağ trafiğini dinleyerek kimlik bilgilerini ele geçirebilir.",
        "oneri": "Derhal kapatılmalıdır. Dosya transferi için SFTP veya SCP kullanılmalıdır."
    },
    "ssh": {
        "tanim": "Uzak sunucuya şifreli bağlantı sağlayan protokoldür.",
        "risk": "Kullanılan OpenSSH 4.7p1 versiyonu çok eskidir ve kritik güvenlik açıkları barındırır. Kaba kuvvet saldırılarına açıktır.",
        "oneri": "Güncel versiyona yükseltilmeli, anahtar tabanlı kimlik doğrulamaya geçilmelidir."
    },
    "telnet": {
        "tanim": "Uzak sisteme bağlanmak için kullanılan eski bir protokoldür.",
        "risk": "Tüm veri, parola dahil, şifresiz olarak iletilir. Ağı dinleyen herkes oturum bilgilerini görebilir.",
        "oneri": "Derhal kapatılmalıdır. Bunun yerine SSH kullanılmalıdır."
    },
    "smtp": {
        "tanim": "E-posta gönderimi için kullanılan protokoldür.",
        "risk": "Kimlik doğrulama zayıflığı nedeniyle sistemi spam göndermek veya sahte e-posta üretmek için kullanılabilir.",
        "oneri": "Gereksizse kapatılmalı, gerekiyorsa TLS kullanılmalıdır."
    },
    "domain": {
        "tanim": "DNS servisidir, alan adlarını IP adreslerine çevirir.",
        "risk": "ISC BIND 9.4.2 versiyonu çok eskidir. DNS zehirleme ve uzaktan kod çalıştırma saldırılarına açıktır.",
        "oneri": "Güncel versiyona yükseltilmeli ve dış ağa kapalı tutulmalıdır."
    },
    "http": {
        "tanim": "Web sunucusudur. Tarayıcı üzerinden erişilebilir.",
        "risk": "Apache 2.2.8 versiyonu kritik güvenlik açıkları içerir. Şifresiz bağlantı sunduğu için veriler dinlenebilir.",
        "oneri": "Apache güncel versiyona yükseltilmeli, HTTPS kullanılmalıdır."
    },
    "exec": {
        "tanim": "Uzaktan komut çalıştırma servisidir.",
        "risk": "Kimlik doğrulama gerektirmez. Saldırgan sisteme doğrudan komut gönderebilir ve tam kontrol ele geçirebilir.",
        "oneri": "Derhal kapatılmalıdır. Hiçbir durumda dışarıya açık olmamalıdır."
    },
    "login": {
        "tanim": "Uzak sistemde oturum açmaya yarayan eski bir servistir.",
        "risk": "Şifresiz erişime izin verir. Saldırgan sisteme kolayca giriş yapabilir.",
        "oneri": "Derhal kapatılmalıdır. SSH kullanılmalıdır."
    },
    "shell": {
        "tanim": "Uzak sistemde kabuk erişimi sağlayan eski bir servistir.",
        "risk": "Kimlik doğrulamasız uzak komut çalıştırmaya olanak tanır. Sisteme tam erişim sağlanabilir.",
        "oneri": "Derhal kapatılmalıdır."
    },
    "nfs": {
        "tanim": "Ağ üzerinden dosya paylaşımı sağlayan protokoldür.",
        "risk": "Yetkisiz kullanıcılar paylaşılan dosyalara erişebilir. Yanlış yapılandırıldığında sisteme dosya yazılabilir.",
        "oneri": "Dış ağa kapatılmalı, sadece güvenilen IP adreslerine erişim verilmelidir."
    },
    "mysql": {
        "tanim": "İlişkisel veritabanı yönetim sistemidir.",
        "risk": "MySQL 5.0.51a versiyonu kritik SQL açıkları içerir. Dışarıya açık olması veritabanının ele geçirilmesine yol açabilir.",
        "oneri": "Güncellenmelidir. Sadece yerel erişime açık olmalı, dışarıdan bağlantı engellenmelidir."
    },
    "postgresql": {
        "tanim": "Gelişmiş ilişkisel veritabanı yönetim sistemidir.",
        "risk": "Dışarıya açık veritabanı yetkisiz erişim ve veri sızıntısı riski taşır.",
        "oneri": "Dış ağa kapatılmalı, güçlü parola politikası uygulanmalıdır."
    },
    "vnc": {
        "tanim": "Uzak masaüstü erişim protokolüdür.",
        "risk": "Zayıf şifreleme kullanır. Kaba kuvvet saldırılarıyla parola kırılabilir ve masaüstüne tam erişim sağlanabilir.",
        "oneri": "Kapatılmalı veya VPN arkasına alınmalıdır."
    },
    "X11": {
        "tanim": "Linux sistemlerde grafik arayüz protokolüdür.",
        "risk": "Dışarıya açıksa saldırgan ekran içeriğini görebilir, klavye girişlerini izleyebilir.",
        "oneri": "Dış ağa kapatılmalıdır."
    },
    "irc": {
        "tanim": "İnternet üzerinden anlık mesajlaşma protokolüdür.",
        "risk": "Bu sistemdeki UnrealIRCd versiyonunda arka kapı açığı bulunmaktadır. Saldırgan sisteme doğrudan erişim sağlayabilir.",
        "oneri": "Derhal kapatılmalıdır."
    },
    "ccproxy-ftp": {
        "tanim": "FTP proxy servisidir.",
        "risk": "Güvenlik açıkları barındırır, yetkisiz erişime zemin hazırlayabilir.",
        "oneri": "Kapatılmalıdır."
    },
    "ajp13": {
        "tanim": "Apache web sunucusu ile Tomcat arasında iletişim sağlayan protokoldür.",
        "risk": "Ghostcat açığına karşı savunmasızdır. Saldırgan sunucudaki dosyaları okuyabilir veya kod çalıştırabilir.",
        "oneri": "Kapatılmalı veya güncel versiyona yükseltilmelidir."
    }
}