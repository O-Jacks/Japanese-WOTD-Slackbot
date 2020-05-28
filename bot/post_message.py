import os
from slack import WebClient
from dotenv import load_dotenv
from bot.builder import construct_payload
from utils.random_quote  import get_translations

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

# Initialize a Web API client
slack_web_client = WebClient(token=SLACK_BOT_TOKEN)


def post_quote_to_channel():
    trans_dict1, trans_dict2, trans_dict3, trans_dict4, wotd_img, count = get_translations()
    print("Count:", count)

    if count == 4:
        jap_wotd = trans_dict1['japanese_word-0']
        rom_wotd = trans_dict1['romaji_word-0']
        eng_wotd = trans_dict1['english_word-0']

        src = wotd_img['img-src']
        alt = wotd_img['img-alt']
        
        jap_ex1 = trans_dict2['japanese_word-1']
        rom_ex1 = trans_dict2['romaji_word-1']
        eng_ex1 = trans_dict2['english_word-1']

        jap_ex2 = trans_dict3['japanese_word-2']
        rom_ex2 = trans_dict3['romaji_word-2']
        eng_ex2 = trans_dict3['english_word-2']

        jap_ex3 = trans_dict4['japanese_word-3']
        rom_ex3 = trans_dict4['romaji_word-3']
        eng_ex3 = trans_dict4['english_word-3']

        # Get the onboarding message payload
        message = construct_payload(
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*<https://www.japanesepod101.com/japanese-phrases/|:japan: :japanese_castle: :bamboo: :dango: :dolls: :koko: *Today's Japanese word is*:>*"
                }
            },
            {
                "type": "section",
                "accessory": {
                    "type": "image",
                    "image_url": f"{src}",
                    "alt_text": f"{alt}"
			    },
                "text": {
                    "type": "mrkdwn",
                    "text": f"\n *{jap_wotd}* ({rom_wotd}) = {eng_wotd}"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Examples:* \n *{jap_ex1}* \n ({rom_ex1}) \n\n = {eng_ex1} \n\n\n *{jap_ex2}* \n ({rom_ex2}) \n\n = {eng_ex2} \n\n\n *{jap_ex3}* \n ({rom_ex3}) \n\n = {eng_ex3}"
                }
            },
            {
                "type": "divider"
            })

        print("Success!")
        response = slack_web_client.chat_postMessage(**message)
    else:
        print("ERROR!!!!!")
        
        
    #     {
    #     "type": "section",
    #     "text": {
    #             "type": "mrkdwn",
    #             "text": "*Your daily dose of Japanese* :japan: :japanese_castle: :bamboo: :dango: :dolls: :koko:"
    #     }
    # },
    #     {
    #     "type": "divider"
    # },
    #     {
    #     "type": "section",
    #     "text": {
    #         "type": "mrkdwn",
    #         "text": f"The test of the artist does not lie in the will with which he goes to work, but in the excellence of the work he produces... *By <{link}|{author}>*"
    #     }
    # })
    # Post the onboarding message in Slack
   

# def post_quote_to_channel():
#     quote = get_translations()
#     print(quote)
#     author = quote['japanese_word-0']
#     message = construct_payload(
#         {
#         "type": "section",
#         "text": {
#                 "type": "mrkdwn",
#                 "text": "*Your daily dose of Japanese* :japan: :japanese_castle: :bamboo: :dango: :dolls: :koko:"
#         }
#     },
#         {
#         "type": "divider"
#     },
#         {
#         "type": "section",
#         "text": {
#             "type": "mrkdwn",
#             "text": f"The test of the artist does not lie in the will with which he goes to work, but in the excellence of the work he produces... *By <{link}|{author}>*"
#         }
#     })
#     response = slack_web_client.chat_postMessage(**message)