#!/usr/bin/env python3

# 1. นิยาม Array เดิม
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# 2. สร้าง List ใหม่พร้อมเงื่อนไข (มากกว่า 5 และ บวก 2) เหมือนข้อที่แล้ว
filtered_list = [x + 2 for x in original_array if x > 5]

# 3. แปลง List เป็น Set เพื่อลบตัวซ้ำออกโดยอัตโนมัติ
# สังเกตว่าผลลัพธ์จะเปลี่ยนจากเครื่องหมาย [ ] เป็น { } ตามที่โจทย์ต้องการ
result_set = set(filtered_list)

# 4. แสดงผลทั้งสองชุด
print(original_array)
print(result_set)