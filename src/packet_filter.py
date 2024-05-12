import subprocess
from logger import log_info, log_error

def add_rule(ip, action='DROP'):
    """Add a rule to block or allow an IP."""
    try:
        subprocess.run(f'sudo iptables -A INPUT -s {ip} -j {action}', shell=True)
        log_info(f"Rule added: {action} all traffic from {ip}")
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to add rule: {action} all traffic from {ip}. Error: {str(e)}")

def remove_rule(ip, action='DROP'):
    """Remove a rule blocking or allowing an IP."""
    try:
        subprocess.run(f'sudo iptables -D INPUT -s {ip} -j {action}', check=True, shell=True)
        log_info(f"Rule removed: {action} all traffic from {ip}")
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to remove rule: {action} all traffic from {ip}. Error: {str(e)}")

def list_rules():
    """List all active iptables rules."""
    try:
        result = subprocess.run('sudo iptables -L', shell=True)
        log_info("Listed all active iptables rules")
        return result.stdout  # Return the list to the caller
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to list iptables rules. Error: {str(e)}")
        return None

