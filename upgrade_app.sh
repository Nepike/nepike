#!/usr/bin/bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$script_dir"

VENV_DIR="./virtualenv"


> ./logs/deploy.log
exec > >(tee -a ./logs/deploy.log)
exec 2>&1


# TODO: make backup

git reset --hard
git pull origin main

source $VENV_DIR/bin/activate
pip install -r requirements.txt

rm -rf static
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

# TODO - create command
# python manage.py notify "Website updated successfully!" \
#      || echo "DEPLOY NOTIFICATION FAILED!"

pm2 restart nepike:web
pm2 restart nepike:tgbot
pm2 restart nepike:deploy-listener

# TODO ecosystem.config.js