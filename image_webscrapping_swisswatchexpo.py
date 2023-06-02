import requests
import re

# URL der Webseite, von der du die Bilder herunterladen möchtest
url = "https://www.swisswatchexpo.com/watches/rolex/?=H4sIAAAAAAAACj2OSw6AIAxE79K1LlDZcBXjAvETEiSN4Mp4dztoWPX1ZTpwk3cbmXxea0McbCbTA1L2hRx_IpHZbEgS8tFWjpb9UrckoXiFAKp4SM.o9SRhkMwZc4CRbgjeYZSQXFGnWq0IT_55xle.Mi5tcK7A8wIsg3ITvwAAAA--"
response = requests.get(url)

# Suche nach allen URLs, die auf .jpg enden
image_urls = re.findall(r"(https?://[^\s]+\.jpg)", response.text)

# Zähler für die heruntergeladenen Bilder
counter = 1

# Iteriere über alle gefundenen Bild-URLs
for image_url in image_urls:
    try:
        # Lade das Bild herunter und speichere es lokal
        response = requests.get(image_url)
        with open(f"rolex_daydate_swisswatchexpo_page3_{counter}.jpg", "wb") as f:
            f.write(response.content)
        
        print(f"Bild {counter} heruntergeladen: {image_url}")
        counter += 1
    except:
        print(f"Fehler beim Herunterladen von {image_url}")

print("Web-Scraping abgeschlossen.")

