import subprocess
import logging

def run_command(command):
    try:
        return subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.output}")
        return None

def add_rule(protocol, port, action="DROP"):
    command = ["sudo", "iptables", "-A", "INPUT", "-p", protocol, "--dport", str(port), "-j", action]
    print(run_command(command))

def remove_rule(protocol, port, action="DROP"):
    command = ["sudo", "iptables", "-D", "INPUT", "-p", protocol, "--dport", str(port), "-j", action]
    print(run_command(command))

def list_rules():
    command = ["sudo", "iptables", "-L"]
    print(run_command(command))

import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Manage Firewall Rules")
    parser.add_argument("--add", nargs=2, help="Add a new rule: protocol port")
    parser.add_argument("--remove", nargs=2, help="Remove a rule: protocol port")
    parser.add_argument("--list", action='store_true', help="List all rules")
    args = parser.parse_args()

    if args.add:
        add_rule(args.add[0], args.add[1])
    elif args.remove:
        remove_rule(args.remove[0], args.remove[1])
    elif args.list:
        list_rules()
    else:
        parser.print_help()
        sys.exit(1)

logging.basicConfig(level=logging.INFO, filename='firewall.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

def run_command(command):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        logging.info(f"Command success: {' '.join(command)} - Output: {output}")
        print(output)
        return output
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {' '.join(command)} - Error: {e.output}")
        print(f"An error occurred: {e.output}")
        return None

if __name__ == '__main__':
    main()




