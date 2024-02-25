import re

def defang_url(url):
    defanged_url = re.sub(r'https?://', 'hxxps://', url)
    defanged_url = re.sub(r'http://', 'hxxp://', defanged_url)
    defanged_url = re.sub(r':', '[:]', defanged_url)
    defanged_url = re.sub(r'\.', '[.]', defanged_url)
    return defanged_url

def defang_ip(ip):
    defanged_ip = re.sub(r'\.', '[.]', ip)
    return defanged_ip

def identify_hash_type(hash_value):
    if re.match(r'^[a-fA-F0-9]{32}$', hash_value):
        return 'MD5'
    elif re.match(r'^[a-fA-F0-9]{40}$', hash_value):
        return 'SHA-1'
    elif re.match(r'^[a-fA-F0-9]{64}$', hash_value):
        return 'SHA-256'
    else:
        return 'Unknown'

def process_hashes(file_path):
    unique_hashes = set()
    unique_urls = set()
    unique_ips = set()

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if re.match(r'^https?://', line) or re.match(r'^http://', line):
                defanged_url = defang_url(line)
                unique_urls.add(defanged_url)
            elif re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', line):
                defanged_ip = defang_ip(line)
                unique_ips.add(defanged_ip)
            else:
                hash_type = identify_hash_type(line)
                unique_hashes.add((line, hash_type))

    with open('ioc-output.txt', 'w') as output_file:
        if unique_urls:
            output_file.write("Unique URLs:\n")
            for url in unique_urls:
                output_file.write(url + '\n')

        if unique_ips:
            output_file.write("\nUnique IPs:\n")
            for ip in unique_ips:
                output_file.write(ip + '\n')

        if unique_hashes:
            output_file.write("\nUnique hashes:\n")
            for hash_value, hash_type in unique_hashes:
                output_file.write(f"{hash_value} - {hash_type}\n")

file_path = 'IOC.txt'
process_hashes(file_path)

