import queue
import threading
from packet_worker import process_packet

num_workers = 3
queues = [queue.Queue() for _ in range(num_workers)]
workers = []

def setup_workers():
    for i in range(num_workers):
        worker = threading.Thread(target=process_packet, args=(queues[i],))
        worker.daemon = True  # Make threads daemon so they don't prevent program termination
        workers.append(worker)
        worker.start()

def dispatch_packets():
    # This function needs to be adapted to continuously receive or simulate incoming packets
    # Example placeholder for continuous packet input
    import time
    while True:
        # Simulate incoming packets; replace this with real data or packet capture logic
        incoming_packets = [{'ip': f'192.168.1.{i % 10}', 'port': i % 1024, 'action': 'ACCEPT'} for i in range(20)]
        for i, packet in enumerate(incoming_packets):
            queues[i % num_workers].put(packet)
        time.sleep(10)  # Adjust time delay as necessary for your simulation or real packet interval

# Start packet processing on script load
setup_workers()
threading.Thread(target=dispatch_packets, daemon=True).start()
