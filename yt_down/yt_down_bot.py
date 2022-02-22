#/yt_down https://www.youtube.com/watch?v=CrwRKsh5Y_A&list=LL&index=12
#/yt_down https://youtu.be/u-8KUMXQMzE
bot.answer_callback_query(call.id, text="Дата выбрана"); bot.answer_callback_query(call.id, show_alert=True, text="Дата выбрана")

bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")
bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Пыщь!")

#telegram.error.BadRequest: Message can't be edited


yt.streams.filter(
    file_extension='mp4'
    ).order_by('resolution').desc().last().download();
yt.streams.filter(
    progressive=True,
    file_extension='mp4'
    ).order_by('resolution').desc().last().download();

yt.streams.filter(
    progressive=True,
    file_extension='mp4'
    ).order_by('resolution').desc().first().default_filename;