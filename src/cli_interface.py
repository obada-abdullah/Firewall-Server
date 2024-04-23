import argparse
from packet_filter import add_rule, remove_rule, list_rules
from port_manager import add_port_rule, remove_port_rule, list_port_rules
from rate_limiter import add_rate_limit, remove_rate_limit, list_rate_limits

def main():
    parser = argparse.ArgumentParser(description="Manage Firewall Rules")
    subparsers = parser.add_subparsers(dest='category', help='commands')

    # Packet management commands
    packet_parser = subparsers.add_parser('packet', help='Packet management commands')
    packet_subparsers = packet_parser.add_subparsers(dest='command', help='Packet management actions')
    packet_add_parser = packet_subparsers.add_parser('add', help='Add a new rule')
    packet_add_parser.add_argument('ip', type=str, help='IP address to block/allow')
    packet_add_parser.add_argument('--action', type=str, default='DROP', choices=['DROP', 'ACCEPT'],
                                   help='Action to take (default: DROP)')
    packet_remove_parser = packet_subparsers.add_parser('remove', help='Remove an existing rule')
    packet_remove_parser.add_argument('ip', type=str, help='IP address to remove block/allow')
    packet_remove_parser.add_argument('--action', type=str, default='DROP', choices=['DROP', 'ACCEPT'],
                                      help='Action to remove (default: DROP)')
    packet_list_parser = packet_subparsers.add_parser('list', help='List all rules')

    # Port management commands
    port_parser = subparsers.add_parser('port', help='Port management commands')
    port_subparsers = port_parser.add_subparsers(dest='port_command', help='Port management actions')
    port_add_parser = port_subparsers.add_parser('add', help='Add a port rule')
    port_add_parser.add_argument('port', type=int, help='Port to manage')
    port_add_parser.add_argument('--action', type=str, default='DROP', choices=['DROP', 'ACCEPT'],
                                 help='Action to apply (default: DROP)')
    port_remove_parser = port_subparsers.add_parser('remove', help='Remove a port rule')
    port_remove_parser.add_argument('port', type=int, help='Port to manage')
    port_remove_parser.add_argument('--action', type=str, default='DROP', choices=['DROP', 'ACCEPT'],
                                    help='Action to remove (default: DROP)')
    port_list_parser = port_subparsers.add_parser('list', help='List all port rules')
    
    
    # Rate limiting commands
    rate_parser = subparsers.add_parser('rate', help='Rate limiting commands')
    rate_subparsers = rate_parser.add_subparsers(dest='rate_command', help='Rate limiting actions')
    rate_add_parser = rate_subparsers.add_parser('add', help='Add a rate limit')
    rate_add_parser.add_argument('ip', type=str, help='IP address to limit')
    rate_add_parser.add_argument('rate', type=str, help='Rate (e.g., 5/second)')
    rate_add_parser.add_argument('--limit-burst', type=int, default=5, help='Burst limit (default: 5)')
    rate_remove_parser = rate_subparsers.add_parser('remove', help='Remove a rate limit')
    rate_remove_parser.add_argument('ip', type=str, help='IP address to remove limit from')
    rate_list_parser = rate_subparsers.add_parser('list', help='List all rate limits')
    
    args = parser.parse_args()

    if args.category == 'packet':
        if args.command == 'add':
            add_rule(args.ip, args.action)
        elif args.command == 'remove':
            remove_rule(args.ip, args.action)
        elif args.command == 'list':
            list_rules()
    elif args.category == 'port':
        if args.port_command == 'add':
            add_port_rule(args.port, args.action)
        elif args.port_command == 'remove':
            remove_port_rule(args.port, args.action)
        elif args.port_command == 'list':
            list_port_rules()
    
    elif args.category == 'rate':
        if args.rate_command == 'add':
            add_rate_limit(args.ip, args.rate, args.limit_burst)
        elif args.rate_command == 'remove':
            remove_rate_limit(args.ip)
        elif args.rate_command == 'list':
            list_rate_limits()

if __name__ == '__main__':
    main()
