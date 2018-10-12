def all_processes():
    n = int(input("Please type the number of processes \n"))
    list_of_process = []
    for x in range(1, n + 1):
        curr_process = {'NUMBER': x, 'BURST': None, 'ARRIVAL': None}
        arrival_ = int(input("Please enter the arrival time of the process {} \n".format(x)))
        curr_process['ARRIVAL'] = arrival_
        burst_ = int(input("Please enter the burst time of the process {} \n".format(x)))
        curr_process['BURST'] = burst_
        priority_ = int(input("Please enter the priority of the process {} \n".format(x)))
        curr_process['PRIO'] = priority_
        list_of_process.append(curr_process)
    return list_of_process

def calculate_everything(list_of_process):
    temp_wait = 0
    list_of_process[0]['WAIT'] = temp_wait
    list_of_process[0]['TURNAROUND'] = list_of_process[0]['BURST'] + list_of_process[0]['WAIT']
    for x in range(1, len(list_of_process)):
        temp_wait = temp_wait + list_of_process[x-1]['BURST']
        list_of_process[x]['WAIT'] = temp_wait
        list_of_process[x]['TURNAROUND'] = list_of_process[x]['BURST'] + list_of_process[x]['WAIT']
    total_wait_time = 0
    total_turnaround_time = 0
    for x in range(0, len(list_of_process)):
        print("Waiting time for process {} is {} and turnaround is {}".format(list_of_process[x]['NUMBER'], list_of_process[x]['WAIT'], list_of_process[x]['TURNAROUND']))
        total_wait_time = list_of_process[x]['WAIT'] + total_wait_time
        total_turnaround_time = list_of_process[x]['TURNAROUND'] + total_turnaround_time
    print("Total Wait Time is {}".format(total_wait_time))
    print("Total Turnaround Time is {}".format(total_turnaround_time))
    print("Average Waiting Time is {}".format(total_wait_time / len(list_of_process)))
    print("Average Turnaround Time is {}".format(total_turnaround_time / len(list_of_process)))
    return list_of_process

def decide_algo(list_of_process):
    ch = int(input("1. FCFS\n2. SJF\n3. Non-Preemptive Priority\n4.Round Robin\n"))
    if ch is 1:
        list_of_process = sorted(list_of_process, key=lambda k: k['ARRIVAL']) 
        calculate_everything(list_of_process)
    if ch is 2:
        list_of_process = sorted(list_of_process, key=lambda k: k['BURST'])
        calculate_everything(list_of_process)
    if ch is 3:
        list_of_process = sorted(list_of_process, key=lambda k: k['PRIO'])
        calculate_everything(list_of_process)

x = all_processes()

decide_algo(x)
