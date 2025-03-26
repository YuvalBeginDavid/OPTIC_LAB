import streamlit as st
from PIL import Image

# טעינת תמונות
img_off = Image.open("lab_off.png")
img_on = Image.open("lab_on.png")

# כותרת
st.title('מעבדת חשמל - מתג אור')

# כפתור להדלקה וכיבוי אור
if st.button('הדלק/כבה אור'):
    # בודקים את המצב הנוכחי של הכפתור ומעדכנים את מצב התמונה
    if 'light_on' not in st.session_state:
        st.session_state.light_on = False  # מצב התחלתי

    st.session_state.light_on = not st.session_state.light_on  # שינוי מצב

# תצוגת התמונה המתאימה
if st.session_state.get('light_on', False):
    st.image(img_on, caption="אור דולק")
else:
    st.image(img_off, caption="אור כבוי")
