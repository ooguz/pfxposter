# pfxposter

![PyPI](https://img.shields.io/pypi/v/pfxposter)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pfxposter)
![GLWTS](https://img.shields.io/badge/license-GLWTS-success)
![PyPI - Status](https://img.shields.io/pypi/status/pfxposter)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/ooguz/pfxposter/issues)
![PyPI - Format](https://img.shields.io/pypi/format/pfxposter)
![GitHub followers](https://img.shields.io/github/followers/ooguz?label=Follow&style=social)

A PixelFed to Mastodon and Twitter crossposter that is not written as intended. Due to the unknown error on pixelfed.social instance, Atom feeds are used for checking new posts. 

In order to post PixelFed entries to Twitter, you will need a Mastodon-Twitter crossposter, you may find them on web.

## Installation
```
python3 -m pip instal pfxposter
```
Use of virtual enviroments is strongly recommended, requests package may override your OS vendored version.

## Usage

First, create a Mastodon application from the settings of your Mastodon instance. You can create it under "Development" menu in settings. When you have created your app, Mastodon will give you an access token. Write the token to your configurion file.

The configuration file is located at `~/.pfxposter`. 
```toml
updated = 2020-08-21 07:56:48+00:00

[mastodon]
mastodon_url = "https://oyd.social"
access_token = "your_access_token_here"

[pixelfed]
pixelfed_url = "https://pixelfed.social"
username = "ooguz"
```

pfxposter reads the configuration file, and runs frequently. Installation from `pip` should add a crontab entry, you can check it with the command:
```
crontab -l
```

From Mastodon to Twitter, you will need another cross-poster, there are some links below: 

* <https://crossposter.masto.donte.com.br/>
* <https://moa.party>

**DISCLAIMER: These services listed below are neither maintained nor recommended from the developer, these are listed only for general information.**

## License

```
              GLWTS(Good Luck With That Shit) Public License
            Copyright (c) Every-fucking-one, except the Author

Everyone is permitted to copy, distribute, modify, merge, sell, publish,
sublicense or whatever the fuck they want with this software but at their
OWN RISK.

                             Preamble

The author has absolutely no fucking clue what the code in this project
does. It might just fucking work or not, there is no third option.


                GOOD LUCK WITH THAT SHIT PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION, AND MODIFICATION

  0. You just DO WHATEVER THE FUCK YOU WANT TO as long as you NEVER LEAVE
A FUCKING TRACE TO TRACK THE AUTHOR of the original product to blame for
or held responsible.

IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.

Good luck and Godspeed.
```
