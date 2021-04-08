LINE API
===

[Send reply message](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)
---

### HTTP request
``` POST https://api.line.me/v2/bot/message/reply ```

### Request headers
**Content-Type**
```
application/json
```
**Authorization**
```
Bearer {channel access token}
```

### Request body
**replyToken** [String]
###### Reply token received via webhook
**messages** [Array of [message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects)]
###### Messages to send
###### Max: 5

##### Example request
```
curl -v -X POST https://api.line.me/v2/bot/message/reply \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-d '{
    "replyToken":"nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
    "messages":[
        {
            "type":"text",
            "text":"Hello, user"
        },
        {
            "type":"text",
            "text":"May I help you?"
        }
    ]
}'
```

---

[Send push message](https://developers.line.biz/en/reference/messaging-api/#send-push-message)
---

### HTTP request
```POST https://api.line.me/v2/bot/message/push```

### Request headers
**Content-Type**
```
application/json
```
**Authorization**
```
Bearer {channel access token}
```

### Request body

**to** [String]
###### ID of the target recipient. Use a `userId`, `groupId`, or `roomId` value returned in a [webhook event object](https://developers.line.biz/en/reference/messaging-api/#common-properties). Do not use the LINE ID found on LINE.

**messages** [Array of [message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects)]
###### Messages to send
###### Max: 5

**notificationDisabled** [Boolean] `Optional`
###### Default: false
- `true`: The user doesn't receive a push notification when the message is sent.
- `false`: The user receives a push notification when the message is sent (unless they have disabled push notifications in LINE and/or their device).

##### Example request
```
curl -v -X POST https://api.line.me/v2/bot/message/push \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-d '{
    "to": "U4af4980629...",
    "messages":[
        {
            "type":"text",
            "text":"Hello, world1"
        },
        {
            "type":"text",
            "text":"Hello, world2"
        }
    ]
}'
```

---

[Send multicast message](https://developers.line.biz/en/reference/messaging-api/#send-multicast-message)
---

##### Example request
```
curl -v -X POST https://api.line.me/v2/bot/message/multicast \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-d '{
    "to": ["U4af4980629...","U0c229f96c4..."],
    "messages":[
        {
            "type":"text",
            "text":"Hello, world1"
        },
        {
            "type":"text",
            "text":"Hello, world2"
        }
    ]
}'

```

---

[message
Object](https://developers.line.biz/en/reference/messaging-api/#message-event)
---

### Text message
##### Example json
```
// Text message example
{
    "type": "text",
    "text": "Hello, world"
}

// Text message example with LINE emoji
{
    "type": "text",
    "text": "$ LINE emoji $",
    "emojis": [
      {
        "index": 0,
        "productId": "5ac1bfd5040ab15980c9b435",
        "emojiId": "001"
      },
      {
        "index": 13,
        "productId": "5ac1bfd5040ab15980c9b435",
        "emojiId": "002"
      }
    ]
}

// Text message example with LINE original emoji
{
  "type": "text",
  "text": "\uDBC0\uDC84 LINE original emoji"
}
```
### Sticker message
##### Example json
```
{
  "type": "sticker",
  "packageId": "446",
  "stickerId": "1988"
}
```
### Image message
##### Example json
```
{
    "type": "image",
    "originalContentUrl": "https://example.com/original.jpg",
    "previewImageUrl": "https://example.com/preview.jpg"
}
```
### Video message
##### Example json
```
{
    "type": "video",
    "originalContentUrl": "https://example.com/original.mp4",
    "previewImageUrl": "https://example.com/preview.jpg",
    "trackingId": "track_id"
}
```
### Audio message
##### Example json
```
{
    "type": "audio",
    "originalContentUrl": "https://example.com/original.m4a",
    "duration": 60000
}
```
### Location message
##### Example json
```
{
    "type": "location",
    "title": "my location",
    "address": "1-6-1 Yotsuya, Shinjuku-ku, Tokyo, 160-0004, Japan", 
    "latitude": 35.687574,
    "longitude": 139.72922
}
```