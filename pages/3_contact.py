import streamlit as st 

st.title('Contact Form')
with st.form('user form'):
    col1, col2 = st.columns(2)
    
    with col1:
        FirstName = st.text_input('Enter First Name')
        Email = st.text_input('Enter Email address')
    with col2:
        LastName = st.text_input('Enter Last Name')
        Phone = st.number_input('Enter Phone Number')
    Message = st.text_area('Write Your Message')
    Select = st.selectbox('Select One',options=['-','Orange','Apple','Pineapple','Banana'])
    submitted = st.form_submit_button('Send Information')
   
   

    
st.sidebar.markdown(
    """
        <html>
            Copyright Lotus-Gold
        </html>
    """,
    unsafe_allow_html=True
) 