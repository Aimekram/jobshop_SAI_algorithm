#Program based on SAI algorithm
#by: Janina Byszewska
#date: 23.11.2017

jobs = [[2, 3, 5],
		[4, 4, 2],
		[1, 2, 3],
		[5, 5, 5]]

j = 0

M0 = [] 
M1 = []
M2 = []

next_job = {}
job_sequence = []
next_job_full = []

print("\nJobs list (machines):")
for operations in jobs:
	M0.append(jobs[j][0])
	M1.append(jobs[j][1])
	M2.append(jobs[j][2])
	j = j + 1

machines = [M0, M1, M2]
print("",machines)

print("\nJobs list (jobs):\n",jobs)

print() 

def algorytm():
	m_min = []
	j_min = []
	j_list = []
	m_list = []
	m = 0

	for times in machines:
		machine_min_time = min(machines[m])
		machine_nr_min_time = machines[m].index(machine_min_time)
		print("For machine nr", m, "minimum time is", machine_min_time, "for job nr", machine_nr_min_time)
		j_min.append(machine_nr_min_time)
		m_list.append(m)
		m = m + 1

	print() 

	j = 0
	for times in jobs:
		job_min_time = min(jobs[j])
		job_nr_min_time = jobs[j].index(job_min_time)
		print("For job nr", j, "minimum time is", job_min_time, "at the machine nr", job_nr_min_time)
		m_min.append(job_nr_min_time)
		j_list.append(j)
		j = j + 1

	list_1 = [m_list, j_min] 
	list_2 = [m_min, j_list] 
	print("\nFind same list elements for", list_1, "and", list_2)

	k = 0
	l = 0
	for x, y, z, a in zip(m_list, m_min, j_min, j_list):
		for x, y, z, a in zip(m_list, m_min, j_min, j_list):
			if m_list[k] == m_min[l] and j_min[k] == j_list[l]:
				print("Next job was found") 
				next_job[m_list[k]] = j_min[k]
			else:
				l = l + 1
		else:
			l = 0
			k = k + 1		
		
		job_sequence.append(next_job[0])
		print("Next job to do is job nr", next_job.values(), "on the machine nr", next_job.keys())
		return(next_job)
	
next_job = algorytm()

next_job_full.append(jobs[job_sequence[0]])
print("\nJob sequence:", next_job_full)

del jobs[next_job[0]]
del M0[next_job[0]]
del M1[next_job[0]]
del M2[next_job[0]]
print("Remaining jobs:", jobs, "\n")

next_job = algorytm()

next_job_full.append(jobs[job_sequence[1]])
print("\nJob sequence", next_job_full)

del jobs[next_job[0]]
del M0[next_job[0]]
del M1[next_job[0]]
del M2[next_job[0]]
print("Remaining jobs:", jobs, "\n")

next_job = algorytm()

next_job_full.append(jobs[job_sequence[2]])
print("\nJob sequence:", next_job_full)

del jobs[next_job[0]]
del M0[next_job[0]]
del M1[next_job[0]]
del M2[next_job[0]]
print("Remaining jobs:", jobs, "\n")

job_sequence.append(0)

next_job_full.append(jobs[job_sequence[3]])
print("\nFinal job sequence:", next_job_full, "\n")

M0_t_in = []
M0_t_out = []

M0_t_in.append(0)
M0_t_out.append(M0_t_in[0] + next_job_full[0][0])

M1_t_in =[]
M1_t_out =[]

M1_t_in.append(M0_t_out[0])
M1_t_out.append(M0_t_out[0] + next_job_full[0][1])

M2_t_in =[]
M2_t_out =[]

M2_t_in.append(M1_t_out[0])
M2_t_out.append(M1_t_out[0] + next_job_full[0][2])

k = 1
while k < 4: 	
	M0_t_in.append(M0_t_out[k-1])
	M0_t_out.append(M0_t_in[k] + next_job_full[k][0])

	if M0_t_out[k-1] > M1_t_out[k-1]:   
		M1_t_in.append(M1_t_out[k-1])
	else:
		M1_t_in.append(M0_t_out[k])

	M1_t_out.append(M1_t_in[k] + next_job_full[k][1])

	if M1_t_out[k-1] > M2_t_out[k-1]:
		M2_t_in.append(M2_t_out[k-1])
	else:
		M2_t_in.append(M1_t_out[k])

	M2_t_out.append(M2_t_in[k] + next_job_full[k][2])
	k = k + 1

print("M0 time out:", M0_t_out)
print("M1 time out:", M1_t_out)
print("M2 time out:", M2_t_out)

print("\nFull time of doing the jobs is:", M2_t_out[3])