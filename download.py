import asyncio
from pathlib import Path

import aiohttp
import requests

FILE_URL = 'https://www.gutenberg.org/files/1342/1342-0.txt'
CHUNK_SIZE = 94072
DESTINATION = r'C:\Users\victoria.gur\temp\services\123'

def get_size():
    try:
        response = requests.head(FILE_URL)
        response.raise_for_status()
        file_size = int(response.headers.get('Content-Length', 0))

        if not file_size:
            raise ValueError("\n No file size - not downloaded")
        print(f"\nFile size: {file_size} bytes")
        return file_size

    except requests.exceptions.RequestException as e:
        print(f"Error getting size {e}")
        raise


def test_get_size():
    get_size()


def download_file_in_chunks(url, destintion_path, chunk_size):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        print(f"\n HTTP {response.status_code}, {response.content}")
        with open(destintion_path, 'ab') as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    print(f"Writing chunk of {len(chunk)} bytes to {destintion_path}")
                    f.write(chunk)
                else:
                    print(f"Error no chunk")

        print(f"Downloaded to {destintion_path=}")

    except requests.exceptions.RequestException as e:
        print(f"Error making request {e}")
        raise

def test_download_file():
    download_file_in_chunks(url=FILE_URL, destintion_path=DESTINATION, chunk_size=int(CHUNK_SIZE))


#   refactoring - async download

DESTINATION_FOR_ASYNC = Path('C:/Users/victoria.gur/temp/services/777')

async def download_file_async(url, destination_path, chunk_size):
    response = requests.head(url)
    response.raise_for_status()
    file_size = int(response.headers.get('Content-Length', 0))

    if not file_size:
        raise ValueError("\n No file size - not downloaded")
    print(f"\nFile size: {file_size} bytes")

    try:
        with open(destination_path, 'wb') as f:
            f.truncate(file_size)

        tasks = []
        for start in range(0, file_size, chunk_size):
            end = min(start + chunk_size - 1, file_size - 1)
            task = asyncio.create_task(download_chunk_async(url, start, end, destination_path))
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        print(f"Downloaded {sum(results)} bytes in {len(tasks)} chunks to {destination_path}")

    except Exception as e:
        print(f"Download failed: {e}")
        raise


async def download_chunk_async(url, start, end, destination_path):
    headers = {"Range": f"bytes={start}-{end}"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            response.raise_for_status()
            content = await response.read()
    try:
        with open(destination_path, 'r+b') as f:
            f.seek(start)
            f.write(content)

        bytes_downloaded = len(content)
        print(f"Downloaded bytes {start}-{end} ({bytes_downloaded} bytes)")
        return bytes_downloaded

    except Exception as e:
        print(f"Chunk {start}-{end} failed: {e}")
        raise


async def main():
    await download_file_async(FILE_URL, DESTINATION_FOR_ASYNC, CHUNK_SIZE)


def test_async_download():
    asyncio.run(main())

