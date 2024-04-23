import subprocess

def add_ip_rule(ip, action='DROP'):
    """Add an IP rule to the firewall."""
    command = f"sudo iptables -A INPUT -s {ip} -j {action}"
    subprocess.run(command, shell=True)
    print(f"IP rule added: {action} traffic from {ip}")

def remove_ip_rule(ip, action='DROP'):
    """Remove an IP rule from the firewall."""
    command = f"sudo iptables -D INPUT -s {ip} -j {action}"
    subprocess.run(command, shell=True)
    print(f"IP rule removed: {action} traffic from {ip}")

def list_ip_rules():
    """List all IP rules from the firewall."""
    command = "sudo iptables -L INPUT -v -n"
    subprocess.run(command, shell=True)
