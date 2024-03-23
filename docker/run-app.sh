#!/usr/bin/env bash

set -e

role=${CONTAINER_ROLE:-api}

python3 -m venv src/venv/
source src/venv/bin/activate
pip3 install --upgrade pip
pip3 install -r src/requirements.txt

# APP
if [ "$role" = "app" ]; then
    sudo ln -sf /etc/supervisor/conf.d-available/app.conf /etc/supervisor/conf.d/app.conf

else
    echo "FOO Could not match the container role \"$role\""
    exit 1
fi

exec sudo supervisord -c /etc/supervisor/supervisord.conf
