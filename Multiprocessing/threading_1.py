import threading
from queue import Queue
from urllib.request import urlretrieve
from sys import argv
import os


class DownloadHref(threading.Thread):
    def __init__(self, queue, destfolder):
        super(DownloadHref, self).__init__()
        self.queue = queue
        self.destfolder = destfolder
        self.daemon = True

    def run(self):
        while True:
            url = self.queue.get()
            try:
                self.download_url(url)
            except Exception as e:
                print(f'   Error: {e}')
            self.queue.task_done()

    def download_url(self, url):
        # change it to a different way if you require
        name = url.split('/')[-1]
        dest = os.path.join(self.destfolder, name)
        print(f'[{self.ident}] Downloading {url} -> {dest}')
        urlretrieve(url, dest)


def download(urls, destfolder, numthreads=4):
    queue = Queue()
    for url in urls:
        queue.put(url)

    for i in range(numthreads):
        t = DownloadHref(queue, destfolder)
        t.start()

    queue.join()



if __name__ == "__main__":
    download(argv[1:], os.getcwd())
# py threading_1.py http://en.wikipedia.org/wiki/1 http://en.wikipedia.org/wiki/2 http://en.wikipedia.org/wiki/3 http://en.wikipedia.org/wiki/4
