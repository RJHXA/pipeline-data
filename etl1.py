import zipfile
with zipfile.ZipFile('./nba-draft-basketball-player-data-19892021.zip', 'r') as zip_ref:
    zip_ref.extractall('./raw_data/')