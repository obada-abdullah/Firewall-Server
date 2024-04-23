import subprocess
from logger import log_info, log_error

def add_rule(ip, action='DROP'):
    """Add a rule to block or allow an IP."""
    command = f"sudo iptables -A INPUT -s {ip} -j {action}"
    try:
        subprocess.run(command, shell=True, check=True)
        log_info(f"Rule added: {action} all traffic from {ip}")
    except subprocess.CalledProcessError:
        log_error(f"Failed to add rule: {action} all traffic from {ip}")

def remove_rule(ip, action='DROP'):
    """Remove a rule blocking or allowing an IP."""
    command = f"sudo iptables -D INPUT -s {ip} -j {action}"
    try:
        subprocess.run(command, shell=True, check=True)
        log_info(f"Rule removed: {action} all traffic from {ip}")
    except subprocess.CalledProcessError:
        log_error(f"Failed to remove rule: {action} all traffic from {ip}")

def list_rules():
    """List all active iptables rules."""
    try:
        subprocess.run("sudo iptables -L", shell=True, check=True)
        log_info("Listed all active iptables rules")
    except subprocess.CalledProcessError:
        log_error("Failed to list iptables rules")
