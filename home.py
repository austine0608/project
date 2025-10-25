import streamlit as st 
# import webbrowser 

st.set_page_config(
    page_title = "Lotus-Gold Consulting"
)

st.title('Story Album')
st.sidebar.subheader('Lotus-Gold Consulting')

col1, col2, col3 = st.columns(3)

with col1:
    st.caption('Stressed Up')
    st.image('./images/1.png')
    st.button('Click Me',key='btn1')
    # if st.button("🎥 Watch on YouTube",key='btn1'):
    #     webbrowser.open_new_tab("https://www.youtube.com/watch?v=UVItFN6xwxI")
with col2:
    st.caption('Reletionship Issues')
    st.image('./images/2.png')
    st.button('Click Me',key='btn2')
    # if st.button("🎥 Watch on YouTube",key='btn2'):
    #     webbrowser.open_new_tab("https://www.youtube.com/watch?v=1J0veD3eGRs")
with col3:
    st.caption('Betrayal')
    st.image('./images/3.png')
    st.button('Click Me',key='btn3')
    # if st.button("🎥 Watch on YouTube",key='btn3'):
    #     webbrowser.open_new_tab("https://www.youtube.com/watch?v=bE0TZ79cBfw&t=60s")
    
st.markdown('---')

col1, col2, col3 = st.columns(3)

with col1:
    st.caption('Friendship')
    st.image('./images/4.png')
    st.button('Click Me',key='btn4')
    # if st.button("🎥 Watch on YouTube",key='btn4'):
    #     webbrowser.open_new_tab("https://www.youtube.com/watch?v=l7qalPE8NoY&t=43s")
with col2:
    st.caption('Sales Rep')
    st.image('./images/5.png')
    st.button('Click Me',key='btn5')
    # if st.button("🎥 Watch on YouTube",key='btn5'):
    #     webbrowser.open_new_tab("https://www.youtube.com/watch?v=PD-bRU8f5AY&t=9s")
with col3:
    st.caption('Partners')
    st.image('./images/6.png')
    st.button('Click Me',key='btn6')
    # if st.button("🎥 Watch on YouTube",key='btn6'):
    #     webbrowser.open_new_tab("https://www.youtube.com/watch?v=V_Rgiy-vm3c&t=240s")
    
st.markdown('---')

st.markdown(
    """
        <html>
            Copyright Lotus-Gold Consulting
        </html>
    """,
    unsafe_allow_html=True
)
    