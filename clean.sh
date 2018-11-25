#!/bin/bash

ABSPATH=$(readlink -f "$0") # /home/user/bin/foo.sh
SCRIPTPATH=$(dirname "$ABSPATH") # /home/user/bin
echo $SCRIPTPATH # /home/user/bin

cd $SCRIPTPATH/api/data/image
sudo find . -regex '.*[0-9a-f].jpg' -delete
