import whois

def get_domain_info(domain):
    try:
        # Domen adı ilə WHOIS məlumatlarını əldə edirik
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        print(f"Xəta baş verdi: {e}")
        return None

# İstifadə:
domain = "example.com"
domain_info = get_domain_info(domain)
print(domain_info)

