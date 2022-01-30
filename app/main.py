# (c) @mehranalam-IRAN

import os
from PIL import Image
import random
from pyrogram import Client, filters
from helpers.markup_maker import MakeCaptchaMarkup
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery, ChatPermissions
from config import configBot

TARGETGROUP = configBot.GROUP_NAME

CaptchaBot = Client(
    session_name=configBot.SESSION_NAME,
    api_id=configBot.API_ID,
    api_hash=configBot.API_HASH,
    bot_token=configBot.BOT_TOKEN
)
EmojiBank = ['🐻', '🐔', '☁️', '🔮', '🌀', '🌚', '💎', '🐶', '🍩', '🌏', '🐸', '🌕', '🍏', '🐵', '🌙',
            '🐧', '🍎', '😀', '🐍', '❄️', '🐚', '🐢', '🌝', '🍺', '🍔', '🍒', '🍫', '🍡', '💣', '🍟',
            '🇮🇷', '🍑', '🍷', '🍧', '🍕', '🍵', '🐋', '🐱', '💄', '👠', '💰', '💸', '🎹', '📦', '📍',
            '🐊', '🦕', '🐬', '💋', '🦎', '🦈', '🦷', '🦖', '🐠', '🐟','💀', '🎃', '👮', '⛑️', '🪢', '🧶',
            '🧵', '🪡', '🧥', '🥼', '🥻', '🎩', '👑', '🎒', '🙊', '🐗', '🦋', '🦐', '🐀', '🎻', '🦔', '🦦', 
            '🦫', '🦡', '🦨', '🐇']

EmojiIndex= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 
            57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]



CaptchaDB ={}

def getCAPTCHAJPG():
    captchaAnswer = ""
    EmojiRandomSelect1 = random.choice(EmojiIndex)
    captchaAnswer = captchaAnswer + EmojiBank[EmojiRandomSelect1]+"."

    base_img = Image.open(r"BaseImage/base_image.jpg").convert('RGB')
    position = ((base_img.width - 520) , (base_img.height - 260))
    base_img.paste(Image.open(rf"EmojiFolder/{EmojiBank[EmojiRandomSelect1]}.png").resize((120 , 120)).rotate(120) , position,Image.open(rf"EmojiFolder/{EmojiBank[EmojiRandomSelect1]}.png").resize((120 , 120)).rotate(120))
    position = ((base_img.width - 160) , (base_img.height - 200))
    EmojiRandomSelect2 = random.choice(EmojiIndex)
    captchaAnswer = captchaAnswer + EmojiBank[EmojiRandomSelect2]+"."


    base_img.paste(Image.open(rf"EmojiFolder/{EmojiBank[EmojiRandomSelect2]}.png").resize((120 , 120)).rotate(80) , position,Image.open(rf"EmojiFolder/{EmojiBank[EmojiRandomSelect2]}.png").resize((120 , 120)).rotate(80))
    position = ((base_img.width - 420) , (base_img.height - 190))
    EmojiRandomSelect3 = random.choice(EmojiIndex)
    captchaAnswer = captchaAnswer + EmojiBank[EmojiRandomSelect3]+"."

    base_img.paste(Image.open(rf"EmojiFolder/{EmojiBank[EmojiRandomSelect3]}.png").resize((120 , 120)).rotate(40) , position,Image.open(rf"EmojiFolder/{EmojiBank[EmojiRandomSelect3]}.png").resize((120 , 120)).rotate(40))
    position = ((base_img.width - 240) , (base_img.height - 300))
    EmojiRandomSelect4 = random.choice(EmojiIndex)
    captchaAnswer = captchaAnswer + EmojiBank[EmojiRandomSelect4]+"."

    base_img.paste(Image.open(rf"EmojiFolder/{EmojiBank[EmojiRandomSelect4]}.png").resize((120 , 120)).rotate(90) , position,Image.open(rf"EmojiFolder/{EmojiBank[EmojiRandomSelect4]}.png").resize((120 , 120)).rotate(90))
    position = ((base_img.width - 400) , (base_img.height - 300))
    EmojiRandomSelect5 = random.choice(EmojiIndex)
    captchaAnswer = captchaAnswer + EmojiBank[EmojiRandomSelect5]+"."

    base_img.paste(Image.open(rf"EmojiFolder/{EmojiBank[EmojiRandomSelect5]}.png").resize((120 , 120)).rotate(50) , position,Image.open(rf'EmojiFolder/{EmojiBank[EmojiRandomSelect5]}.png').resize((120 , 120)).rotate(50))
    position = ((base_img.width - 300) , (base_img.height - 200))
    EmojiRandomSelect6 = random.choice(EmojiIndex)
    captchaAnswer = captchaAnswer + EmojiBank[EmojiRandomSelect6]

    base_img.paste(Image.open(rf"EmojiFolder/{EmojiBank[EmojiRandomSelect6]}.png").resize((120 , 120)).rotate(50) , position,Image.open(rf'EmojiFolder/{EmojiBank[EmojiRandomSelect6]}.png').resize((120 , 120)).rotate(50))
    
    base_img.save('captcha.jpg')

    return captchaAnswer


