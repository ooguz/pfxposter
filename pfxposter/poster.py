import os
import re
import sys
import tempfile
import textwrap

import atoma
import requests
import toml
from mastodon import Mastodon

homedir = os.getenv("HOME")
config_file = "{}/.pfxposter".format(homedir)

def create_config(config_file):
    conf_includes = textwrap.dedent("""
        updated = 2020-08-24 00:00:00+00:00

        [mastodon]
        mastodon_url = "https://oyd.social"
        access_token = "your_access_token_here"

        [pixelfed]
        pixelfed_url = "https://pixelfed.social"
        username = "username"
        """)
    with open(config_file, "w") as f:
        f.write(conf_includes)
        print("Configuration file created please edit")
    sys.exit(0)


def syncronize(config_file, config, username, last_updated, mastodon):
    pixelfeed_get = requests.get('https://pixelfed.social/users/{}.atom'.format(username))
    pixelfeed = atoma.parse_atom_bytes(pixelfeed_get.content)

    latest_post = pixelfeed.entries[0]
    last_updated_atom = latest_post.updated

    if last_updated == last_updated_atom:
        print("Up-to-date")
        sys.exit(0)

    config['updated'] = last_updated_atom

    with open(config_file, "w") as f:
        toml.dump(config, f)
        print("Config file updated")

    image_name = latest_post.title.value
    image_url = re.search(r"(?P<url>https?://[^\s]+)", latest_post.summary.value) \
        .group("url") \
        .rstrip('">') \
        .replace("_thumb", "")
    tmp = tempfile.NamedTemporaryFile(suffix=".jpg")
    get_image = requests.get(image_url)
    tmp.write(get_image.content)
    mastodon_media = mastodon.media_post(tmp.name)
    mastodon.status_post(image_name, media_ids=mastodon_media['id'])
    print("Status posted: ", image_name)
    tmp.close()


def main():
    if not os.path.exists(config_file):
        create_config(config_file)

    config = toml.load(config_file)

    username = config['pixelfed']['username']
    last_updated = config['updated']

    mastodon = Mastodon(
            access_token=config['mastodon']['access_token'],
            api_base_url=config['mastodon']['mastodon_url']
    )
    syncronize(config_file, config, username, last_updated, mastodon)



