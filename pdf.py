from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import cm
from datetime import datetime
from servisler import servis_bilgileri
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('DejaVu', r'C:\Windows\Fonts\arial.ttf'))


def pdf_olustur(data):
    from reportlab.lib.pagesizes import A4

    doc = SimpleDocTemplate("rapor.pdf", pagesize=A4,
        leftMargin=1*cm, rightMargin=1*cm, topMargin=1*cm, bottomMargin=1*cm)

    # Tüm stiller DejaVu ile tanımlanıyor
    baslik = ParagraphStyle('baslik', fontName='DejaVu', fontSize=16, leading=20, spaceAfter=6)
    normal = ParagraphStyle('normal', fontName='DejaVu', fontSize=10, leading=14, spaceAfter=4)
    h2 = ParagraphStyle('h2', fontName='DejaVu', fontSize=13, leading=16, spaceAfter=6, spaceBefore=10)
    h3 = ParagraphStyle('h3', fontName='DejaVu', fontSize=11, leading=14, spaceAfter=4, spaceBefore=6)

    content = []

    # BAŞLIK
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
    content.append(Paragraph("Ağ Güvenlik Analiz Raporu", baslik))
    content.append(Spacer(1, 6))
    content.append(Paragraph(f"Oluşturulma tarihi: {tarih}", normal))
    content.append(Paragraph("Hedef sistem: 192.168.56.102 (Metasploitable2)", normal))
    content.append(Spacer(1, 16))

    # GİRİŞ
    content.append(Paragraph("1. Giriş", h2))
    content.append(Paragraph(
        "Bu rapor, hedef sistem üzerinde Nmap aracı kullanılarak gerçekleştirilen ağ taraması sonuçlarını içermektedir. "
        "Tespit edilen servisler CVE veritabanı ile karşılaştırılmış, her servis için CVSS skoruna göre risk seviyesi belirlenmiştir. "
        "Rapor otomatik olarak üretilmiş olup güvenlik uzmanlarının incelemesine yardımcı olmak amacıyla hazırlanmıştır.",
        normal
    ))
    content.append(Spacer(1, 12))

    # ÖZET
    kritik = sum(1 for d in data if d["risk"] == "Kritik")
    yuksek = sum(1 for d in data if d["risk"] == "Yüksek")
    orta = sum(1 for d in data if d["risk"] == "Orta")

    content.append(Paragraph("2. Özet", h2))
    content.append(Paragraph(f"Toplam taranan servis sayısı: {len(data)}", normal))
    content.append(Paragraph(f"Kritik risk seviyesinde servis: {kritik}", normal))
    content.append(Paragraph(f"Yüksek risk seviyesinde servis: {yuksek}", normal))
    content.append(Paragraph(f"Orta risk seviyesinde servis: {orta}", normal))
    content.append(Spacer(1, 12))

    # SERVİS ANALİZİ
    content.append(Paragraph("3. Servis Analizi", h2))
    content.append(Spacer(1, 6))

    for d in data:
        bilgi = servis_bilgileri.get(d["service"], {})
        content.append(Paragraph(f"{d['service'].upper()} — {d['risk']} (CVSS: {d['cvss']})", h3))
        content.append(Paragraph(f"Port: {d.get('port', '-')}", normal))
        content.append(Paragraph(f"Versiyon: {d['version'] or '-'}", normal))
        content.append(Paragraph(f"Tanım: {bilgi.get('tanim', '-')}", normal))
        content.append(Paragraph(f"Risk: {bilgi.get('risk', '-')}", normal))
        content.append(Paragraph(f"Öneri: {bilgi.get('oneri', '-')}", normal))
        content.append(Spacer(1, 8))

    # SONUÇ
    content.append(Paragraph("4. Sonuç ve Öneriler", h2))
    content.append(Paragraph(
        "Gerçekleştirilen tarama sonucunda hedef sistemde çok sayıda kritik güvenlik açığı tespit edilmiştir. "
        "Tespit edilen servisler güncel CVE veritabanı ile karşılaştırılmış ve CVSS skorlarına göre sınıflandırılmıştır. "
        "Gerçek bir sistemde bu bulgular derhal ele alınmalı, gereksiz servisler kapatılmalı ve "
        "kullanılan yazılımlar güncel versiyonlara yükseltilmelidir.",
        normal
    ))

    doc.build(content)