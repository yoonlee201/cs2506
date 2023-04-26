import streamlit as st

def home():
    convert = st.radio('Convert', options=['Binary', 'Hexadecimal', 'Decimal'])
    num_type = {'Binary': bin_to_num, 'Hexadecimal': hex_to_num, 'Decimal': dec_to_num}
    
    inst = st.text_input("Bin/Dec/Hex")
    try: 
        (not inst != '') or num_type[convert](inst)
    except ValueError:
        st.text(f"You did not enter in the correct format.")

    
def bin_to_num(num):
    dec = int(num, 2)
    st.text(f'Bin:\t{num}')
    st.text(f'Dec:\t{dec}')
    st.text(f'Hex:\t0x{dec:x}')
    
def hex_to_num(num):
    dec = int(num[2:], 16)
    st.text('Make sure your hexadecimal starts with \'0x\'')
    st.text(f'Bin:\t{dec:b}')
    st.text(f'Dec:\t{dec}')
    st.text(f'Hex:\t{num}')

def dec_to_num(num):
    dec = int(num)
    st.text(f'Bin:\t{dec:b}')
    st.text(f'Dec:\t{dec}')
    st.text(f'Hex:\t0x{dec:x}')