from threading import Timer
run = True

def test(interval):
	global run
	print("something")
	if run:
		Timer(interval, test).start()

test(2)
