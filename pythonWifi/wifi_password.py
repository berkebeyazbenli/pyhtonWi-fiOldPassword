import subprocess

# SSID'yi belirtin
ssid = "Anadolu"

# Wi-Fi şifresini bulma
try:
    wifi_password = subprocess.check_output(["security", "find-generic-password", "-D", "AirPort network password", "-a", ssid, "-gw"])
    wifi_password = wifi_password.decode("utf-8").strip()
    print(f"Wi-Fi Adı: {ssid}, Şifre: {wifi_password}")
except subprocess.CalledProcessError:
    print(f"Wi-Fi Adı: {ssid}, Şifre bulunamadı")
