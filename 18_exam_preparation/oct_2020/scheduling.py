jobs_list = [int(x) for x in input().split(", ")]
index = int(input())
clock_cycles = 0
for current_job in jobs_list[index + 1:]:
    if current_job < jobs_list[index]:
        clock_cycles += current_job

for job in jobs_list[:index + 1]:
    if job <= jobs_list[index]:
        clock_cycles += job
print(clock_cycles)

