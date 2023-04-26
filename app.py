import streamlit as st
import opcode_converter as op
import num_converter as nc
from streamlit_option_menu import option_menu

# Title
st.title('CS 2506')
st.text('Author: Yoonje Lee')

# Sidebar for each page
st.sidebar.title('Navigation')
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=['Home', 'Opcode Calculator', 'Hex-Bin-Dec']
    )
    

    
if selected == 'Opcode Calculator':
    op.home()
    
elif selected == 'Hex-Bin-Dec':
    nc.home()
# else:
#     st.markdown(
#         'Welcome to GuardianTails, the one-stop platform where guardians can create their own voices and read any sentences with the voice!. Our website '
#         'allows you to upload your voice and imitate it for reading storybooks to '
#         'your kids, helping you stay connected with them even when you are not around. With GuardianStoryTime, '
#         'you can share the joy of storytelling and create lasting memories for your children. Follow these simple '
#         'steps to get started:')

#     st.text('Follow these simple steps to get started:')

#     st.subheader('Step 1: Upload Your Video')
#     st.markdown(
#         'Visit our "Video Upload" page and choose a video file with an extension like MP4 or AVI.'
#         'Once you have selected the video, click the "Upload Voice" button to submit your recording.'
#     )

#     st.subheader('Step 2: Add Text')
#     st.markdown(
#         'Next, navigate to the "Text Upload" section. Here, you can type or copy and paste the text of the story you '
#         'want your children to hear. Make sure the text matches the words spoken in your video recording to ensure a '
#         'seamless storytelling experience. Once you have entered the story text, click "Upload Text" to continue'
#     )
# # st.sidebar.radio('Pages', options=['Data Statistics', 'Data Header', 'Plot'])


