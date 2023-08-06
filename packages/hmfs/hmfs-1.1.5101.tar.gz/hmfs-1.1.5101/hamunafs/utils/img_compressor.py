import asyncio
from codecs import escape_encode
from genericpath import isfile
import os
import resource
import shutil
import sys
import warnings
import numpy as np
from PIL import Image
from sklearn.cluster import MiniBatchKMeans

import json
import random
import aiohttp

QUANT = 50

async def compress(fname, ofname):
    if os.path.isfile(ofname):
        os.remove(ofname)

    img = Image.open(fname)
    img.convert('RGB')

    img = np.asarray(img)
    h, w = img.shape[:2]
    kmeans_n_clusters = min(QUANT, w * h)
                    
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore')
        kmeans_res = MiniBatchKMeans(n_clusters=kmeans_n_clusters, init='k-means++', max_iter=100, batch_size=32768, compute_labels=True, random_state=0).fit(img.reshape((-1,3)))

    palette = np.array(kmeans_res.cluster_centers_ + 0.5, dtype=np.uint8)

    img_palette_map = palette[kmeans_res.labels_].reshape(img.shape)

    img_palette = Image.fromarray(img_palette_map).convert('P', palette=Image.ADAPTIVE)

    img_palette.save(ofname + '.png', optimize=True)

    shutil.move(ofname + '.png', ofname)

    del img
    del img_palette
    del img_palette_map


async def request(method, url, headers={}, data=None):
    async with aiohttp.ClientSession() as session:
        func = session.get if method == 'get' else session.post

        resp = await func(url, headers=headers, data=data, timeout=10)
        return resp



async def download_file(url, ofname):
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url)
        with open(ofname, 'wb') as f:
            async for chunk in resp.content.iter_chunked(1024):
                f.write(chunk)


async def compress_jpeg(fname, ofname):
    try:
        url = 'https://tinypng.com/web/shrink'
        headers = {
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'X-Forwarded-For': get_random_ip()
        }
        result = None
        with open(fname, 'rb') as f:
            response = await request('post', url, headers, f) #requests.post(url, headers=headers, data=file, timeout=5)
            result = json.loads(await response.text())
        if result and result['input'] and result['output']:
            url = result['output']['url']
            await download_file(url, ofname)
            return ofname
        else:
            return None
    except Exception as e:
        print(e)
        return None

def get_random_ip():
    ip = []
    for i in range(4):
        ip.append(str(random.randint(0 if i in (2, 3) else 1, 254)))
    return '.'.join(ip)


async def image_compress(fname, ofname):
    ret = await compress_jpeg(fname, ofname)
    if not ret:
        return fname
    else:
        return ofname


async def compress_files(files):
    tasks = [
        image_compress(f, os.path.join(os.path.split(f)[0], 'compressed_{}'.format(os.path.split(f)[1]))) for f in files    
    ]

    results = await asyncio.gather(*tasks)

    return results

# results = asyncio.run(compress_files([
#     '/home/superpigy/图片/85_1654883759_hd.jpeg',
#     '/home/superpigy/图片/87_1654883850_hd.jpeg',
#     '/home/superpigy/图片/libno_16.45.24.141061_0.000.jpg'
# ]))

# print(results)