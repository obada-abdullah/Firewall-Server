from logger import log_info

def process_packet(queue):
    while True:
        packet = queue.get()
        if packet is None:  # Check for shutdown signal
            break
        # Here you would implement your actual packet filtering logic based on rules
        log_info(f"Processed packet from {packet['ip']} on port {packet['port']} with action {packet['action']}")
        print(f"Processed packet from {packet['ip']} on port {packet['port']} with action {packet['action']}")
        queue.task_done()
