import xml.etree.ElementTree as ET
tree = ET.parse('sonuc.xml') # dosyayı açar
root = tree.getroot() # en üst etikete gider

def portlari_al():
    servisler = []
    for host in root.findall("host"):
        for ports in host.findall("ports"):
            for port in ports.findall("port"):
                service = port.find("service")
                if service is not None:
                    servisler.append({"port":port.get("portid"), "service": service.get("name"), "version": service.get("version")})
                else:
                    print(port.get("portid"), "bilgi yok")

    return servisler
