# (C) 2021 KimMusic

from helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Selamat datang [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💬 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) membantu Anda memutar musik di grup melalui obrolan suara Telegram!**

💡 **Cari tahu semua perintah Bot dan cara kerjanya dengan mengklik » 📚 Tombol perintah !**

🔖 **Untuk mengetahui cara menggunakan bot ini, silakan klik » ❓Tombol Panduan Dasar!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Tambahan saya ke Grup ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ panduan dasar", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Commands", callback_data="cbcmds"),
                    InlineKeyboardButton("😎 𝒦𝒾𝓂", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "🏢 Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "🛶 Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hai !**

» **tekan tombol di bawah untuk membaca penjelasan dan melihat daftar perintah yang tersedia !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 Cmd Dasar", callback_data="cbbasic"),
                    InlineKeyboardButton("📕 Cmd Canggih", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("📘 Cmd Admin", callback_data="cbadmin"),
                    InlineKeyboardButton("📗 Cmd Sudo", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("📙 Cmd Owner", callback_data="cbowner")],
                [InlineKeyboardButton("🔙 Kembali", callback_data="cbguide")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **ini adalah perintah dasar**

🎵 [ VOICE CHAT PLAY CMD ]


/play (nama lagu) - memutar lagu dari youtube
/ytp (nama lagu) - putar lagu langsung dari youtube
/stream (membalas audio) - memutar lagu menggunakan file audio
/playlist - menampilkan daftar lagu dalam antrian
/song (nama lagu) - unduh lagu dari youtube
/search (nama video) - cari video dari youtube secara detail
/video (nama video) - unduh video dari youtube detail
/lyric - (nama lagu) lirik scrapper

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **ini adalah perintah canggih**

/start (dalam grup) - lihat status bot hidup
/reload - muat ulang bot dan segarkan daftar admin
/ping - periksa status bot ping
/uptime - periksa status waktu aktif bot
/id - tampilkan grup/id pengguna & lainnya

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **ini adalah perintah Admin**

/player - menampilkan status pemutaran musik
/pause - menjeda streaming musik
/resume - melanjutkan musik yang dijeda
/skip - lompat ke lagu berikutnya
/end - hentikan streaming musik
/join - undang userbot bergabung ke grup Anda
/leave - perintahkan bot pengguna untuk keluar dari grup Anda
/auth - pengguna resmi untuk menggunakan bot musik
/unauth - tidak sah untuk menggunakan bot musik
/control - buka panel pengaturan pemutar
/delcmd (on | off) - aktifkan / nonaktifkan fitur del cmd
/music (on / off) - nonaktifkan / aktifkan pemutar musik di grup Anda

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **ini adalah perintah Sudo**

/leaveall - perintahkan asisten untuk keluar dari semua grup
/stats - tampilkan statistik bot
/rmd - hapus semua file yang diunduh
/clear - hapus semua file .jpg
/eval (permintaan) - mengeksekusi kode
/sh (permintaan) - jalankan kode

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **ini adalah perintah Owner**


/stats - tampilkan statistik bot
/broadcast (membalas pesan) - mengirim pesan siaran dari bot
/block (id pengguna - durasi - alasan) - blokir pengguna untuk menggunakan bot Anda
/unblock (id pengguna - alasan) - buka blokir pengguna yang Anda blokir karena menggunakan bot Anda
/blocklist - menunjukkan daftar pengguna yang diblokir karena menggunakan bot Anda

📝 catatan: semua perintah yang dimiliki bot ini dapat dijalankan oleh pemilik bot tanpa ada pengecualian.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **BAGAIMANA CARA MENGGUNAKAN BOT INI ?:**

1.) **pertama, tambahkan saya ke grup Anda.**
2.) **kemudian jadikan saya sebagai admin dan berikan semua izin kecuali admin anonim.**
3.) **setelah menjadikan saya admin, ketik /reload di grup untuk memperbarui daftar admin.**
3.) **tambahkan @{ASSISTANT_NAME} ke grup Anda atau ketik /join untuk mengundangnya.**
4.) **nyalakan obrolan video terlebih dahulu sebelum mulai memutar musik.**

