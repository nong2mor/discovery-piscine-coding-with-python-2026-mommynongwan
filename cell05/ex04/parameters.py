#!/usr/bin/env python3
import sys

# sys.argv เป็น List ที่เก็บชื่อไฟล์และ parameter ทั้งหมด
# เราลบ 1 ออก เพราะตำแหน่งแรก (sys.argv[0]) คือชื่อไฟล์เสมอ ซึ่งเราไม่นับเป็น parameter
num_params = len(sys.argv) - 1

print(f"Number of parameters: {num_params}.")