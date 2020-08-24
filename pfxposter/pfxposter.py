#!/usr/bin/env python3

from mastodon import Mastodon
import requests
import atoma 
import re
import tempfile
import toml 
import os

homedir = os.getenv("HOME")
config_file = "{}/.pfxposter".format(homedir)

if os.path.exists(config_file) == False:
    conf_includes = 'updated = 2020-08-24 00:00:00+00:00\n\n[mastodon]\nmastodon_url = "https://oyd.social"\naccess_token = "your_access_token_here"\n\n[pixelfed]\npixelfed_url = "https://pixelfed.social"\nusername = "username"'
    with open(config_file, "w") as f:
        f.write(conf_includes)
        print("Configuration file created please edit")
    os._exit(0)

config = toml.load(config_file)

username = config['pixelfed']['username']
last_updated = config['updated']

mastodon = Mastodon(
    access_token = config['mastodon']['access_token'],
    api_base_url = config['mastodon']['mastodon_url']
)

def main():

	pixelfeed_get = requests.get('https://pixelfed.social/users/{}.atom'.format(username))
	pixelfeed = atoma.parse_atom_bytes(pixelfeed_get.content)

	latest_post = pixelfeed.entries[0]
	last_updated_atom = latest_post.updated
	if last_updated == last_updated_atom:
		print("Up-to-date")
		os._exit(0)
	config['updated'] = last_updated_atom
	with open(config_file, "w") as f:
		toml.dump(config, f)
		print("Config file updated")
	image_name = latest_post.title.value
	image_url = re.search("(?P<url>https?://[^\s]+)", 	latest_post.summary.value).group("url").rstrip('">').replace("_thumb", "")
	tmp = tempfile.NamedTemporaryFile(suffix=".jpg")
	get_image = requests.get(image_url)
	tmp.write(get_image.content)
	mastodon_media = mastodon.media_post(tmp.name)
	mastodon.status_post(image_name, media_ids=mastodon_media['id'])
	print("Status posted: ", image_name)
	tmp.close()
if __name__ == "__main__":
	main()
