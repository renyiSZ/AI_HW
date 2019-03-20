max_choose=[]
max_score=0
room_state="1111111"


max_room_num = 3



list=["00005","00001","00002","00009","00010","00007"]

day_dic={"00005":"0001101","00001":"1000000","00002":"1111100","00009":"0000001","00010":"0000011","00007":"1111000"}

score_dic={"00005":3,"00001":2,"00002":5,"00009":1,"00010":2,"00007":4}

def update_room_state(id,room_state_list):
	days = day_dic[id]
	for i in range(7):
		room_state_list[i] += int(days[i])

def room_state_back(id,room_state_list):
	days = day_dic[id]
	for i in range(7):
		room_state_list[i] -= int(days[i])

def check_choose_valid(id,room_state_list,max_room_num):
	days = day_dic[id]
	for i in range(7):
		if int(days[i]) == 1:
			if int(room_state_list[i]) >= max_room_num:
				return False
	return True

def dfs(step,app_list,app_score_dic, s1,s2,s3,s4,s5,s6,s7, sum,curr_choose,max_room_num,cannot_choose):
	global max_score,max_choose
	if step >= len(app_list):
		if sum > max_score:
			max_score = sum
			max_choose=[]
			for i in range(len(curr_choose)):
				max_choose.append(curr_choose[i])
			return
		if sum == max_score:
			if int(max_choose[0]) > int(curr_choose[0]):
				max_choose=[]
				for i in range(len(curr_choose)):
					max_choose.append(curr_choose[i])
				return




