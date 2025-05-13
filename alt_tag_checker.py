import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def check_image_alt_tags(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        images = soup.find_all("img")

        print(f"\n🔍 Found {len(images)} image(s) on: {url}\n")

        missing_alt = []

        for img in images:
            if not img.get("alt"):
                img_src = img.get("src")
                full_src = urljoin(url, img_src) if img_src else "[No src]"
                print(f"❌ Missing ALT: {full_src}")
                missing_alt.append(full_src)

        if not missing_alt:
            print("\n✅ All images have ALT tags!")
        else:
            print(f"\n🚨 {len(missing_alt)} image(s) missing ALT text.")
    
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    url = input("Enter the URL (include https://): ").strip()
    check_image_alt_tags(url)
