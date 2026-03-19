import json
import os

def main():
    clean_links = []
    
    if os.path.exists('out.json'):
        print("out.json найден! Начинаю фильтрацию...")
        with open('out.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        nodes = data.get("nodes", [])
        for node in nodes:
            # Узел ответил на запрос
            if node.get("ping", 0) > 0:
                link = node.get("link", "")
                remarks = node.get("remarks", "").lower()
                
                # Отсекаем IPv6
                if "ipv6" in remarks or "ipv6" in link.lower():
                    continue
                    
                clean_links.append(link)
    else:
        print("ОШИБКА: out.json не найден. Тестер отработал некорректно.")

    # Гарантированно создаем файл, чтобы не ломать Git
    with open('clean_proxies.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(clean_links))
    
    print(f"Готово! Сохранено {len(clean_links)} узлов.")

if __name__ == "__main__":
    main()
