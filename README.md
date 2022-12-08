# DiscordChatGPT
You can talk to ChatGPT's AI on Discord.

# TODO
askのレスポンスにprevious_convo, convo_id がないので次の会話に引き継げない。ライブラリ側対応待ち。   
会話スレッドの削除もできない対応待ち   

Memo:   

ChatGPTライブラリのask()メソッドのreturnを answer, previous_convo_id, conversation_idにして    
受け取り側で answer, previous_convo_id, conversation_id = chat.ask(message, previous_convo_id, conversation_id) するとマルチユーザ対応となる。   
