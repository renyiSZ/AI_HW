import datetime
start = datetime.datetime.now()

lahsa_room = [0,0,0,0,0,0,0]
spla_room = [0,0,0,0,0,0,0]
lahsa_pre_chosen = []
spla_pre_chosen = []
lahsa_pre_score = 0
spla_pre_score = 0

applicants = {}

applicants_for_lahsa= {}
applicants_for_spla= {}

applicants_intersection_list=[]
applicants_for_lahsa_list0=[]
applicants_for_spla_list0 = []
applicants_for_lahsa_list = []
applicants_for_spla_list = []


max_score=0 
max_choose=[]

map_store_best_step_spla = {}
map_store_best_step_lahsa = {}

f = open("input200.txt", 'r')
b = int(f.readline().rstrip('\n'))
p = int(f.readline().rstrip('\n'))
L = int(f.readline().rstrip('\n'))

for i in range(L):
	L_info = f.readline().rstrip('\n')
	lahsa_pre_chosen.append(L_info[0:5])

S = int(f.readline().rstrip('\n'))

for i in range(S):
	S_info = f.readline().rstrip('\n')
	spla_pre_chosen.append(S_info[0:5])

A = int(f.readline().rstrip('\n'))

for i in range(A):
	A_info = f.readline().rstrip('\n')
	age = 0
	new_add_score = 0
	age = int(A_info[6:9])

	if A_info[0:5] in spla_pre_chosen:
		spla_pre_score += int(A_info[13])+ int(A_info[14])+ int(A_info[15])+ int(A_info[16])+int(A_info[17])+int(A_info[18])+int(A_info[19])
		spla_room[0] += int(A_info[13])
		spla_room[1] += int(A_info[14])
		spla_room[2] += int(A_info[15])
		spla_room[3] += int(A_info[16])
		spla_room[4] += int(A_info[17])
		spla_room[5] += int(A_info[18])
		spla_room[6] += int(A_info[19])
	if A_info[0:5] in lahsa_pre_chosen:
		lahsa_pre_score += int(A_info[13])+ int(A_info[14])+ int(A_info[15])+ int(A_info[16])+int(A_info[17])+int(A_info[18])+int(A_info[19])
		lahsa_room[0] += int(A_info[13])
		lahsa_room[1] += int(A_info[14])
		lahsa_room[2] += int(A_info[15])
		lahsa_room[3] += int(A_info[16])
		lahsa_room[4] += int(A_info[17])
		lahsa_room[5] += int(A_info[18])
		lahsa_room[6] += int(A_info[19])

	if A_info[10:13]== "NYY" and A_info[5:6]=="F" and age > 17 and A_info[9:10]=="N":
		if A_info[0:5] not in lahsa_pre_chosen and A_info[0:5] not in spla_pre_chosen:
			applicants_intersection_list.append(A_info[0:5])
	
	if A_info[10:13]== "NYY":
		new_add_score = int(A_info[13])+ int(A_info[14])+ int(A_info[15])+ int(A_info[16])+int(A_info[17])+int(A_info[18])+int(A_info[19])
		if A_info[0:5] not in spla_pre_chosen and A_info[0:5] not in lahsa_pre_chosen:
			applicants[A_info[0:5]] = A_info[13:20]
			applicants_for_spla[A_info[0:5]] = new_add_score
			applicants_for_spla_list0.append(A_info[0:5])
		

	if A_info[5:6]=="F" and age > 17 and A_info[9:10]=="N":
		new_add_score = int(A_info[13])+ int(A_info[14])+ int(A_info[15])+ int(A_info[16])+int(A_info[17])+int(A_info[18])+int(A_info[19])
		if A_info[0:5] not in lahsa_pre_chosen and A_info[0:5] not in spla_pre_chosen:
			applicants[A_info[0:5]] = A_info[13:20]
			applicants_for_lahsa[A_info[0:5]] = new_add_score
			applicants_for_lahsa_list0.append(A_info[0:5])

def take_score_spla(elem):
	return applicants_for_spla[elem]
def take_score_lahsa(elem):
	return applicants_for_lahsa[elem]

applicants_intersection_list.sort(key=take_score_spla,reverse=True)
for i in range(len(applicants_intersection_list)):
	applicants_for_lahsa_list.append(applicants_intersection_list[i])
	applicants_for_spla_list.append(applicants_intersection_list[i])
for i in range(len(applicants_for_spla_list0)):
	if applicants_for_spla_list0[i] not in applicants_for_spla_list:
		applicants_for_spla_list.append(applicants_for_spla_list0[i])
for i in range(len(applicants_for_lahsa_list0)):
	if applicants_for_lahsa_list0[i] not in applicants_for_lahsa_list:
		applicants_for_lahsa_list.append(applicants_for_lahsa_list0[i])


