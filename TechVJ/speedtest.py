from pyrogram import filters
from pyrogram.types import Message
import speedtest
from .. import app

@app.on_message(filters.command("speedtest"))
async def speedtest_command(client, message: Message):
    try:
        # Initialize Speedtest
        st = speedtest.Speedtest()
        st.get_best_server()  # Select the best server
        
        # Measure download and upload speeds (in Mbps)
        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000
        ping = st.results.ping

        # Format the response
        response = (
            f"🌐 **Internet Speed Test Results**:\n"
            f"Download Speed: {download_speed:.2f} Mbps\n"
            f"Upload Speed: {upload_speed:.2f} Mbps\n"
            f"Ping: {ping:.2f} ms"
        )

        await message.reply_text(response)
    except Exception as e:
        await message.reply_text(f"Error running speed test: {str(e)}")
