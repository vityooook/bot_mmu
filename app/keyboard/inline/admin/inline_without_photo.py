from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from handlers.callback.callback_data import AdminWithoutPhotoCallback



def without_photo() -> InlineKeyboardMarkup:
    """Inline keyboard for sending a newsletter without a photo"""
    builder = InlineKeyboardBuilder()

    builder.button(
        text="без фото",
        callback_data=AdminWithoutPhotoCallback(act="WITHOUT-PHOTO")
    )
    builder.adjust(1)
    return builder.as_markup()
