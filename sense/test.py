#!/usr/bin/env python3
import argparse
import threading
from time import sleep
from sense_hat import SenseHat

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--status", type=str, required=True)
args = parser.parse_args()

sense = SenseHat()
current_status = args.status
current_count = 0

def status():
	while True:
		if current_status == "wait":
			i = 0
			while current_status == "wait":
				i += 1
				if i == 4: i = 0
				sense.load_image("wait" + str(i) + ".png")
				sleep(0.5)
		else:
			sense.load_image(current_status + ".png")

def count():
	while True:
		global current_count
		print(str(current_count))
		current_count += 1
		sleep(1)

def main():
	status_thread = threading.Thread(target = status)
	count_thread = threading.Thread(target = count)
	
	status_thread.start()
	count_thread.start()
	
	status_thread.join()
	count_thread.join()
	
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sense.clear()
