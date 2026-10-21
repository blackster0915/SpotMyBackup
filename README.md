# SpotMyBackup
Backup and Restore your Spotify Playlists and "My Music".

This javascript based app allows you to backup all your playlists and import them in any other Spotify Account. It uses the OAuth-Functionality of Spotify to be able to handle your personal playlists. 

In consequence, no credentials or data is stored or processed on the Webserver itself.

This is a fork of [secuvera/SpotMyBackup](https://github.com/secuvera/SpotMyBackup), which is no longer maintained. The fork is updated to work with the Spotify Web API as of 2026 and is meant to run locally on your own computer.

## Changes in this fork
- Login uses Authorization Code with PKCE. Spotify removed the implicit grant flow and `localhost` redirect URIs in November 2025.
- Uses the endpoints and field names of the February 2026 Web API changes (`/me/playlists`, `/playlists/{id}/items`, `/me/library`).
- Tracks are uploaded in batches (100 per playlist request, 40 per library request), and rate limits (HTTP 429) are retried.
- Restored playlists are created as private.
- Playlists you only follow can't be read anymore (Spotify only returns tracks of playlists you own or collaborate on). They are backed up by name and followed again on import.
- Local files are skipped, the API can't add them.
- Large exports are downloaded as a Blob, so big libraries no longer fail.
- Access errors from Spotify are shown instead of failing silently.

## Run it locally (Windows)
You need [Python 3](https://www.python.org/) and a Spotify account with **Premium** to own the developer app (Spotify requires this for Development Mode apps since February 2026). The accounts you back up from or restore to don't need Premium.

1. Go to the [Spotify developer dashboard](https://developer.spotify.com/dashboard) with your Premium account and create an app:
   - Redirect URI: `http://127.0.0.1:8888/login.html` (exactly like this, `localhost` is not accepted)
   - API: Web API
2. In the app's *User Management*, add every other Spotify account you want to use (name + the e-mail address of that account, up to 5 users).
3. Double-click `start.bat`. On the first start it creates `config.json` from `config.example.json`. Put your app's Client ID into `client_id` there and reload the page.
4. Log in with the account to back up and click *Export*. To restore, reload the page, log in with the target account and *Import* the file.

On macOS or Linux, copy `config.example.json` to `config.json` and run `python3 serve.py`, then open `http://127.0.0.1:8888`.

`config.json` and exported backups are listed in `.gitignore`, so they don't end up in a commit.
