val = 0xCAFE

last_four_bits = val & 0xF
is_at_least_three_on = (
    last_four_bits == 0b0111 or
    last_four_bits == 0b1011 or
    last_four_bits == 0b1101 or
    last_four_bits == 0b1110 or
    last_four_bits == 0b1111
)
print(f"1. At least three of the last four bits are on: {is_at_least_three_on}")

high_byte = (val >> 8) & 0xFF  
low_byte = val & 0xFF         
reversed_val = (low_byte << 8) | high_byte
print(f"2. Value with reversed byte order: 0x{reversed_val:04X}")


num_bits = 16
rotate_amount = 4
rotated_out_bits = (val >> (num_bits - rotate_amount)) & ((1 << rotate_amount) - 1)


shifted_val = (val << rotate_amount) & ((1 << num_bits) - 1) 

rotated_val = shifted_val | rotated_out_bits
print(f"3. Value after rotating four bits: 0x{rotated_val:04X}")