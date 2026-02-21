# Python Concurrency Lab

โปรเจกต์นี้เป็นการทดลองใช้งาน concurrency ในภาษา Python
เพื่อเปรียบเทียบการทำงานของ Thread, asyncio และ Process Pool

## Programs

### 1. Thread
ใช้ threading สำหรับงาน I/O-bound
เช่น งานที่ต้องรอเวลา (sleep, network, file)

### 2. asyncio
ใช้ async/await และ event loop
เหมาะกับงาน I/O-bound ที่ต้องการประสิทธิภาพสูงโดยไม่ใช้หลาย thread

### 3. Process Pool
ใช้ ProcessPoolExecutor
เหมาะกับงาน CPU-bound ที่ต้องการใช้หลาย core

## Conclusion
- Thread และ asyncio เหมาะกับงานที่ต้องรอ I/O
- Process Pool เหมาะกับงานคำนวณหนัก