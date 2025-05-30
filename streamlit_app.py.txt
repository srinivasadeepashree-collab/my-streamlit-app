import streamlit as st
import pywhatkit
import time
import datetime

st.title("📱 WhatsApp Text Message Scheduler")

phone = st.text_input("Enter phone number (with country code):", "+91")
message = st.text_area("Type your message:")
hour = st.number_input("Hour (24H format)", min_value=0, max_value=23, value=12)
minute = st.number_input("Minute", min_value=0, max_value=59, value=0)
second = st.number_input("Second", min_value=0, max_value=59, value=0)

if st.button("Schedule Message"):
    schedule_time = datetime.datetime.now().replace(hour=hour, minute=minute, second=second, microsecond=0)
    now = datetime.datetime.now()
    delay = (schedule_time - now).total_seconds()

    if delay < 0:
        st.error("⛔ Scheduled time is in the past!")
    else:
        st.success(f"📆 Message scheduled for {hour:02d}:{minute:02d}:{second:02d}")
        st.info("⏳ Waiting to send message. Please keep your WhatsApp Web open.")

        time.sleep(delay)

        try:
            pywhatkit.sendwhatmsg_instantly(phone, message, wait_time=15, tab_close=True)
            st.success("✅ Message sent successfully!")
        except Exception as e:
            st.error(f"❌ Failed to send message: {e}")
