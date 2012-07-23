time = Time()
time.hours = 11
time.minutes = 59
time.seconds = 30


class Time:
	def __init__(self, hours=0, minutes=0, seconds=0):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def makeTime(self, seconds):
		self.hours = seconds // 3600
		self.minutes = (seconds%3600) // 60
		self.seconds = seconds%60
		return time
	
	def increment(time, seconds):
		time.seconds = time.seconds + seconds
		while time.seconds >= 60:
			time.seconds = time.seconds - 60
			time.minutes = time.minutes + 1
		while time.minutes >= 60:
			time.minutes = time.minutes - 60
			time.hours = time.hours + 1

	def convertToSeconds(t):
		minutes = t.hours * 60 + t.minutes
		seconds = minutes * 60 + t.seconds
		return seconds

	def addTime(t1, t2):
		seconds = convertToSeconds(t1) + convertToSeconds(t2)
		return makeTime(seconds)

	def addTime(t1, t2):
		seconds = convertToSeconds(t1) + convertToSeconds(t2)
		return makeTime(seconds)

printthis = Time.makeTime(360)
print printthis