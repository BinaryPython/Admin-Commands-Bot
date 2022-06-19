# Admin Commands Bot
 A Discord Bot, written in python, that gives Admins of a server several useful, semi-funny commands to use against problematic users in lieu of a ban. Or against a closer server just for funsies.

 This is by no means a finished product and I am still learning how to properly work with discord.py and it's various modules.

 For those interested, I have the discord library installed on my local environment via a Python Virtual Environment or venv, just to keep my regular install uncluttered by crap.

## Current Plans
- [x] Command that allows Admins of a server to randomize a certain user's display name on the server and prevent them from manually changing it back for a certain amount of time
- [ ] Filter Speech - Stop people from using curse words in chat by deleting messages that conain them
    - [ ] Maybe have an option where any curse word messasges are deleted, but the bot re-words the user's message to be more appropriate. Like "damn" turns into "dang", etc...
- [ ] "Russian Roulette" Banning; Emulate a 6-shooter with one loaded chamber. If you "roll the chamber" and it hits the loaded chamber, the user is banned.
- [ ] Bot Infrastructure
    - [ ] Limit Commmands to be used only by Server Admins
    - [ ] Link up all related command functions in Cogs (?)
    - [ ] Tailor down permissions to ONLY what the bot needs (currently running on a very liberal permissions scheme right now just for development)