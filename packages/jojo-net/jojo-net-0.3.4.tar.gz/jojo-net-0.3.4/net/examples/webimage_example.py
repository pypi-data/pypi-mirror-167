#
# WebImage usage example
#

from net import WebImage


imgs = WebImage('black hole', 'png', count=5)
print(imgs.download_all())

# download images one by one
for index, img in enumerate(imgs.images):
    print(img.filename, img.file_ext, img.url)
    if not img.download(index):
        print("error downloading image of %s" % index)

