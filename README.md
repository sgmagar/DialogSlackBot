# DialogSlackBot
A slack bot with the implementation of slack command and dialog.

### Installation instruction
1. Install [pipenv] (https://pypi.org/project/pipenv/)
2. Clone this repo and `cd DialogSlackBot`
3. Run `pipenv install`
4. Run `cp .env.example .env`

### Usage
1. Create a [Slack App] (https://api.slack.com/apps)
2. Update .env file with `client_id`, `client_secret`, `verification_token` of your app. Update `SECRET_KEY` as well
3. Run `pipenv shell`
4. Run `python manage.py migrate`
5. Run `python manage.py runserver`
6. Add `oauth redirect url` of slack app with the `http://localhost:8000/oauth-callback/`.
7. Create command `/dialog` and enable `interaction` and add url of `command` and `interacion`. Should use [ngrok] (https://ngrok.com/) or similar services for this.
8. Install app to your workspace with add to `slack button` on landing page.
9. From your workspace, use command `/dialog`  
