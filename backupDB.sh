#!/bin/bash

retry=10
for i in $(seq 1 $retry);
do
    if gdrive upload api/data/db/user_action.db -p 1zOxDh07rlOgK1N8oLXWvX0HghvfZC9HL; then
        echo "upload complete"
#        curl --request POST \
#          --url https://api.line.me/v2/bot/message/push \
#          --header 'authorization: Bearer 91GhAd0IeyItMXs6e+Dl1sqYplxhXLMDj8ZzbnK57uqfgurw6IQ5TyjHoDd3S8XhPWVXWG9v$
#          --header 'content-type: application/json' \
#          --data '{
#            "to": "C9eb08306f28fd68ea5254ce123977be9",
#            "messages":[
#                {
#                    "type":"text",
#                    "text":"鴨發GO user_action已備份成功"
#                }
#            ]
#        }'
        break
    else
        echo "upload fail"
        sleep 1
    fi
done

for i in $(seq 1 $retry);
do
    if gdrive upload api/data/db/user_log.db -p 1zOxDh07rlOgK1N8oLXWvX0HghvfZC9HL; then
        echo "upload complete"
#        curl --request POST \
#          --url https://api.line.me/v2/bot/message/push \
#          --header 'authorization: Bearer 91GhAd0IeyItMXs6e+Dl1sqYplxhXLMDj8ZzbnK57uqfgurw6IQ5TyjHoDd3S8XhPWVXWG9v$
#          --header 'content-type: application/json' \
#          --data '{
#            "to": "C9eb08306f28fd68ea5254ce123977be9",
#            "messages":[
#                {
#                    "type":"text",
#                    "text":"鴨發GO user_log已備份成功"
#                }
#            ]
#        }'
        break
    else
        echo "upload fail"
        sleep 1
    fi
done
