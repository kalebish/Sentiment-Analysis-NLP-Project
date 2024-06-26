import gdown

url = f'https://drive.google.com/uc?export=download&id=1gy_xg86ieyPvzx5MSwJjKzvC_cp7CUcv'
output = 'reviews_dataset.csv'

gdown.download(url, output, quiet=False)



