import urllib.request
import os
from os.path import isdir
from os.path import join

from tqdm import tqdm

url = "https://www.finisherpix.com/en/photos/7146/1561"
fid=urllib.request.urlopen(url)

webpage=fid.read().decode('utf-8')

quote_list = webpage.split('"')
link_list = [c for c in quote_list if 'https' in c]
image_list = [c for c in link_list if 'fp-zoom-us.s3.amazonaws.com' in c]

output_dir = './tri_images/'

if not isdir(output_dir):
	os.mkdir(output_dir)

for img_url in tqdm(image_list):
	urllib.request.urlretrieve(img_url, join(output_dir, img_url.split('/')[-1]))