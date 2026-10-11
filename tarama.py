import subprocess
ip="metasploit ip"
sonuc= "dosya yolu"
subprocess.run(["nmap", "-sV", "-oX", sonuc, ip])
