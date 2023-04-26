import streamlit as st
import re
class op_function:
    def __init__(self, inst, format, code, func3, func7, imm):
        self.inst = inst
        self.format = format
        self.code = code
        self.func3 = func3
        self.func7 = func7
        self.imm = imm
        
    
op_dict_opcode = [
     op_function('lb',       'IL', 0b0000011, 0b000, None, None),
     op_function('lh',       'IL', 0b0000011, 0b001, None, None),
    op_function('lw',       'IL', 0b0000011, 0b010, None, None),
    op_function('ld',       'IL', 0b0000011, 0b011, None, None),
    op_function('lbu',      'IL', 0b0000011, 0b100, None, None),
    op_function('lhu',      'IL', 0b0000011, 0b101, None, None),
    op_function('lwu',      'IL', 0b0000011, 0b110, None, None),
    op_function('addi',     'I', 0b0010011, 0b000, None, None),
    op_function('slli',     'I', 0b0010011, 0b001, 0b0000000, None),
    op_function('slti',     'I', 0b0010011, 0b010, None, None),
    op_function('sltiu',    'I', 0b0010011, 0b011, None, None),
    op_function('xori',     'I', 0b0010011, 0b100, None, None),
    op_function('srli',     'I', 0b0010011, 0b101, 0b0000000, None),
    op_function('srai',     'I', 0b0010011, 0b101, 0b0100000, None),
    op_function('ori',      'I', 0b0010011, 0b110, None, None),
    op_function('andi',     'I', 0b0010011, 0b111, None, None),
    op_function('auipc',    'U', 0b0010111, 0b000, None, None),
    op_function('addiw',    'I', 0b0011011, 0b000, None, None),
    op_function('slliw',    'I', 0b0011011, 0b001, 0b0000000, None),
    op_function('srliw',    'I', 0b0011011, 0b101, 0b0000000, None),
    op_function('sraiw',    'I', 0b0011011, 0b101, 0b0100000, None),
    op_function('sb',       'S', 0b0100011, 0b000, None, None),
    op_function('sh',       'S', 0b0100011, 0b001, None, None),
    op_function('sw',       'S', 0b0100011, 0b010, None, None),
    op_function('sd',       'S', 0b0100011, 0b011, None, None),
    op_function('add',      'R', 0b0110011, 0b000, 0b0000000, None),
    op_function('sub',      'R', 0b0110011, 0b000, 0b0100000, None),
    op_function('sll',      'R', 0b0110011, 0b001, 0b0000000, None),
    op_function('slt',      'R', 0b0110011, 0b010, 0b0000000, None),
    op_function('sltu',     'R', 0b0110011, 0b011, 0b0000000, None),
    op_function('xor',      'R', 0b0110011, 0b100, 0b0000000, None),
    op_function('srl',      'R', 0b0110011, 0b101, 0b0000000, None),
    op_function('sra',      'R', 0b0110011, 0b101, 0b0100000, None),
    op_function('or',       'R', 0b0110011, 0b110, 0b0000000, None),
    op_function('and',      'R', 0b0110011, 0b111, 0b0000000, None),
    op_function('lui',      'U', 0b0110111, 0b000, None, None),
    op_function('addw',     'R', 0b0111011, 0b000, 0b0000000, None),
    op_function('subw',     'R', 0b0111011, 0b000, 0b0100000, None),
    op_function('sllw',     'R', 0b0111011, 0b001, 0b0000000, None),
    op_function('srlw',     'R', 0b0111011, 0b101, 0b0000000, None),
    op_function('sraw',     'R', 0b0111011, 0b101, 0b0100000, None),
    op_function('beq',      'B', 0b1100011, 0b000, None, None),
    op_function('bne',      'B', 0b1100011, 0b001, None, None),
    op_function('blt',      'B', 0b1100011, 0b100, None, None),
    op_function('bge',      'B', 0b1100011, 0b101, None, None),
    op_function('bltu',     'B', 0b1100011, 0b110, None, None),
    op_function('bequ',     'B', 0b1100011, 0b111, None, None),
    op_function('jalr',     'I', 0b1100111, 0b000, None, None),
    op_function('jal',      'UJ', 0b1101111, 0b000, None, None),
    op_function('ecall',    'I', 0b1110011, 0b000, None, 0),
    op_function('ebreak',   'I', 0b1110011, 0b000, None, 1)
]

   
op_dict_inst = {
    'lb': op_function('lb',       'IL', 0b0000011, 0b000, None, None),
    'lh': op_function('lh',       'IL', 0b0000011, 0b001, None, None),
    'lw':op_function('lw',       'IL', 0b0000011, 0b010, None, None),
    'ld':op_function('ld',       'IL', 0b0000011, 0b011, None, None),
    'lbu':op_function('lbu',      'IL', 0b0000011, 0b100, None, None),
    'lhu':op_function('lhu',      'IL', 0b0000011, 0b101, None, None),
    'lwu':op_function('lwu',      'IL', 0b0000011, 0b110, None, None),
    'addi':op_function('addi',     'I', 0b0010011, 0b000, None, None),
    'slli':op_function('slli',     'I', 0b0010011, 0b001, 0b0000000, None),
    'slti':op_function('slti',     'I', 0b0010011, 0b010, None, None),
    'sltiu':op_function('sltiu',    'I', 0b0010011, 0b011, None, None),
    'xori': op_function('xori',     'I', 0b0010011, 0b100, None, None),
    'srli':op_function('srli',     'I', 0b0010011, 0b101, 0b0000000, None),
    'srli':op_function('srli',     'I', 0b0010011, 0b101, 0b0100000, None),
    'ori':op_function('ori',      'I', 0b0010011, 0b110, None, None),
    'andi':op_function('andi',     'I', 0b0010011, 0b111, None, None),
    'auipc':op_function('auipc',    'U', 0b0010111, 0b000, None, None),
    'addiw':op_function('addiw',    'I', 0b0011011, 0b000, None, None),
    'slliw':op_function('slliw',    'I', 0b0011011, 0b001, 0b0000000, None),
    'srliw':op_function('srliw',    'I', 0b0011011, 0b101, 0b0000000, None),
    'sraiw':op_function('sraiw',    'I', 0b0011011, 0b101, 0b0100000, None),
    'sb':op_function('sb',       'S', 0b0100011, 0b000, None, None),
    'sh':op_function('sh',       'S', 0b0100011, 0b001, None, None),
    'sw':op_function('sh',       'S', 0b0100011, 0b010, None, None),
    'sd':op_function('sd',       'S', 0b0100011, 0b011, None, None),
    'add':op_function('add',      'R', 0b0110011, 0b000, 0b0000000, None),
    'sub':op_function('sub',      'R', 0b0110011, 0b000, 0b0100000, None),
    'sll':op_function('sll',      'R', 0b0110011, 0b001, 0b0000000, None),
    'slt':op_function('slt',      'R', 0b0110011, 0b010, 0b0000000, None),
    'sltu':op_function('sltu',     'R', 0b0110011, 0b011, 0b0000000, None),
    'xor':op_function('xor',      'R', 0b0110011, 0b100, 0b0000000, None),
    'srl':op_function('srl',      'R', 0b0110011, 0b101, 0b0000000, None),
    'sra':op_function('sra',      'R', 0b0110011, 0b101, 0b0100000, None),
    'or':op_function('or',       'R', 0b0110011, 0b110, 0b0000000, None),
    'and':op_function('and',      'R', 0b0110011, 0b111, 0b0000000, None),
    'lui':op_function('lui',      'U', 0b0110111, 0b000, None, None),
    'addw':op_function('addw',     'R', 0b0111011, 0b000, 0b0000000, None),
    'subw':op_function('subw',     'R', 0b0111011, 0b000, 0b0100000, None),
    'sllw':op_function('sllw',     'R', 0b0111011, 0b001, 0b0000000, None),
    'srlw':op_function('srlw',     'R', 0b0111011, 0b101, 0b0000000, None),
    'sraw':op_function('sraw',     'R', 0b0111011, 0b101, 0b0100000, None),
    'beq':op_function('beq',      'B', 0b1100011, 0b000, None, None),
    'bne':op_function('bne',      'B', 0b1100011, 0b001, None, None),
    'blt':op_function('blt',      'B', 0b1100011, 0b100, None, None),
    'bge':op_function('bge',      'B', 0b1100011, 0b101, None, None),
    'bltu':op_function('bltu',     'B', 0b1100011, 0b110, None, None),
    'bequ':op_function('bequ',     'B', 0b1100011, 0b111, None, None),
    'jalr':op_function('jalr',     'I', 0b1100111, 0b000, None, None),
    'jal':op_function('jal',      'UJ', 0b1101111, 0b000, None, None),
   'ecall': op_function('ecall',    'I', 0b1110011, 0b000, None, 0),
    'ebreak':op_function('ebreak',   'I', 0b1110011, 0b000, None, 1)
}

