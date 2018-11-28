# Book downloader from Telegram channels #

CLI for searching and downloading books from Telegram channels

## Setup ##

### Add environment variables ###

Get your Telegram [**api_id** and **api_hash**](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id).
Then add **api_id** as **TG_API_ID** and **api_hash** as **TG_API_HASH** environment variables.

### Install dependencies ###
`pip install -r requirements`

## Usage ##

``` bash
python books.py \
-a list \
-c python_textbooks \
-kw 'Machine learning' 'Computer vision' \
-e .pdf
```

+ -a/--action - Action to take: **download** or **list**\
+ -c/--channel - Telegram channel name\
+ -kw/--key-words - Keywords to search for, ex: **'Computer vision'** **'Machine learning'**\
+ -e/--extensions - Book extensions, ex: pdf epub etc.

### Note ###
+ Keywords are case insensitive, meaning `Machine Learning` and `machine learning` are equal.
+ To group keywords use quotation marks `"` or `'`. Passing `Computer vision` and `'Computer vision'` are different, in first case you are looking for `computer` and `vision` keywords, in second `computer vision` as one keyword.

+ Successive keywords or extensions are passed space separated
