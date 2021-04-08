from bs4 import BeautifulSoup


def vote_to_number(vote):
    return vote.replace(',', '').replace('(', '').replace(')', '')


def get_imdb_series_info(response_text, season_num):
    html_content = BeautifulSoup(response_text, 'html.parser')
    episode_blocks = html_content.find_all('div', class_='info')
    ep_data = []
    for ep in episode_blocks:
        season = season_num
        episode = ep.meta['content']
        title = ep.a['title']
        air_date = ep.find('div', class_='airdate').text.strip()
        print(air_date)
        rating = ep.find('span', class_='ipl-rating-star__rating').text
        total_votes = vote_to_number(ep.find('span', class_='ipl-rating-star__total-votes').text)
        desc = ep.find('div', class_='item_description').text.strip()
        ep_data.append([season_num, episode, title, air_date, rating, total_votes, desc])
    return ep_data
