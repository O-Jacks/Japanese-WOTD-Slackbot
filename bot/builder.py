def construct_payload(DIVIDER_BLOCK, HEADER_BLOCK, MESSAGE_BLOCK, MESSAGE_BLOCK2, DIVIDER_BLOCK2):

    return {
        "channel": "G0144B0RT9T",
        "username": "先生 (Sensei)",
        "icon_emoji": ":robot_face:",
        "text": ":wave: Your daily dose of motivation has arrived",
        "blocks": [
            DIVIDER_BLOCK,
            HEADER_BLOCK,
            MESSAGE_BLOCK,
            MESSAGE_BLOCK2,
            DIVIDER_BLOCK2
        ],
    }
