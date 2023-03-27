# Midjourney Showcase Image Downloader

I was pretty impressed by [Midjourney](https://www.midjourney.com) and their showcase, but was disappointed to see that the showcase would not let you download the images.

I discovered by poking around the website that the images do indeed exist in full quality, and decided to create a small script which would just download that day's trending images.

The script downloads both trending and all time faves from the gallery visible publicly, so no login, session token etc is required.

The images will be stored in a new folder with today's date in the form of `YYYYMMDD`

Have fun viewing and exploring AI art!

## Setup

1. Clone this repo

2. Install requirements by running

```bash
pip install -r requirements.txt
```

3. Run the program
```bash
python3 scraper.py
```

4. See the beautiful artwork downloaded
