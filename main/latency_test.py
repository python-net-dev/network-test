import os
import platform
import subprocess
import time

def ping_host(host):
    """
    Returns True if host responds to a ping request
    """
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '4', host]
    return subprocess.call(command, stdout=subprocess.DEVNULL) == 0

def benchmark_node(node_name, address):
    print(f"[*] Testing Node: {node_name} ({address})")
    start_time = time.time()
    success = ping_host(address)
    end_time = time.time()
    
    if success:
        latency = (end_time - start_time) * 1000 / 4
        print(f"[+] Status: Online | Avg Latency: {latency:.2f}ms")
    else:
        print(f"[-] Status: Offline or High Packet Loss")
    print("-" * 30)

if __name__ == "__main__":
    print("=== 2026 Network Protocol Benchmark Tool ===")
    # 模拟测试地址
    nodes = {
        "CloudFlare-Anycast": "1.1.1.1",
        "Google-Public-DNS": "8.8.8.8",
        "Target-Server-Proxy": "yuncat.top"
    }
    
    for name, addr in nodes.items():
        benchmark_node(name, addr)
