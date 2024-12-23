# CVE məlumatlarını almaq üçün funksiya
import requests

def get_cve_info(cve_id):
    url = f"https://cve.circl.lu/api/cve/{cve_id}"
    response = requests.get(url)
    if response.status_code == 200:
        cve_data = response.json()
        print(f"CVE məlumati: {cve_data}")
    else:
        print("CVE məlumati tapilmadi.")

cve_id = "CVE-2023-12345"  # Məsələn, CVE identifikatoru
get_cve_info(cve_id)
