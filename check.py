import socket
import requests
import yaml
import re

# Источники (твои ссылки)
SOURCE_TXT = "https://github.com/igareck/vpn-configs-for-russia/raw/main/BLACK_SS+All_RUS.txt"
SOURCE_YAML = "https://github.com/mahdibland/V2RayAggregator/raw/refs/heads/master/update/provider/provider-all.yml"

OUTPUT_FILE = "clean_proxies.yaml"
TIMEOUT = 2 

def check_tcp(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=TIMEOUT):
            return True
    except:
        return False

def is_ipv6_named(text):
    return "ipv6" in str(text).lower()

def main():
    final_proxies = []
    
    # 1. Обработка TXT
    print("Загрузка TXT...")
    try:
        res_txt = requests.get(SOURCE_TXT, timeout=10)
        for line in res_txt.text.splitlines():
            line = line.strip()
            if not line or is_ipv6_named(line): continue
            
            # Проверка TCP для ссылок формата vless://...
            match = re.search(r'@(.*?):(\d+)', line)
            if match:
                if check_tcp(match.group(1), int(match.group(2))):
                    final_proxies.append(line)
    except Exception as e:
        print(f"Ошибка TXT: {e}")

    # 2. Обработка YAML
    print("Загрузка YAML...")
    try:
        res_yaml = requests.get(SOURCE_YAML, timeout=10)
        data = yaml.safe_load(res_yaml.text)
        if data and 'proxies' in data:
            for p in data['proxies']:
                name = p.get('name', '')
                server = p.get('server', '')
                port = p.get('port', 0)
                
                # Фильтр IPv6 в названии И в адресе сервера
                if is_ipv6_named(name) or is_ipv6_named(server) or ":" in str(server):
                    continue
                
                if check_tcp(server, port):
                    final_proxies.append(p)
    except Exception as e:
        print(f"Ошибка YAML: {e}")

    # Сохраняем результат
    output_data = {'proxies': final_proxies}
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        yaml.dump(output_data, f, allow_unicode=True, sort_keys=False)
    
    print(f"Готово! Сохранено рабочих прокси: {len(final_proxies)}")

if __name__ == "__main__":
    main()
