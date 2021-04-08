# IMDB ratings scrapper
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)

## General info
This code allows to scrap data like season, episode, rating, number of votes, title from series episodes.
Example usage code:

```Python
s_imdb = ScrapIMDB("url for imdb series episode guide page")
s_imdb.get_data(from_season, to_season)
s_imdb.data_to_csv('file.csv')
```

## Technologies
Project is created with:
* Python
* Pandas
* BeautifulSoup
