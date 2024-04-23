import subprocess

def add_port_rule(port, action='DROP'):
    """Add a rule to block or allow traffic on a specific port."""
    command = f"sudo iptables -A INPUT -p tcp --dport {port} -j {action}"
    subprocess.run(command, shell=True)
    print(f"Rule added: {action} traffic on port {port}")

def remove_port_rule(port, action='DROP'):
    """Remove a rule blocking or allowing traffic on a specific port."""
    command = f"sudo iptables -D INPUT -p tcp --dport {port} -j {action}"
    subprocess.run(command, shell=True)
    print(f"Rule removed: {action} traffic on port {port}")

def list_port_rules():
    """List all rules for a specific port from the firewall."""
    command = "sudo iptables -L INPUT -v -n --line-numbers"
    subprocess.run(command, shell=True)
