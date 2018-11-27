# Book downloader from Telegram channels #

## Setup ##

[Get your **api_id** and **api_hash**](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id).
Then add environment variables **api_id** as **TG_API_ID** and **api_hash** as **TG_API_HASH**

### Install dependencies ###
`pip install -r requirements`

## Usage ##

`python downloader.py -c python_textbooks -kw 'Machine learning' 'Computer vision' -e .pdf`

-c/--channel - Telegram channel name

-kw/--key-words - Keywords to search for, ex: **Computer vision**, **Machine learning**

-e/--extensions - Book extensions, ex: pdf, epub, etc.

### Note ###
To group keywords use quotation marks `"` or `'`. Passing `Computer vision` and `'Computer vision'` are different, in first case you are looking for `computer` and `vision` keywords, in second `Computer vision` as one keyword

