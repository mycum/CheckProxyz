import json
import os

def main():
    clean_links = []
    
    if os.path.exists('out.json'):
        print("✅ Файл out.json успешно создан тестером! Начинаю парсинг...")
        with open('out.json', 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except:
                data = {}
        
        nodes = data.get("nodes", [])
        print(f"Всего протестировано узлов: {len(nodes)}")
        
        for node in nodes:
            ping_val = str(node.get("ping", ""))
            # Оставляем только те, которые реально ответили (пинг > 0)
            if ping_val and ping_val != "0" and ping_val != "0.00":
                link = node.get("link", "")
                remarks = str(node.get("remarks", "")).lower()
                
                # Отсекаем IPv6
                if "ipv6" in remarks or "ipv6" in str(link).lower():
                    continue
                    
                clean_links.append(link)
    else:
        print("❌ ОШИБКА: out.json не найден. Тестер упал или не отработал.")
        print("Файлы в текущей папке:", os.listdir('.'))

    # Записываем результат
    with open('clean_proxies.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(clean_links))
    
    print(f"🎯 Готово! В итоговый файл записано {len(clean_links)} рабочих узлов.")

if __name__ == "__main__":
    main()
