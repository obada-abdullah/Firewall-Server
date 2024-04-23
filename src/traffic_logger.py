import subprocess
from logger import log_info, log_error

def enable_traffic_logging(ip=None, port=None, protocol='tcp'):
    """Enable logging for matching traffic."""
    rule_components = ["sudo iptables -A INPUT -j LOG"]
    if ip:
        rule_components.append(f"-s {ip}")
    if port:
        rule_components.append(f"--dport {port}")
    rule_components.append(f"-p {protocol}")
    rule_components.append("--log-prefix 'TrafficLog: '")
    command = " ".join(rule_components)
    try:
        subprocess.run(command, shell=True, check=True)
        log_info(f"Enabled traffic logging: IP={ip}, Port={port}, Protocol={protocol}")
    except subprocess.CalledProcessError:
        log_error(f"Failed to enable traffic logging: IP={ip}, Port={port}, Protocol={protocol}")

def disable_traffic_logging(ip=None, port=None, protocol='tcp'):
    """Disable logging for matching traffic."""
    rule_components = ["sudo iptables -D INPUT -j LOG"]
    if ip:
        rule_components.append(f"-s {ip}")
    if port:
        rule_components.append(f"--dport {port}")
    rule_components.append(f"-p {protocol}")
    rule_components.append("--log-prefix 'TrafficLog: '")
    command = " ".join(rule_components)
    try:
        subprocess.run(command, shell=True, check=True)
        log_info(f"Disabled traffic logging: IP={ip}, Port={port}, Protocol={protocol}")
    except subprocess.CalledProcessError:
        log_error(f"Failed to disable traffic logging: IP={ip}, Port={port}, Protocol={protocol}")
