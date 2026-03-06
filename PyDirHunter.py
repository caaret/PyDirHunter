import requests 

IP = input("Enter Domain : ")

import_directory = [
    "/.env",
    "/config.php",
    "/config.json",
    "/.git/",
    "/admin",
    "/login",
    "/wp-admin",
    "/administrator",
    "/cpanel",
    "/phpmyadmin",
    "/dashboard",
    "/backup.zip",
    "/backup.sql",
    "/config.bak",
    "/.vscode",
    "/robots.txt",
    "/sitemap.xml",
    "/info.php",
    "/phpinfo.php"
]
open_list = []
for scan_domain in import_directory:
    full_url = f"{IP}{scan_domain}"
    result = requests.get(full_url)
    if result.status_code == 200:
        open_list.append(scan_domain)

print("Found Domain")
print(*open_list)