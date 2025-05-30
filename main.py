import streamlit as st
import pywhatkit
import pyautogui
import time
import datetime

st.title("📱 WhatsApp Scheduler")

phone = st.text_input("Enter phone number (with country code):", "+91")
message = st.text_area("Type your message:")
hour = st.number_input("Hour (24H format)", min_value=0, max_value=23, value=12)
minute = st.number_input("Minute", min_value=0, max_value=59, value=0)
second = st.number_input("Second", min_value=0, max_value=59, value=0)
upload = st.file_uploader("Attach a file (image/doc/pdf):", type=["png", "jpg", "pdf", "docx"])

if st.button("Schedule Message"):
    schedule_time = datetime.datetime.now().replace(hour=hour, minute=minute, second=second, microsecond=0)
    now = datetime.datetime.now()
    delay = (schedule_time - now).total_seconds()

    if delay < 0:
        st.error("⛔ Scheduled time is in the past!")
    else:
        st.success(f"📆 Message scheduled for {hour}:{minute}:{second}")

        # Delay until time
        time.sleep(delay)

        # Send message using pywhatkit
        pywhatkit.sendwhatmsg_instantly(phone, message, wait_time=15, tab_close=True)

        # Wait and click attachment (if file attached)
        if upload:
            st.info("📎 Sending attachment... Please keep WhatsApp Web open and ready.")
            time.sleep(10)  # wait for WhatsApp to load

            pyautogui.click(x=1250, y=950)  # position of attachment button (adjust as needed)
            time.sleep(2)
            pyautogui.write(upload.name)  # type the file path
            pyautogui.press("enter")
            time.sleep(2)
            pyautogui.press("enter")  # send