def print_opcode(inst):
    
    op_code = op_dict_inst[inst[0]]
    
    match op_code.format:
        case 'R': print_R(op_code, inst)
        case 'I': print_I(op_code, inst)
        case 'IL': print_IL(op_code, inst)
        case 'S': print_S(op_code, inst)
        case 'B': print_B(op_code, inst)
        case 'U': print_U(op_code, inst)
    
def print_R(op_code: op_function, inst):
    
    rd = int(inst[1][1:-1])
    rs1 = int(inst[2][1:-1])
    rs2 = int(inst[3][1:])
    
    code_bin = f'{op_code.func7:07b}|{rs2:05b}|{rs1:05b}|{op_code.func3:03b}|{rd:05b}|{op_code.code:07b}'
    print__(code_bin)
   
def print_I(op_code: op_function, inst):
    
    rd = int(inst[1][1:-1])
    rs1 = int(inst[2][1:-1])
    imm = int(inst[3])
    code_bin = f'{imm:012b}|{rs1:05b}|{op_code.func3:03b}|{rd:05b}|{op_code.code:07b}'
    print__(code_bin)

def print_S(op_code: op_function, inst):
    rs2 = int(inst[1][1:-1])
    inst = re.findall(r'\d+',inst[2]) 
    imm = f'{int(inst[0]):012b}'
    rs1 = int(inst[1])
    print(rs2)
    
    code_bin = f'{imm[:-5]}|{rs2:05b}|{rs1:05b}|{op_code.func3:03b}|{imm[-5:]}|{op_code.code:07b}'
    print__(code_bin)
    
