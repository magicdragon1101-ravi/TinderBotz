from analytics import Analytics

analytics = Analytics(path_file='../data/geomatches/geomatches.json')


print("You scraped {} profiles!".format(analytics.getAmountOfProfiles()))
print("The name {} occurred the most, namely {} times".format(analytics.getMostCommonName()[0], analytics.getMostCommonName()[1]))
print("The average age of the profiles is {}".format(analytics.getAverageAge()))
print("The average distance between you and the profiles is {} km".format(analytics.getAverageDistance()))
print("The average profile has {} images".format(analytics.getAverageAmountOfImages()))

# by default take all scraped geomatches, not counting their name as a parameter
analytics.getWordCloudOfNames()
analytics.getWordCloudOfBio()
for age in range(18, 26):
    analytics.getWordCloudOfNames(age=age)
    analytics.getWordCloudOfBio(age=age)


analytics.getDotMapOfMatches()
analytics.getHistogramOfMatches()
analytics.getHeatmapOfMatches()
analytics.getDelaunayTriangulation()
