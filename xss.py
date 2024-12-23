import requests

def xss_test(url):
    payload = "<script>alert('XSS')</script>"
    response = requests.get(url + "?search=" + payload)
    if payload in response.text:
        print(f"[XSS] Zəiflik aşkarlandı: {url}")
    else:
        print(f"[XSS] Zəiflik aşkarlanmadı: {url}")

# İstifadə
url = "https://sso.aztu.edu.az/"
xss_test(url)
