# -------------------- MODULES --------------------
"""imported BeautifulSoup class from the bs4 module"""
from bs4 import BeautifulSoup

"""imported requests module"""
import requests


## day45 project: 100 movies that you must watch
# -------------------- WORKING WITH INTERNET ARCHIVE DATA --------------------
"""variable to store address"""
iaEndpoint = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

"""variable to store the response"""
iaResponse = requests.get(url=iaEndpoint)
iaResponse.raise_for_status()

"""variable tp store the data"""
iaWebpage = iaResponse.text

"""created the soup object"""
soup = BeautifulSoup(iaWebpage, "html.parser")

"""list to store all the movies name"""
iaMoviesList = []

"""getting all the movies"""
iaMovies = soup.findAll(name="h3", class_="title")

"""loop to iterate over iaMovies"""
for movie in iaMovies:
    iaMoviesList.append(movie.getText())

print(iaMoviesList)

"""moving the data to a text file"""
with open("movies.txt", "a") as file:
    for movie in range(-1, -(len(iaMoviesList) + 1), -1):
        file.write(f"{iaMoviesList[movie]}\n")



















# # -------------------- WORKING WITH HACKERNEWS --------------------
# """variable to store the address for hackernews"""
# hnEndpoint = "https://news.ycombinator.com"
#
# """variable to store the response"""
# hnResponse = requests.get(url=hnEndpoint)
# hnResponse.raise_for_status()
#
# """variable to store the text from the hackernews website"""
# hnWebpage = hnResponse.text
#
# """created soup object"""
# soup = BeautifulSoup(hnWebpage, "html.parser")
#
# """list to store news texts"""
# hnNewsTexts = []
#
# """list to store news links"""
# hnNewsLinks = []
#
# """getting the details of the news"""
# hnNews = soup.findAll(name="span", class_="titleline")
#
# """loop to iterate over hnNews"""
# for news in hnNews:
#     hnNewsTexts.append(news.contents[0].text)
#     hnNewsLinks.append(news.contents[0].get("href"))
#
# """list to store all the votes"""
# hnNewsVotes = [int(score.getText().split(' ')[0]) for score in soup.findAll(name="span", class_="score")]
#
# print(hnNewsTexts)
# print(hnNewsLinks)
# print(hnNewsVotes)
#
# """printing the news and link with highest number of votes"""
# highestVoteIndex = hnNewsVotes.index((max(hnNewsVotes)))
# print(highestVoteIndex)
# print(hnNewsTexts[highestVoteIndex], hnNewsLinks[highestVoteIndex])


# -------------------- WORKING WITH HTML PARSING --------------------

# """getting the data from the index.html file"""
# with open("index.html") as file:
#     contents = file.read()
#
# """created soup object"""
# soup = BeautifulSoup(contents, "html.parser")

# """getting all anchor tags"""
# allAnchorTags = soup.find_all(name="a")

# """getting all anchor tags"""
# print(allAnchorTags)

# for i in allAnchorTags:
#     # """getting the texts of anchor tags"""
#     # print(i.getText())
#
#     """getting all the href of anchor tags"""
#     print(i.get("href"))

# """getting particulars"""
# collegeUrl = soup.select_one("p a").get("href")
# print(collegeUrl)