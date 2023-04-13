from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pause",
            description=f"Pause The Current Playing Stream On VideoChat .",
            thumb_url="https://telegra.ph/file/5cb5424eef2c11b5bbc9b.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Resume",
            description=f"Resume The Pause Stream On VideoChat  ",
            thumb_url="https://telegra.ph/file/5cb5424eef2c11b5bbc9b.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Skip",
            description=f"Skip The Current Playing Stream On VideoChat And Moves To The Next Stream.",
            thumb_url="https://telegra.ph/file/5cb5424eef2c11b5bbc9b.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="End",
            description="End The Current Playing Stream On VideoChat.",
            thumb_url="https://telegra.ph/file/5cb5424eef2c11b5bbc9b.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="Shuffle",
            description="Shuffle The Queued Songs In Playlist",
            thumb_url="https://telegra.ph/file/5cb5424eef2c11b5bbc9b.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Loop",
            description="Loop The Current Playing Track On VideoChat",
            thumb_url="https://telegra.ph/file/5cb5424eef2c11b5bbc9b.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
