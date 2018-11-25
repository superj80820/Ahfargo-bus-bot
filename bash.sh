#!/bin/bash

ABSPATH=$(readlink -f "$0") # /home/user/bin/foo.sh
SCRIPTPATH=$(dirname "$ABSPATH") # /home/user/bin
echo $SCRIPTPATH # /home/user/bin

sudo chown www-data:www-data $SCRIPTPATH/api/__init__.py
sudo chown www-data:www-data $SCRIPTPATH/api/data/db/user_action.db 
sudo chown www-data:www-data $SCRIPTPATH/api/data/image

