import socket
import time
import subprocess

def check_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((host, port))
            return True
    except (socket.timeout, ConnectionRefusedError):
        return False

def read_hosts(file_path):
    hosts = {}
    with open(file_path, 'r') as file:
        for line in file:
            host, port = line.strip().split(':')
            hosts[host] = int(port)
    return hosts

def log_result(host, port, is_open):
    with open('port_check.log', 'a') as log_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        status = 'open' if is_open else 'closed'
        log_file.write(f'{timestamp} - Host: {host}, Port: {port}, Status: {status}\n')
        if not is_open:
            mtr_output = subprocess.run(['mtr', '-r','-c', '10', host], capture_output=True, text=True)
            log_file.write(mtr_output.stdout)

if __name__ == '__main__':
    hosts = read_hosts('/app/input.txt')
    while True:
        for host, port in hosts.items():
            is_open = check_port(host, port)
            log_result(host, port, is_open)
        time.sleep(10)  # Check every 10 seconds

