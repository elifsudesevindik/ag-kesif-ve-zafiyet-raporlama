from xml_oku import portlari_al
from cve import cve, cve_ara


def risk_hesaplama(cvss):
        if cvss >= 9:
            return "Kritik"
        elif cvss >= 7:
            return "Yüksek"
        elif cvss >= 4:
            return "Orta"
        else:
            return "Düşük"
def main():
    servisler = portlari_al()
    veritabani = cve()
    ports = []
    for s in servisler:
        cves = cve_ara(s["service"], s["version"], veritabani)
        if cves:
            skorlar = [c["cvss"] for c in cves if c["cvss"] is not None]
            if skorlar:
                max_skor = max(skorlar)
                risk = risk_hesaplama(max_skor)
                versiyon = s["version"] if s["version"] else ""

                ports.append({"port": s.get("port", "—"), "service": s["service"], "version": versiyon, "cvss": max_skor, "risk": risk})
    return ports
print("Tarama ve analiz tamamlandı.")