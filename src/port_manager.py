import subprocess
from logger import log_info, log_error

def add_port_rule(port, action='DROP'):
    """Add a rule to block or allow traffic on a specific port."""
    command = f"sudo iptables -A INPUT -p tcp --dport {port} -j {action}"
    try:
        subprocess.run(command, shell=True, check=True)  # Ensure command execution is checked for errors
        log_info(f"Rule added: {action} traffic on port {port}")
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to add rule: {action} traffic on port {port} - {e}")

def remove_port_rule(port, action='DROP'):
    """Remove a rule blocking or allowing traffic on a specific port."""
    command = f"sudo iptables -D INPUT -p tcp --dport {port} -j {action}"
    try:
        subprocess.run(command, shell=True, check=True)  # Ensure command execution is checked for errors
        log_info(f"Rule removed: {action} traffic on port {port}")
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to remove rule: {action} traffic on port {port} - {e}")

def list_port_rules():
    """List all rules for a specific port from the firewall."""
    command = "sudo iptables -L INPUT -v -n --line-numbers"
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        log_info("Listed all port rules")
        return result.stdout  # Return the list of rules as output for further processing or display
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to list port rules - {e}")
        return None
