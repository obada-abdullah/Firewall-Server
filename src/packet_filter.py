import subprocess
from logger import log_info, log_error

def add_rule(ip, action='DROP'):
    """Add a rule to block or allow an IP."""
    command = ['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', action]
    try:
        subprocess.run(command, check=True)
        log_info(f"Rule added: {action} all traffic from {ip}")
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to add rule: {action} all traffic from {ip}. Error: {str(e)}")

def remove_rule(ip, action='DROP'):
    """Remove a rule blocking or allowing an IP."""
    command = ['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', action]
    try:
        subprocess.run(command, check=True)
        log_info(f"Rule removed: {action} all traffic from {ip}")
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to remove rule: {action} all traffic from {ip}. Error: {str(e)}")

def list_rules():
    """List all active iptables rules."""
    command = ['sudo', 'iptables', '-L']
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        log_info("Listed all active iptables rules")
        return result.stdout  # Return the list to the caller
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to list iptables rules. Error: {str(e)}")
        return None

