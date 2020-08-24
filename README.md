# pfxposter

A PixelFed to Mastodon and Twitter crossposter that is not written as intended. Due to the unknown error on pixelfed.social instance, Atom feeds are used for checking new posts. 

In order to post PixelFed entries to Twitter, you will need a Mastodon-Twitter crossposter, you may find them on web.

## Usage

There is a configuration file located at `~/.pfxposter`. 
```toml
updated = 2020-08-21 07:56:48+00:00

[mastodon]
mastodon_url = "https://oyd.social"
access_token = "your_access_token_here"

[pixelfed]
pixelfed_url = "https://pixelfed.social"
username = "ooguz"
```

pfxposter reads the configuration file, and runs frequently.

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
