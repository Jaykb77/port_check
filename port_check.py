import socket
import time
import subprocess

def check_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((host, port))
            return True, None
    except Exception as e:
            return False, str(e)

def read_hosts(file_path):
    hosts = {}
    with open(file_path, 'r') as file:
        for line in file:
            host, port = line.strip().split(':')
            hosts[host] = int(port)
    return hosts

def log_result(host, port, is_open, error):
    with open('port_check.log', 'a') as log_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_file.write(f'{timestamp} - Host: {host}, Port: {port}, error: {error}\n')
        mtr_output = subprocess.run(['mtr', '-r', '-n','-c', '10', host], capture_output=True, text=True)
        log_file.write(mtr_output.stdout)

if __name__ == '__main__':
    hosts = read_hosts('/app/input.txt')
    while True:
        for host, port in hosts.items():
            is_open, error = check_port(host, port)
            if not is_open:
             log_result(host, port, is_open, error)
        time.sleep(15)  # Check every 10 seconds

