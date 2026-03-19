import json
import os

def main():
    if not os.path.exists('out.json'):
        print("Error: out.json not found")
        return

    with open('out.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    nodes = data.get("nodes", [])
    clean_links = []

    for node in nodes:
        # Проверяем ping (если 0 - узел мертв)
        if node.get("ping", 0) > 0:
            link = node.get("link", "")
            remarks = node.get("remarks", "").lower()
            
            # Фильтр IPv6 в названии или самой ссылке
            if "ipv6" in remarks or "ipv6" in link.lower():
                continue
                
            clean_links.append(link)

    with open('clean_proxies.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(clean_links))
    
    print(f"Done! Saved {len(clean_links)} nodes.")

if __name__ == "__main__":
    main()