def print_IL(op_code: op_function, inst):
    rd = int(inst[1][1:-1])
    inst = re.findall(r'\d+',inst[2]) 
    imm = int(inst[0])
    rs1 = int(inst[1])
    
    code_bin = f'{imm:012b}|{rs1:05b}|{op_code.func3:03b}|{rd:05b}|{op_code.code:07b}'
    print__(code_bin)
     
def print_B(op_code: op_function, inst):
    rs1 = int(inst[1][1:-1])
    rs2 = int(inst[2][1:-1])
    imm = f'{int(inst[3][2:], 16):012b}'
    
    code_bin = f'{imm[0]}{imm[-11:-5]}|{rs2:05b}|{rs1:05b}|{op_code.func3:03b}|{imm[-5:-1]}{imm[1]}|{op_code.code:07b}'
    print__(code_bin)

def print_U(op_code: op_function, inst):
    rd = int(inst[1][1:-1])
    imm = int(inst[2][2:],16)
    code_bin = f'{imm:020b}|{rd:05b}|{op_code.code:07b}'
    print__(code_bin)  

def print__(code_bin):
    st.text(f'Code: \t\t{code_bin}')
    st.text(f'Binary: \t{code_bin.replace("|", "")}')
    st.text(f'Hexadecimal:\t0x{int(code_bin.replace("|", ""), 2):07x}')
    
    
