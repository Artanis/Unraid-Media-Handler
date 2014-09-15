class Series(list):
	def _init_(self, name, season, episodes):
		super().__init__(episodes)
		self.name = name
		self.season = season
