class Series:
	def _init_(self, seriesName, season, numberOfEpisodes, episodeList):
		self.seriesName = seriesName
		self.season = season
		self.numberOfEpisodes = numberOfEpisodes
		self.episodeList = episodeList

	def getName(self):
		return self.seriesName

	def getSeason(self):
		return self.season

	def getnumberOfEpisodes(self):
		return self.numberOfEpisodes

	def getEpisode(self, numberOfEpisodes):
		return self.episodeList[numberOfEpisodes]