import subprocess
from logger import log_info, log_error

def add_rate_limit(ip, rate, limit_burst=5):
    """Add a rate limit rule for a specific IP."""
    try:
        subprocess.run(f'sudo iptables -A INPUT -s {ip} -m limit --limit {rate}/second --limit-burst {limit_burst} -j ACCEPT', shell=True)
        log_info(f"Rate limit rule added: {rate}/second for {ip}, burst {limit_burst}")
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to add rate limit rule: {rate}/second for {ip} - {str(e)}")

def remove_rate_limit(ip, rate, limit_burst=5):
    """Remove a rate limit rule for a specific IP."""
    command = [
        'sudo', 'iptables', '-D', 'INPUT', '-s', ip,
        '-m', 'limit', '--limit', f"{rate}/second", '--limit-burst', str(limit_burst), '-j', 'ACCEPT'
    ]
    try:
        subprocess.run(f'sudo iptables -D INPUT -s {ip} -m limit --limit {rate}/second --limit-burst {limit_burst} -j ACCEPT', shell=True)
        log_info(f"Rate limit rule removed for {ip}")
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to remove rate limit rule for {ip} - {str(e)}")

def list_rate_limits():
    """List all rate limit rules."""
    try:
        result = subprocess.run('sudo iptables -L INPUT -v -n --line-numbers', shell=True)
        log_info("Listed all rate limit rules")
        return result.stdout
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to list rate limit rules - {str(e)}")
        return None