📌 **jika bot pengguna tidak bergabung ke obrolan video, pastikan jika obrolan video sudah diaktifkan, atau ketik /leave lalu ketik /join lagi.**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("📚 Daftar perintah", callback_data="cbhelp")],
                [InlineKeyboardButton("🗑 Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
async def cbback(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 hanya admin yang dapat menekan tombol ini !", show_alert=True)
    await query.edit_message_text(
        "**💡 ini adalah menu kontrol bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⏸ pause", callback_data="cbpause"),
                    InlineKeyboardButton("▶️ resume", callback_data="cbresume"),
                ],
                [
                    InlineKeyboardButton("⏩ skip", callback_data="cbskip"),
                    InlineKeyboardButton("⏹ stop", callback_data="cbend"),
                ],
                [InlineKeyboardButton("⛔ anti cmd", callback_data="cbdelcmds")],
                [InlineKeyboardButton("🗑 Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
async def cbdelcmds(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 hanya admin yang dapat menekan tombol ini !", show_alert=True)
    await query.edit_message_text(
        f"""📚 **ini adalah informasi fitur:**
        
**💡 Fitur:** hapus setiap perintah yang dikirim oleh pengguna untuk menghindari spam dalam grup!

❔ penggunaan:**

 1️⃣ Untuk menghidupkan fitur:
     » ketik `/delcmd on`
    
 2️⃣ Untuk mematikan fitur:
     » ketik `/delcmd off`
      
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbback")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hallo** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

» **tekan tombol di bawah untuk membaca penjelasan dan melihat daftar perintah yang tersedia !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 Cmd Dasar", callback_data="cblocal"),
                    InlineKeyboardButton("📕 Cmd Canggih", callback_data="cbadven"),
                ],
                [
                    InlineKeyboardButton("📘 Cmd Admin", callback_data="cblamp"),
                    InlineKeyboardButton("📗 Cmd Sudo", callback_data="cblab"),
                ],
                [InlineKeyboardButton("📙 Cmd Owner", callback_data="cbmoon")],
                [InlineKeyboardButton("🔙 Kembali", callback_data="cbstart")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **BAGAIMANA CARA MENGGUNAKAN BOT INI ?:**

1.) **pertama, tambahkan saya ke grup Anda.**
2.) **kemudian jadikan saya sebagai admin dan berikan semua izin kecuali admin anonim.**
3.) **setelah menjadikan admin saya, ketik /reload di grup untuk memperbarui daftar admin.**
3.) **tambahkan @{ASSISTANT_NAME} ke grup Anda atau ketik /join untuk mengundangnya.**
4.) **nyalakan obrolan video terlebih dahulu sebelum mulai memutar musik.**

📌 **jika bot pengguna tidak bergabung ke obrolan video, pastikan jika obrolan video sudah diaktifkan, atau ketik /leave lalu ketik /join lagi.**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblocal"))
async def cblocal(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **ini adalah perintah Dasar**

🎵 [ VOICE CHAT PLAY CMD ]

/play (nama lagu) - memutar lagu dari youtube
/ytp (nama lagu) - putar lagu langsung dari youtube
/stream (membalas audio) - memutar lagu menggunakan file audio
/playlist - menampilkan daftar lagu dalam antrian
/song (nama lagu) - unduh lagu dari youtube
/search (nama video) - cari video dari youtube secara detail
/video (nama video) - unduh video dari youtube detail
/lyric - (nama lagu) lirik scrapper

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadven"))
async def cbadven(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **ini adalah perintah canggih**

/start (dalam grup) - lihat status bot hidup
/reload - muat ulang bot dan segarkan daftar admin
/ping - periksa status bot ping
/uptime - periksa status waktu aktif bot
/id - tampilkan grup/id pengguna & lainnya

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblamp"))
async def cblamp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **ini adalah perintah Admin**

/player - menampilkan status pemutaran musik
/pause - menjeda streaming musik
/resume - melanjutkan musik yang dijeda
/skip - lompat ke lagu berikutnya
/end - hentikan streaming musik
/join - undang userbot bergabung ke grup Anda
/leave - perintahkan bot pengguna untuk keluar dari grup Anda
/auth - pengguna resmi untuk menggunakan bot musik
/unauth - tidak sah untuk menggunakan bot musik
/control - buka panel pengaturan pemutar
/delcmd (on | off) - aktifkan / nonaktifkan fitur del cmd
/music (on / off) - nonaktifkan / aktifkan pemutar musik di grup Anda

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblab"))
async def cblab(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **ini adalah perintah Sudo**

/leaveall - perintahkan asisten untuk keluar dari semua grup
/stats - tampilkan statistik bot
/rmd - hapus semua file yang diunduh
/clear - hapus semua file .jpg
/eval (permintaan) - mengeksekusi kode
/sh (permintaan) - jalankan kode

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmoon"))
async def cbmoon(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **ini adalah perintah Owner**

/stats - tampilkan statistik bot
/broadcast (membalas pesan) - mengirim pesan siaran dari bot
/block (id pengguna - durasi - alasan) - blokir pengguna untuk menggunakan bot Anda
/unblock (id pengguna - alasan) - buka blokir pengguna yang Anda blokir karena menggunakan bot Anda
/blocklist - menunjukkan daftar pengguna yang diblokir karena menggunakan bot Anda

📝 catatan: semua perintah yang dimiliki bot ini dapat dijalankan oleh pemilik bot tanpa ada pengecualian.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cmdhome"))
async def cmdhome(_, query: CallbackQuery):
    
    bttn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Command Syntax", callback_data="cmdsyntax")
            ],[
                InlineKeyboardButton("🗑 Close", callback_data="close")
            ]
        ]
    )
    
    nofound = "**tidak dapat menemukan lagu yang Anda minta**\n\n» **harap berikan nama lagu yang benar atau sertakan juga nama artis**"
    await query.edit_message_text(nofound, reply_markup=bttn)


@Client.on_callback_query(filters.regex("cmdsyntax"))
async def cmdsyntax(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Command Syntax** untuk memutar musik di **Obrolan Suara:**

• `/play (query)` - untuk memutar musik melalui youtube
• `/ytp (query)` - untuk memutar musik langsung melalui youtube

⚡ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cmdhome")]]
        ),
    )
