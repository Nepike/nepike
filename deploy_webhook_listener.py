
from flask import Flask, request, abort
import subprocess
import yaml
import os
from pathlib import Path
import requests
import telebot


CONFIG_PATH = Path(__file__).resolve().parent.parent / 'config.yml'
with open(CONFIG_PATH) as f:
	SITE_CONFIG = yaml.safe_load(f.read())

TGBOT_TOKEN = SITE_CONFIG["telegram_bot"]["token"]
DEPLOY_SECRET = SITE_CONFIG.get("deploy_secret", None)
DEPLOY_CHAT_ID = SITE_CONFIG['telegram_bot']['admin_chats'][0]['chat_id']
DEPLOY_CHAT_FIRST_MSG_ID = SITE_CONFIG['telegram_bot']['admin_chats'][0]['thread_msg']

app = Flask(__name__)

bot = telebot.TeleBot(TGBOT_TOKEN)


@app.route('/deploy_webhook', methods=['POST'])
def webhook():
	signature = request.headers.get("X-Gitlab-Token")

	bot.send_message(chat_id=DEPLOY_CHAT_ID,
					 text="🔧 Webhook received, starting deployment...",
					 reply_to_message_id=DEPLOY_CHAT_FIRST_MSG_ID,
					 disable_web_page_preview=False)

	if DEPLOY_SECRET != signature:
		bot.send_message(chat_id=DEPLOY_CHAT_ID,
						 text="❌ Deployment error:\nInvalid signature!",
						 reply_to_message_id=DEPLOY_CHAT_FIRST_MSG_ID,
						 disable_web_page_preview=False)
		abort(403, "Invalid signature")

	payload = request.get_json()
	if not payload:
		bot.send_message(chat_id=DEPLOY_CHAT_ID,
						 text="❌ Deployment error:\nNo payload received!",
						 reply_to_message_id=DEPLOY_CHAT_FIRST_MSG_ID,
						 disable_web_page_preview=False)
		return "No payload", 400

	commits = payload.get('commits', [])
	if commits:
		changes_message = "Изменения:\n"
		for commit in commits:
			commit_message = commit.get('message', '').strip()
			commit_url = commit.get('url', '')
			commit_id = commit.get('id', '')[:8]
			author_name = commit.get('author', {}).get('name', '')
			changes_message += f"- {commit_id} by {author_name}: <a href='{commit_url}'>{commit_message}</a>\n"
	else:
		changes_message = "Обновление прошло без новых коммитов."

	bot.send_message(chat_id=DEPLOY_CHAT_ID,
					 text=f"🔄 Deployment started successfully!\n{changes_message}",
					 parse_mode="HTML",
					 reply_to_message_id=DEPLOY_CHAT_FIRST_MSG_ID,
					 disable_web_page_preview=True)

	subprocess.Popen(["/bin/bash", os.path.join(os.path.dirname(__file__), 'upgrade_app.sh')])

	return "Deploy started", 200


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)