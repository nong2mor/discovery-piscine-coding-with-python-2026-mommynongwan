#!/usr/bin/env python3

# 1. นิยาม Array เดิม
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# 2. สร้าง Array ใหม่ด้วย List Comprehension พร้อมเงื่อนไข filtering
# อ่านว่า: เอา x + 2 สำหรับทุก x ใน original_array เฉพาะตอนที่ x > 5 เท่านั้น
new_array = [x + 2 for x in original_array if x > 5]

# 3. แสดงผลทั้งสองชุด
print(original_array)
print(new_array)