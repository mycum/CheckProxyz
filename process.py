import json
import os

def main():
    clean_links = []
    
    if os.path.exists('out.json'):
        print("✅ Файл out.json успешно создан! Начинаю парсинг...")
        with open('out.json', 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except:
                data = {}
        
        nodes = data.get("nodes", [])
        print(f"Всего протестировано узлов: {len(nodes)}")
        
        for node in nodes:
            ping_val = str(node.get("ping", ""))
            # Пинг должен быть больше 0 (значит узел рабочий)
            if ping_val and ping_val not in ["0", "0.00", "0.0"]:
                link = node.get("link", "")
                remarks = str(node.get("remarks", "")).lower()
                
                # Строгий фильтр IPv6
                if "ipv6" in remarks or "ipv6" in str(link).lower():
                    continue
                    
                clean_links.append(link)
    else:
        print("❌ ОШИБКА: out.json не найден. Тестер не отработал.")

    # Гарантированная запись, чтобы не падал Action
    with open('clean_proxies.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(clean_links))
    
    print(f"🎯 Готово! Сохранено рабочих узлов: {len(clean_links)}")

if __name__ == "__main__":
    main()