def print_inst(code):
    print(code)
    op_code = [item for item in op_dict_opcode if item.code == int(code[-7:], 2)]
    
    match op_code[0].format:
        case 'R': print_R_inst(op_code[0], code)
        case 'I': print_I_inst(op_code[0], code)
        case 'IL': print_IL_inst(op_code[0], code)
        case 'S': print_S_inst(op_code[0], code)
               
def print_R_inst(op_code: op_function, code):
   st.text(f'{op_code[0].inst} x{int(code[20:25], 2)}, x{int(code[12:17], 2)}, x{int(code[7:12], 2)}')
    
def print_I_inst(op_code: op_function, code):
    op_ = op_code.code
    func3 = int(code[-15:-12],2)
    
    op_code = [item for item in op_dict_opcode if item.code == op_ and item.func3 == func3]
   
    
    imm_hex = signed_hex(code[:12], 8)
    imm_dec = code[0] == '0' and int(code[:12], 2) or -int(code[:12], 2)
    st.text(f'Dec: {op_code[0].inst} x{int(code[20:25], 2)}, x{int(code[12:17], 2)}, {imm_dec}')
    st.text(f'Hex: {op_code[0].inst} x{int(code[20:25], 2)}, x{int(code[12:17], 2)}, 0x{imm_hex}')

def print_IL_inst(op_code: op_function, code):
    op_ = op_code.code
    func3 = int(code[-15:-12],2)
    
    op_code:op_function = [item for item in op_dict_opcode if item.code == op_ and item.func3 == func3] 

   
    imm_hex = signed_hex(code[:12], 8)
    imm_dec = code[0] == '0' and int(code[:12], 2) or -int(code[:12], 2)
    
    st.text(f'Dec: {op_code[0].inst} x{int(code[20:25], 2)}, {imm_dec}(x{int(code[12:17], 2)})')
    st.text(f'Hex: {op_code[0].inst} x{int(code[20:25], 2)}, 0x{imm_hex}(x{int(code[12:17], 2)})')

def print_S_inst(op_code: op_function, code):
    op_ = op_code.code
    func3 = int(code[-14: -12],2)
    op_code:op_function = [item for item in op_dict_opcode if item.code == op_ and item.func3 == func3] 
    # imm = f'{code[:-25]}|{code[-25:-20]}|{code[-20:-15]}|{code[-15:-12]}|{code[-12:-7]}|{code[-7:]}'
    # print(imm)
    imm = f'{code[:-25]}{code[-12:-7]}'
    imm_hex = signed_hex(imm, 8)
    imm_dec = imm[0] == '0' and int(imm, 2) or -int(imm, 2)
    
    st.text(f'Dec: {op_code[0].inst} x{int(code[-25:-20], 2)}, {imm_dec}(x{int(code[-20:-15], 2)})')
    st.text(f'Hex: {op_code[0].inst} x{int(code[-25:-20], 2)}, 0x{imm_hex}(x{int(code[-20:-15], 2)})')
     
def signed_hex(code, lenth):
    imm = f'{int(code, 2):x}'
    imm = code[0] == '0' and f'{"0" * (lenth - len(imm))}{imm}' or f'{"f" * (lenth - len(imm))}{imm}'
    return imm       
    
reg = [
    'zero', 'ra', 'sp', 'gp',
    'tp', 't0', 't1', 't2',
    's0', 's1', 'a0', 'a1',
    'a2', 'a3', 'a4', 'a5',
    'a6', 'a7', 's2', 's3',
    's4', 's5', 's6', 's7',
    's8', 's9', 's10', 's11',
    't3', 't4', 't5', 't6'
]
    
    
    