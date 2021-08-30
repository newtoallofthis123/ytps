def ytps():
	from youtube_search import YoutubeSearch
	from youtubesearchpython import CustomSearch, VideoSortOrder, ChannelsSearch
	from rich.console import Console
	from rich.panel import Panel
	from rich.progress import Progress
	from rich.markdown import Markdown
	from rich.table import Table
	from rich import print
	from rich.text import Text
	import os
	import time
	import argparse

	console = Console()
	parser = argparse.ArgumentParser(prog='Youtube Terminal Play and Search')
	parser.add_argument("search_term", help="Youtube Search Query")
	parser.add_argument('-v','--version', action='version', version='%(prog)s 0.1')
	parser.add_argument("-o", help="Open Latest Video in mpv", action='store_true')
	parser.add_argument("-c", help="Search Only in this Channel")
	parser.add_argument("-l", help="More Relevant Results and more formatting, but slower", action='store_true')
	parser.add_argument("-a", help="About ytps and license", action='store_true')
	args = parser.parse_args()

	def search_yt(search_term):
		if args.o:
			customSearch = CustomSearch(search_term, VideoSortOrder.uploadDate, limit = 1)
			latest_video = customSearch.result()
			console.print(f':new: Latest Video from {latest_video["result"][0]["channel"]["name"]}')
			console.print(f'{latest_video["result"][0]["title"]} released {latest_video["result"][0]["publishedTime"]}.')
			watch_in_mpv = str.lower(input("Press any key to watch or exit to exit: "))
			if watch_in_mpv == "exit":
				quit()
			else:
				with Progress() as progress:
					task1 = progress.add_task("[green]Loading Player...", total=1000)
					while not progress.finished:
						time.sleep(0.01)
						progress.update(task1, advance=5)
				try:
					os.system(f'mpv --fullscreen --no-terminal --title="ytps - Playing {latest_video["result"][0]["title"]} from {latest_video["result"][0]["channel"]["name"]}"  {latest_video["result"][0]["link"]}')
				except:
					os.system(f'vlc {latest_video["result"][0]["link"]}')
			quit()
		if args.l:
			table = Table(title=Panel(f'Results for [red]{search_term.capitalize()}'), show_header=True, header_style="bold green")
			table.add_column("Released", style="dim", width=20)
			table.add_column("Title", style="yellow")
			table.add_column("Channel", style="cyan")
			table.add_column("Url", no_wrap=True, style="dim blue")

			results = YoutubeSearch(search_term, max_results=20).to_dict()
			for i in results:
				video_url_for_table = f'https://youtu.be/{i["id"]}'
				channel = i["channel"]
				channelsSearch = ChannelsSearch(channel, limit = 10, region = 'US')
				channelsSearch_content = channelsSearch.result()
				table.add_row(
					i["publish_time"],
					i["title"],
					f'[link={channelsSearch_content["result"][0]["link"]}]{channel}[/link]',
					video_url_for_table,
				)
			table.caption = ":zap: Made by [link=https://newtoallofthis123.github.io/About]NoobScience[/link]"
			console.print(table)
			quit()
		if args.c:
			channel_to_search = args.c
			channelsSearch = ChannelsSearch(channel_to_search, limit = 10, region = 'US')
			channelsSearch_content = channelsSearch.result()
			console.print(Panel(f'[red]{channel_to_search.capitalize()} Videos'), justify="center")
			quit()
		if args.a:
			about_content = "# YouTube Terminal Player and Search\n\n YouTube Terminal Player and Search is a simple tools to search [youtube]('https://youtube.com') from the terminal. It also gives you the url, so you can use [mpv]('https://mpv.io') to watch the video. This bypasses the need to use youtube at all. Also, ytps doesn't use the youtube REST API, it only uses programs that scrape youtube. ytps uses many modules that scrap youtube.\n\n*ytps doesn't on it's own provides no results. It only uses the below modules and compiles them to look beautiful and nice*. \n\n ## 3rd party modules used in ytps: \n\n *youtube-search-python*: [website]('https://github.com/alexmercerind/youtube-search-python') ; \n *youtube-search*: [website]('https://github.com/joetats/youtube_search') ; \n *rich*: [website]('https://github.com/willmcgugan/rich') \n\n ## License \n\n The MIT License (MIT) \n\n Copyright © 2021 NoobScience \n\n Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: \n\n The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. \n\n THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."
			about_md = Markdown(about_content)
			console.print(about_md)
			console.print("\n :zap: Made by [link=https://newtoallofthis123.github.io/About]NoobScience[/link]")
			quit()
		try:
			table = Table(title=Panel(f'Results for [red]{search_term.capitalize()}'), show_header=True, header_style="bold green")
			table.add_column("Released", style="dim", width=20)
			table.add_column("Title", style="yellow")
			table.add_column("Channel", style="cyan")
			table.add_column("Url", no_wrap=True, style="dim blue")

			results = YoutubeSearch(search_term, max_results=20).to_dict()
			for i in results:
				video_url_for_table = f'https://youtu.be/{i["id"]}'
				table.add_row(
					i["publish_time"],
					i["title"],
					i["channel"],
					video_url_for_table,
				)
			table.caption = ":zap: Made by [link=https://newtoallofthis123.github.io/About]NoobScience[/link]"
			console.print(table)
		except:
			for i in results:
				print(f'\n________________________________________\n{i["title"]}\n {i["publish_time"]}\t {i["channel"]}\t {i["duration"]}\t {i["views"]}\n Video Url: https://youtube.com{i["url_suffix"]}\n________________________________________')
			print("Made by NoobScience")
			print("Unable to use rich, use pip install rich and try again.")

	console.print("\n\t\t:compass:Youtube Search\n", style="bold red", justify="center")
	term_to_search = args.search_term
	search_yt(term_to_search)

if __name__ == '__main__':
	ytps()