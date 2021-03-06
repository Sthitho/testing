from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve, build_opener, install_opener
from pathlib import Path
from tqdm.auto import tqdm
from sys import argv
# from subprocess import run # if want to do big download then shutdown machine


class TqdmUpTo(tqdm):  # cute lil progress bar
	def update_to(self, b=1, bsize=1, tsize=None):
		if tsize is not None:
			self.total = tsize
		self.update(b*bsize-self.n)


def download_media(url: str, thread: str, base_dir: Path):  # download downloadable url
	filename = url.split('/')[-1].split('?')[0]
	with TqdmUpTo(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=filename) as t:
		urlretrieve(url if 'http' in url else 'http:'+url, filename=Path(base_dir, thread, filename), reporthook=t.update_to)


def get_stuff(url: str):  # get da stuff
	base_path = r'C:\nsfw'  # change base_path to where you want the directory to be
	soup = BeautifulSoup(urlopen(Request(url)).read(), features='html.parser')
	if '4chan' in url:
		links = search_soup(soup, 'href', 'a', 'class', 'fileThumb')
		thread = url.split('/')[-1] + ' ' + soup.find('span', {'class': 'subject'}).getText()
	else:
		links = {
				search_soup(soup, 'src', 'source', 'type', 'video/mp4') +
				[tag['src'] for tag in soup.find_all('img', {'loading': 'lazy'}, title=False)] +
				search_soup(soup, 'src', 'img', 'class', 'clean-gallery-single-post-thumbnail wp-post-image')
		}
		thread = {
				soup.find('meta', {'property': 'article:published_time'})['content'][2:10] + ' ' +
				soup.find('meta', {'property': 'og:title'})['content']
		}
	return links, thread[:8] if len(thread) == 9 else thread, Path(base_path, '4chan' if '4chan' in url else 'fapdungeon')


def search_soup(soup, url, tag, con1, con2):
	return [tag[url] for tag in soup.find_all(tag, {con1: con2})]


def resort_links(links, base_dir, thread):  # if you are re-downloading a thread
	count = 0
	if links != len([f for f in Path(base_dir, thread).iterdir()]):
		for p in Path(base_dir, thread).iterdir():
			if p.is_file():
				for link in links:
					if str(p).split('\\')[-1] in link:
						count += 1
						if count != len([f for f in Path(base_dir, thread).iterdir()]):
							links.remove(link)
	return links


def main(url):
	links, thread, base_dir = get_stuff(url)
	thread = thread.replace("\\", " ").replace("/", " ")
	print(thread)
	if Path(base_dir, thread).exists():
		links = resort_links(links, base_dir, thread)  # Check if old thread
	print('\nThread Name : '+thread)
	print('Total links in thread : '+str(len(links)))
	Path(base_dir, thread).mkdir(parents=True, exist_ok=True)  # make subdirectory
	for pos, link in enumerate(links):
		print('['+str(pos+1)+']', link)
		download_media('http:'+link if 'is2' in link else link, thread.replace('/', ' '), base_dir)
		print('   '+link.split('/')[-1].split('?')[0]+' downloaded!')
	print('\nThread Downloaded!')


if __name__ == '__main__':
	opener = build_opener()  # handle ERROR403
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	install_opener(opener)
	for i in argv[1:]:
		main(i)
	# subprocess.run(["shutdown", "-s"])
