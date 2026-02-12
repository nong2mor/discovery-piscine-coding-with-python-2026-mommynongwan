#!/usr/bin/env python3

# 1. นิยาม Array เดิม
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# 2. สร้าง Array ใหม่โดยการวนลูปบวก 2 ให้กับสมาชิกทุกตัว
new_array = [x + 2 for x in original_array]

# 3. แสดงผลทั้งสอง Array ตามรูปแบบที่โจทย์กำหนด
print(f"Original array: {original_array}")
print(f"New array: {new_array}")