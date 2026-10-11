import json

def cve():
    dosyalar = ["nvdcve-2.0-2022.json", "nvdcve-2.0-2023.json", "nvdcve-2.0-2024.json", "nvdcve-2.0-2025.json", "nvdcve-2.0-2026.json"]
    veritabani = []
    for dosya in dosyalar:
        with open(dosya, "r", encoding="utf-8") as f:
            veri = json.load(f)
            veritabani.append(veri)
    return veritabani

def cve_ara(servis, version, veritabani):
    bulunan_cve = []
    for veri in veritabani:
        for item in veri["vulnerabilities"]:
            aciklama = item["cve"]["descriptions"][0]["value"]
            if servis.lower() in aciklama.lower():
                    skor = None
                    metrics = item["cve"]["metrics"]   #metrics → O CVE'nin tehlike ölçüm verileri. Yani o açığın ne kadar tehlikeli olduğunu sayısal olarak gösteren bilgiler.
                    if "cvssMetricV31" in metrics:
                        skor = metrics["cvssMetricV31"][0]["cvssData"]["baseScore"]
                    elif "cvssMetricV2" in metrics:
                        skor = metrics["cvssMetricV2"][0]["cvssData"]["baseScore"]
                    bulunan_cve.append({"cve": item["cve"]["id"], "cvss": skor})
    return bulunan_cve
