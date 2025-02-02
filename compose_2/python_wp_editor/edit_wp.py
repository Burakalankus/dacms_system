import requests
import json
import time
# WordPress API URL (Post ID 10)
WP_URL = "http://192.168.56.4:8080/wp-json/wp/v2/posts/10"
WP_USER = "Balankus"
WP_PASSWORD = "135246bba"

# Yeni içerik
data = {
        "content": "This is Post 10, updated with Burak"

}

# API isteğini "PUT" yöntemiyle gönderiyoruz
response = requests.put(WP_URL, json=data, auth=(WP_USER, WP_PASSWORD))

# API yanıtını detaylı kontrol edelim
if response.status_code == 200:
    response_json = response.json()  # JSON formatına çevir
    post_id = response_json.get("id", "Unknown")  # Güncellenen post ID'sini al
    post_title = response_json.get("title", {}).get("rendered", "Unknown")  # Post başlığını al
    print(f"✅ Blog post {post_id} ({post_title}) updated successfully!")
    print("📌 API Response:", json.dumps(response_json, indent=4, ensure_ascii=False))
else:
    print(f"❌ Failed to update post: {response.status_code}")
    print("📌 Response Content:", response.text)

time.sleep(1800)
