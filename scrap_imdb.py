from content_parser import get_imdb_series_info
from requests import get
import pandas as pd


class ScrapIMDB:
    def __init__(self, season_one_url):
        self.url = season_one_url[:season_one_url.index('=') + 1]
        self.episodes_frame = []

    def get_data(self, start_season, end_season):
        episodes_data = []

        for season_num in range(start_season, end_season + 1):
            season_episodes = get_imdb_series_info(get(self.url + str(season_num)).text, season_num)
            episodes_data.extend(season_episodes)

        self.format_data(episodes_data)

    def format_data(self,episodes_data):
        self.episodes_frame = pd.DataFrame(episodes_data, columns=['season', 'episode', 'title', 'air_date',
                                                                   'rating', 'total_votes', 'desc'])
        self.episodes_frame['episode'] = self.episodes_frame['episode'].astype(int)
        self.episodes_frame['rating'] = self.episodes_frame['rating'].astype(float)
        self.episodes_frame['total_votes'] = self.episodes_frame['total_votes'].astype(int)
        self.episodes_frame['air_date'] = pd.to_datetime(self.episodes_frame['air_date'])

    def data_to_csv(self, file_name):
        self.episodes_frame.to_csv(file_name)

