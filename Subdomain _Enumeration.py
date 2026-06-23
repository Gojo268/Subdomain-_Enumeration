import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
import os

def check_subdomain(subdomain, target_url, timeout=5):
    url = f"{subdomain}.{target_url}"
    try:
        result = requests.get(f"https://{url}", timeout=timeout, allow_redirects=True)
        if result.status_code < 400:
            print(f"[+] Subdomain Discovered ----------> {url} [Status: {result.status_code}]")
            return url
    except:
        pass
    return None

def main():
    print("=" * 50)
    print("     Subdomain Enumerator Tool")
    print("=" * 50)

    target_url = input("\n[?] Enter target domain (e.g. google.com): ").strip()
    target_url = target_url.replace("https://", "").replace("http://", "").rstrip("/")

    with ThreadPoolExecutor(max_workers=20) as executor:
        try:
            with open("subdomains-10000.txt", "r") as f:
                subdomains = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print("[-] subdomains-10000.txt not found!")
            sys.exit(1)

    print(f"\n[*] Enumerating subdomains for: {target_url}")
    print(f"[*] Testing {len(subdomains)} subdomains...\n")

    discovered = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_subdomain, sub, target_url): sub for sub in subdomains}
        for future in as_completed(futures):
            result = future.result()
            if result:
                discovered.append(result)

    print(f"\n[*] Done! Found {len(discovered)} subdomains.")

main()
