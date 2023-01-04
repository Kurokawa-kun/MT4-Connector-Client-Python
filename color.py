class color:
	Red = 0
	Green = 0
	Blue = 0
	Alpha = 0
	
    # コンストラクタ
#	def __init__(self, red, green, blue):
#		self.Red = red & 0xFF
#		self.Green = green & 0xFF
#		self.Blue = blue & 0xFF
#		self.Alpha = 0
#		return
	def __init__(self, red, green, blue, alpha = 0):
		self.Red = red & 0xFF
		self.Green = green & 0xFF
		self.Blue = blue & 0xFF
		self.Alpha = alpha & 0xFF
		return
	def GetRed(self):
		return self.Red
	def GetGreen(self):
		return self.Green
	def GetBlue(self):
		return self.Blue
	def GetAlpha(self):
		return self.Alpha
