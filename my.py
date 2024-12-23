import requests
from bs4 import BeautifulSoup

def get_site_info(url):
    try:
        # Veb sayta sorğu göndəririk
        response = requests.get(url)
        response.raise_for_status()  # HTTP səhvlərini yoxlayırıq

        # Saytın başlığını alırıq
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "Başliq yoxdur"
        
        # Saytın meta məlumatlarını alırıq
        metas = soup.find_all('meta')
        meta_info = {}
        for meta in metas:
            if 'name' in meta.attrs:
                meta_info[meta.attrs['name']] = meta.attrs.get('content', 'Məlumat yoxdur')

        return title, meta_info
    except requests.exceptions.RequestException as e:
        print(f"Xəta baş verdi: {e}")
        return None, None

# İstifadə:
url = "http://example.com"
title, meta_info = get_site_info(url)
print(f"Başliq: {title}")
print(f"Meta Məlumatlari: {meta_info}")