print("applicants_for_lahsa_list")
print(applicants_for_lahsa_list)
print("applicants_for_spla_list")
print(applicants_for_spla_list)
print("applicants_intersection_list")
print(applicants_intersection_list)
print(applicants)
print("spla_pre_score:"+str(spla_pre_score))
print(spla_room)
print("lahsa_pre_score:"+str(lahsa_pre_score))
print(lahsa_room)

def update_room_state(id,room_state_list):
	days = applicants[id]
	for i in range(7):
		room_state_list[i] += int(days[i])

def room_state_back(id,room_state_list):
	days = applicants[id]
	for i in range(7):
		room_state_list[i] -= int(days[i])

def check_choose_valid(id,room_state_list,max_room_num):
	days = applicants[id]
	for i in range(7):
		if int(days[i]) == 1:
			if int(room_state_list[i]) >= max_room_num:
				return False
	return True

def update_app_list(id,list_spla,list_lahsa,org):
	if id in applicants_intersection_list:
		list_spla.remove(id)
		list_lahsa.remove(id)
	else:
		if org=="spla":
			list_spla.remove(id)
		else:
			list_lahsa.remove(id)

def no_more_room(room_state,max_room_num):
	for i in range(7):
		if room_state[i] != max_room_num:
			return False
	return True

def cannot_choose_equal_app_list(cannot_choose,app_list):
	for i in range(len(app_list)):
		if app_list[i] not in cannot_choose:
			return False
	return True

def no_more_room_for_left_app(room_state,max_room_num,min_score):
	score = 0
	for i in range(7):
		score+=room_state[i]
	if score + min_score > 7*max_room_num:
		return True
	return False

def left_list_score(list,dic,no_list):
	score = 0
	for i in range(len(list)):
		if list[i] not in no_list:
			score+=int(dic[list[i]])
	return score

""" current best single step """
def dfs(step,app_list,app_score_dic,room_state,sum,curr_choose,max_room_num,cannot_choose,maxStep):
	global max_score,max_choose

	if step >= maxStep:
		if len(curr_choose)==0:
			return
		if sum > max_score:
			max_score = sum
			max_choose=[]
			for i in range(len(curr_choose)):
				max_choose.append(curr_choose[i])
			return
		
		if sum == max_score:
			if len(max_choose)!=0 and len(curr_choose)!=0:
				if int(max_choose[0]) > int(curr_choose[0]):
					max_choose=[]
					for i in range(len(curr_choose)):
						max_choose.append(curr_choose[i])
					return
		return

	id = app_list[step]
	
	dfs(step+1,app_list,app_score_dic,room_state,sum,curr_choose,max_room_num,cannot_choose,maxStep)

	if check_choose_valid(app_list[step],room_state,max_room_num)==True and id not in curr_choose:
		curr_choose.append(id)
		sum += app_score_dic[id]
		update_room_state(id,room_state)
		dfs(step+1,app_list,app_score_dic,room_state,sum,curr_choose,max_room_num,cannot_choose,maxStep)
		curr_choose.remove(id)
		sum -= app_score_dic[id]
		room_state_back(id,room_state)
	
def get_next_best_step(applicants_list,applicant_score_dic,room_state,max_room_num,org):
	global max_score,max_choose
	max_score=0 
	max_choose=[]
	list1 = []
	list1 = sorted(applicants_list)
	listToString = "".join(list1)
	listToString2=""
	for i in range(7):
		listToString2+=str(room_state[i])
	listToString+="|"
	listToString+=listToString2
	

	if org == "spla":
		if map_store_best_step_spla.has_key(listToString)==True:
			return map_store_best_step_spla[listToString]
	else:
		if map_store_best_step_lahsa.has_key(listToString)==True:
			return map_store_best_step_lahsa[listToString]
	maxStep = len(applicants_list)	
	app_list=[]
	for i in range(len(applicants_list)):
		app_list.append(applicants_list[i])
	new_room_state=[]
	for i in range(len(room_state)):
		new_room_state.append(room_state[i])
	dfs(0,app_list,applicant_score_dic,new_room_state,0,[],max_room_num,[],maxStep)
	
	if len(max_choose)==0:
		return ""
	else:
		max_choose_from_intersection=[]
		max_choose_not_from_intersection=[]
		for i in range(len(max_choose)):
			if max_choose[i] in applicants_intersection_list:
				max_choose_from_intersection.append(max_choose[i])
			else:
				max_choose_not_from_intersection.append(max_choose[i])
		
		if len(max_choose_from_intersection)==0:
			if org == "lahsa":
				"""
				max_choose_not_from_intersection.sort(key=take_score_lahsa,reverse=True)
				"""
				max_choose_not_from_intersection.sort()
				map_store_best_step_spla[listToString] = max_choose_not_from_intersection[0]
			else:
				"""
				max_choose_not_from_intersection.sort(key=take_score_spla,reverse=True)
				"""
				max_choose_not_from_intersection.sort()
				map_store_best_step_lahsa[listToString] = max_choose_not_from_intersection[0]
			return max_choose_not_from_intersection[0]
		else:
			if len(max_choose_from_intersection)>1:
				max_choose_from_intersection.sort(key=take_score_spla,reverse=True)
			if org == "spla":
				map_store_best_step_spla[listToString] = max_choose_from_intersection[0]
			else:
				map_store_best_step_lahsa[listToString] = max_choose_from_intersection[0]
			return max_choose_from_intersection[0]


