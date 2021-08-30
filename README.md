# YouTube Terminal Player and Search
YouTube Terminal Player and Search is a simple tools to search [youtube]('https://youtube.com') from the terminal. It also gives you the url, so you can use [mpv]('https://mpv.io') to watch the video. 
This bypasses the need to use youtube at all. Also, ytps doesn't use the youtube REST API, it only uses programs that scrape youtube. ytps uses many modules that scrap youtube.
*ytps doesn't on it's own provides no results. It only uses the below modules and compiles them to look beautiful and nice*.

### Installation

Pip Install
```bash
pip install ytps
```

Directly from Repository
```bash
git clone https://github.com/newtoallofthis123/ytps.git
```

```bash
pip install -r requirements.txt
```

## 3rd party modules used in ytps:
*youtube-search-python*: [website]('https://github.com/alexmercerind/youtube-search-python') ; 
*youtube-search*: [website]('https://github.com/joetats/youtube_search') ; 
*rich*: [website]('https://github.com/willmcgugan/rich') 

## Usage

1. General Usage

```bash
ytps "youtube_search_term"
```

2. Open latest video in mpv
```bash
ytps -o "youtube_search_term"
```

3. Open more relevant but slower results
```bash
ytps -l "youtube_search_term"
```

4. Play Url or Most Relevant Result based on string
```bash
ytps -p "youtube_search_term"
```

5. Channel Info
```bash
ytps -c "channel_name"
```

6. Video Info
```bash
ytps --info "video_url"
```

7. About
```bash
ytps -a "any_string"
```

8. Help
```bash
ytps --help
```

9. Version
```bash
ytps --version
```

## License 

### The MIT License (MIT) 

Copyright © 2021 NoobScience 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: 

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

>[Github](https://newtoallofthis123.github.io/ytps) 



>Made By [NoobScience](https://newtoallofthis123.github.io/About)