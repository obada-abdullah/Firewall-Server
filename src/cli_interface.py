import argparse
from packet_filter import add_rule, remove_rule, list_rules

def main():
    parser = argparse.ArgumentParser(description="Manage Firewall Rules")
    subparsers = parser.add_subparsers(dest='command', help='commands')

    # Add rule command
    add_parser = subparsers.add_parser('add', help='Add a new rule')
    add_parser.add_argument('ip', type=str, help='IP address to block/allow')
    add_parser.add_argument('--action', type=str, default='DROP', choices=['DROP', 'ACCEPT'],
                            help='Action to take (default: DROP)')

    # Remove rule command
    remove_parser = subparsers.add_parser('remove', help='Remove an existing rule')
    remove_parser.add_argument('ip', type=str, help='IP address to remove block/allow')
    remove_parser.add_argument('--action', type=str, default='DROP', choices=['DROP', 'ACCEPT'],
                               help='Action to remove (default: DROP)')

    # List rules command
    list_parser = subparsers.add_parser('list', help='List all rules')

    args = parser.parse_args()

    if args.command == 'add':
        add_rule(args.ip, args.action)
    elif args.command == 'remove':
        remove_rule(args.ip, args.action)
    elif args.command == 'list':
        list_rules()

if __name__ == '__main__':
    main()
