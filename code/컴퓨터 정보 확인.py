# CPU,메모리,디스크,네트워크 등의 정보를 확인하는 프로그램을 만들어본다
# pip install psutil
# --------------------------------------------------------------------------------------------------------------

# 컴퓨터 정보 확인 코드 만들기

# import psutil

# cpu = psutil.cpu_freq()
# print(cpu)

# cpu_core = psutil.cpu_count(logical=False)
# print(cpu_core)

# memory = psutil.virtual_memory()
# print(memory)

# disk = psutil.disk_partitions()
# print(disk)

# net = psutil.net_io_counters()
# print(net)
# --------------------------------------------------------------------------------------------------------------

# 필요한 정보만 출력하는 코드 만들기

# import psutil

# cpu = psutil.cpu_freq()
# cpu_current_ghz = round(cpu.current/ 1000, 2)
# print(f'cpu속도: {cpu_current_ghz}GHz')

# cpu_core = psutil.cpu_count(logical=False)
# print(f'코어: {cpu_core} 개')

# memory = psutil.virtual_memory()
# memory_total = round(memory.total/ 1024**3)

# disk = psutil.disk_partitions()
# for p in disk: # 디스크는 하나가 아닌 여러 개가 있을 수 있으므로 찾은 수 만큼 출력한다
#     print(p.mountpoint, p.fstype, end=' ')
#     du = psutil.disk_usage(p.mountpoint)
#     disk_total = round(du.total / 1024**3)
#     print(f'디스크 크기: {disk_total}GB')

# net = psutil.net_io_counters() # 네트워크를 통해 보내고 받은 데이터 크기를 MB단위로 출력한다. 보내고 받은 데이터는 누적데이터 값입니다.
# sent = round(net.bytes_sent/1024**2, 1)
# recv = round(net.bytes_recv/1024**2, 1)
# print(f'보내기: {sent}MB 받기: {recv}MB')
# --------------------------------------------------------------------------------------------------------------

# 1초당 반복해서 정보를 출력하는 코드 만들기

import psutil

curr_sent = 0
curr_recv = 0

prev_sent = 0
prev_recv = 0

while True:
    cpu_p = psutil.cpu_percent(interval=1) # cpu 사용량의 1초동안의 평균값을 구함
    print(f'cpu사용량 : {cpu_p}')

    memory = psutil.virtual_memory()
    memory_avail = round(memory.available/1024**3,1)
    print(f'사용 가능한 메모리: {memory_avail}')

    net = psutil.net_io_counters()
    curr_sent = net.bytes_sent/1024**2
    curr_recv = net.bytes_recv/1024**2

    sent = round(curr_sent-prev_sent,1)
    recv = round(curr_recv-prev_recv,1)
    print(f'보내기: {sent}MB 받기: {recv}MB')

    prev_sent = curr_sent # 이전의 값을 현재 값에 바인딩한다. 이전의 값을 가지고 있어야 현재값과 비교하여 1초동안 얼마를 보냈는지 계산할 수 있기 때문 
    prev_recv = curr_recv