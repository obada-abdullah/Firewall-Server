import subprocess
from logger import log_info, log_error

def add_rate_limit(ip, rate, limit_burst=5):
    """Add a rate limit rule for a specific IP."""
    command = f"sudo iptables -A INPUT -s {ip} -m limit --limit {rate}/second --limit-burst {limit_burst} -j ACCEPT"
    try:
        subprocess.run(command, shell=True, check=True)
        log_info(f"Rate limit rule added: {rate}/second for {ip}, burst {limit_burst}")
    except subprocess.CalledProcessError:
        log_error(f"Failed to add rate limit rule: {rate}/second for {ip}")

def remove_rate_limit(ip):
    """Remove a rate limit rule for a specific IP."""
    command = f"sudo iptables -D INPUT -s {ip} -m limit -j ACCEPT"
    try:
        subprocess.run(command, shell=True, check=True)
        log_info(f"Rate limit rule removed for {ip}")
    except subprocess.CalledProcessError:
        log_error(f"Failed to remove rate limit rule for {ip}")

def list_rate_limits():
    """List all rate limit rules."""
    try:
        subprocess.run("sudo iptables -L INPUT -v -n --line-numbers", shell=True, check=True)
        log_info("Listed all rate limit rules")
    except subprocess.CalledProcessError:
        log_error("Failed to list rate limit rules")
