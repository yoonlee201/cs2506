# @author Yoonje Lee
# @version 0.0.0

# TO-DO:  1. uj
#         2. register name
#         3. instuction for restriction (ex. hex must have 0x, imm must be hex)
#______________________________________#
    
import streamlit as st
import opcode_dictionary as opd

'''
HOME
    This function makes the over view of the opcode instruction converter
'''
def home():
    
    col1, col2= st.columns(2)
    with col1:
        convert = st.radio('Convert', options=['Instruction -> Opcode', 'Opcode -> Instruction'])
    
    inst = st.text_input("Instruction / Opcode ( inst rd, rs1, rs2 )")
    
    # converting from instuction to op code
    if convert == 'Instruction -> Opcode':
        try: 
            (not inst != '') or opd.print_opcode(inst.split())
        except ValueError:
            st.text(f"You did not enter in the correct format.\nex. add x8, x9, x20")
    # converting from opcode to instruction     
    else:
        with col2:
            num = st.radio('Num', options=['Hex', 'Bin'])
        
        try: 
            code = (num == 'Hex') and f'{int(inst[2:], 16):032b}' or f'{int(inst, 2):032b}'
            (not inst != '') or opd.print_inst(code)
        except ValueError:
            st.text(f"You did not enter in the correct format.")