""" main """
max_sum_score_spla = 0
max_sum_score_lahsa = 0
max_score_point = ""
app_list_spla=[]
app_list_lahsa=[]
spla_room_state=[]
lahsa_room_state=[]
sum_one_choose_spla = 0
sum_one_choose_lahsa = 0
spla_best_choose=[]
lahsa_best_choose=[]
spla_choose=[]
lahsa_choose=[]

for i in range(len(applicants_for_spla_list)):
	sum_one_choose_spla = 0
	sum_one_choose_lahsa = 0
	spla_choose=[]
	lahsa_choose=[]
	firstID = applicants_for_spla_list[i]
	app_list_spla=[]
	app_list_lahsa=[]
	spla_room_state=[]
	lahsa_room_state=[]
	"""initialize app list and room state list"""
	for i in range(len(applicants_for_spla_list)):
		app_list_spla.append(applicants_for_spla_list[i])
	for i in range(len(applicants_for_lahsa_list)):
		app_list_lahsa.append(applicants_for_lahsa_list[i])
	for i in range(7):
		spla_room_state.append(spla_room[i])
		lahsa_room_state.append(lahsa_room[i])
	
	"""---------------------------------------"""	
	for step in range(1,2*len(applicants)+1):
		nextid=""
		if step == 1:
			spla_choose.append(firstID)
			update_app_list(firstID,app_list_spla,app_list_lahsa,"spla")
			update_room_state(firstID, spla_room_state)	
			sum_one_choose_spla += applicants_for_spla[firstID]
		
		if step % 2 ==0:
			nextid = get_next_best_step(app_list_lahsa,applicants_for_lahsa,lahsa_room_state,b,"lahsa")
			if nextid == "":
				continue
			lahsa_choose.append(nextid)
			update_app_list(nextid,app_list_spla,app_list_lahsa,"lahsa")
			update_room_state(nextid, lahsa_room_state)	
			sum_one_choose_lahsa += applicants_for_lahsa[nextid]

		if step % 2 ==1 and step > 1:
			nextid = get_next_best_step(app_list_spla,applicants_for_spla,spla_room_state,p,"spla")
			if nextid == "":
				continue
			spla_choose.append(nextid)
			update_app_list(nextid,app_list_spla,app_list_lahsa,"spla")
			update_room_state(nextid, spla_room_state)	
			sum_one_choose_spla += applicants_for_spla[nextid]

	print("---------------------------------------")
	print("firstID:"+firstID)
	print("spla: "+str(spla_choose))
	print("lahsa: "+str(spla_choose))
	print(str(sum_one_choose_spla)+ " "+str(sum_one_choose_lahsa))
	print("---------------------------------------")

	if max_sum_score_spla < sum_one_choose_spla:
		max_sum_score_spla = sum_one_choose_spla
		max_sum_score_lahsa = sum_one_choose_lahsa
		max_score_point = firstID
		spla_best_choose=[]
		lahsa_best_choose=[]
		for i in range(len(spla_choose)):
			spla_best_choose.append(spla_choose[i])
		for i in range(len(lahsa_choose)):
			lahsa_best_choose.append(lahsa_choose[i])
		
	if max_sum_score_spla == sum_one_choose_spla:
		"""
		if max_sum_score_lahsa < sum_one_choose_lahsa:
			max_sum_score_lahsa = sum_one_choose_lahsa
			max_score_point = firstID
			spla_best_choose=[]
			lahsa_best_choose=[]
			for i in range(len(spla_choose)):
				spla_best_choose.append(spla_choose[i])
			for i in range(len(lahsa_choose)):
				lahsa_best_choose.append(lahsa_choose[i])

				
		if max_sum_score_lahsa == sum_one_choose_lahsa:
		"""
		if int(max_score_point) > int(firstID):
			max_score_point = firstID
			spla_best_choose=[]
			lahsa_best_choose=[]
			for i in range(len(spla_choose)):
				spla_best_choose.append(spla_choose[i])
			for i in range(len(lahsa_choose)):
				lahsa_best_choose.append(lahsa_choose[i])

print("#######################################")
"""
print("spla: "+str(spla_best_choose))
print("lahsa: "+str(lahsa_best_choose))
"""
print("max score spla: "+str(max_sum_score_spla+spla_pre_score))
print("max score lahsa: "+str(max_sum_score_lahsa+lahsa_pre_score))
print("choose: "+max_score_point)
f2 = open("output.txt", "w")
f2.write(str(max_score_point)+"\n")
end = datetime.datetime.now()
print (end-start)
print("#######################################")