@CaptchaBot.on_message(filters.command("start"))
async def start_handler(_, event: Message):
    await event.reply_text("Hi, I am captcha bot by @mehranny")


@CaptchaBot.on_message(filters.chat(TARGETGROUP) & filters.new_chat_members)
async def welcome_handler(bot: Client, event: Message):
    user_ = await bot.get_chat_member(event.chat.id, event.from_user.id)
    await bot.delete_messages(
        chat_id=event.chat.id,
        message_ids=event.message_id
    )
        
    if event.from_user.id is None:
        await bot.send_message(
            chat_id=event.chat.id,
            text=f"{event.from_user.mention} again joined group without verifying!\n\n"
                    f"He can try again after 10 minutes.",
            disable_web_page_preview=True
        )
        await bot.restrict_chat_member(
            chat_id=event.chat.id,
            user_id=event.from_user.id,
            permissions=ChatPermissions(can_send_messages=False)
        )
        await bot.delete_messages(chat_id=event.chat.id,
                                    message_ids=CaptchaDB[event.from_user.id]["message_id"])
        
    else:
        await bot.restrict_chat_member(
            chat_id=event.chat.id,
            user_id=event.from_user.id,
            permissions=ChatPermissions(can_send_messages=False)
        )
        
        await bot.send_message(
            chat_id=event.chat.id,
            text=f"{event.from_user.mention}, to chat here, please verify that you are not a robot.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Verify Now", callback_data=f"._{str(event.from_user.id)}")]
                , [InlineKeyboardButton("🤠 Admin : Time out!", callback_data=f"admin_{str(event.from_user.id)}")]
            ])
        )


