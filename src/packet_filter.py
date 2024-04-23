import argparse
import subprocess

def add_rule(ip, action='DROP'):
    """Add a rule to block or allow an IP."""
    subprocess.run(f"sudo iptables -A INPUT -s {ip} -j {action}", shell=True)
    print(f"Rule added: {action} all traffic from {ip}")

def remove_rule(ip, action='DROP'):
    """Remove a rule blocking or allowing an IP."""
    subprocess.run(f"sudo iptables -D INPUT -s {ip} -j {action}", shell=True)
    print(f"Rule removed: {action} all traffic from {ip}")

def list_rules():
    """List all active iptables rules."""
    subprocess.run("sudo iptables -L", shell=True)