@CaptchaBot.on_callback_query()
async def buttons_handlers(bot: Client, cb: CallbackQuery):

    if cb.data.startswith("admin_"):
        if cb.from_user.status == "creator" or cb.from_user.status == "administrator":
            """❌  re-joined the group without verifying themselves. They can try again later."""
            await CaptchaBot.send_message(cb.message.chat.id, f"""Hey {cb.from_user.mention} ,❌  re-joined the group without verifying themselves. They can try again later.""" , disable_web_page_preview=True)
        else:
            pass
            await cb.answer("❌  You're not a admin ", show_alert=True)
            # TODO : ADD MESSAGE TO BANNED

    if cb.data.startswith("._"):
        __user = cb.data.split("_")[1]
        if cb.from_user.id != int(__user):
            await cb.answer("This Message is Not For You!", show_alert=True)
            return
        await cb.message.edit("Generating Captcha ...")
        Answer = getCAPTCHAJPG()
        text12 = Answer
        captchaAnswer = Answer.split(".")
        
        
        print("Done!")
        markup = [[], [], []]
        print(captchaAnswer)
        _emojis = ['🐻', '🐔', '☁️', '🔮', '🌀', '🌚', '💎', '🐶', '🍩', '🌏', '🐸', '🌕', '🍏', '🐵', '🌙',
                    '🐧', '🍎', '😀', '🐍', '❄️', '🐚', '🐢', '🌝', '🍺', '🍔', '🍒', '🍫', '🍡', '💣', '🍟',
                    '🇮🇷', '🍑', '🍷', '🍧', '🍕', '🍵', '🐋', '🐱', '💄', '👠', '💰', '💸', '🎹', '📦', '📍',
                    '🐊', '🦕', '🐬', '💋', '🦎', '🦈', '🦷', '🦖', '🐠', '🐟','💀', '🎃', '👮', '⛑️', '🪢', '🧶',
                    '🧵', '🪡', '🧥', '🥼', '🥻', '🎩', '👑', '🎒', '🙊', '🐗', '🦋', '🦐', '🐀', '🎻', '🦔', '🦦', 
                    '🦫', '🦡', '🦨', '🐇']
        print("Cleaning Answer Emojis from Emojis List ...")
        for a in range(len(captchaAnswer)):
            if captchaAnswer[a] in _emojis:
                _emojis.remove(captchaAnswer[a])
        show = captchaAnswer
        print("Appending New Emoji List ...")
        for b in range(9):
            show.append(_emojis[b])
        print("Randomizing ...")
        random.shuffle(show)
        count = 0
        print("Appending to ROW - 1")
        for _ in range(5):
            markup[0].append(InlineKeyboardButton(f"{show[count]}",
                                                    callback_data=f"_{str(cb.from_user.id)}_{show[count]}_{text12}"))
            count += 1   
        print("Appending to ROW - 2")
        for _ in range(5):
            markup[1].append(InlineKeyboardButton(f"{show[count]}",
                                                    callback_data=f"_{str(cb.from_user.id)}_{show[count]}_{text12}"))
            count += 1  
        print("Appending to ROW - 3")
        for _ in range(5):
            markup[2].append(InlineKeyboardButton(f"{show[count]}",
                                                    callback_data=f"_{str(cb.from_user.id)}_{show[count]}_{text12}"))
            count += 1
        print("Setting Up in Database ...")
        CaptchaDB[cb.from_user.id] = {
            "emojis": captchaAnswer,
            "mistakes": 0,
            "group_id": cb.message.chat.id,
            "message_id": None
        }
        print("Sending Captcha ...")
        __message = await bot.send_photo(
            chat_id=cb.message.chat.id,
            photo="captcha.jpg",
            caption=f"{cb.from_user.mention}, select all the emojis you can see in the picture. "
                    f"You are allowed only (3) mistakes.",
            reply_markup=InlineKeyboardMarkup(markup)
        )
        
        CaptchaDB[cb.from_user.id]["message_id"] = __message.message_id
        await cb.message.delete(revoke=True)

    elif cb.data.startswith("_"):
        __emoji = cb.data.split("_")[2]
        __user = cb.data.split("_")[1]
        __Answer = cb.data.split("_")[3]
        __Answer = __Answer.split(".")
        
        if cb.from_user.id != int(__user):
            await cb.answer("This Message is Not For You!", show_alert=True)
            return
        if CaptchaDB.get(__user) == None:
            CaptchaDB[__user] = 0
            CaptchaDB[__user+"e"] = 0
        if __emoji not in __Answer:
            CaptchaDB[__user+"e"] += 1
            await cb.answer("You pressed wrong emoji!", show_alert=True)
            n = 3 - CaptchaDB[__user+"e"]
            if n == 0:
                await CaptchaBot.send_message(cb.message.chat.id , f"""❌ Ops {cb.from_user.mention} re-joined the group without verifying themselves. They can try again later.""")
                await cb.message.delete(True)
                del CaptchaDB[cb.from_user.id]
                return
            markup = await MakeCaptchaMarkup(cb.message["reply_markup"]["inline_keyboard"], __emoji, "❌")
            await cb.message.edit_caption(
                caption=f"{cb.from_user.mention}, select all the emojis you can see in the picture. "
                        f"You are allowed only ({n}) mistakes.",
                reply_markup=InlineKeyboardMarkup(markup)
            )
            
            return
        else:
            #CaptchaDB.get(cb.from_user.id).get("emojis").remove(__emoji)
            print(CaptchaDB.get(__user))

            CaptchaDB[__user] = CaptchaDB.get(__user)+1
            markup = await MakeCaptchaMarkup(cb.message["reply_markup"]["inline_keyboard"], __emoji, "✅")
            print(__Answer)
            await cb.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(markup))
            if CaptchaDB.get(__user) == 6:
                del CaptchaDB[cb.from_user.id]
                print("hhhopp")
                await cb.answer("You Passed the Captcha!", show_alert=True)
                UserOnChat = await bot.get_chat_member(user_id=cb.from_user.id, chat_id=cb.message.chat.id)
                await bot.unban_chat_member(chat_id=cb.message.chat.id, user_id=cb.from_user.id)
                await CaptchaBot.send_message(cb.message.chat.id, f"""{configBot.WELCOMING_PASSED}""" , disable_web_page_preview=True)
                
                await cb.message.delete(True)
            await cb.answer()


CaptchaBot.run()
