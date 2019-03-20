import datetime
import numpy

start = datetime.datetime.now()
f = open("input0.txt", 'r')
s = int(f.readline().rstrip('\n'))

# up, right, down, left
direction = [(0,-1),(1, 0),(0, 1),(-1, 0)]
char_direction = ["^",">","v","<"]
grid_point =  numpy.zeros(shape=(s,s))
reward={}
states = set()
for i in range(s):
	for j in range(s):
		grid_point[i][j] = -1
		states.add((i,j))
		reward[i,j] = -1
"""state, reward x,y direction same as picture"""

n = int(f.readline().rstrip('\n').rstrip('\r'))
"""number of cars"""
o = int(f.readline().rstrip('\n').rstrip('\r'))
"""number of obstacles"""

for i in range(o):
	o_loc = f.readline().rstrip('\n').rstrip('\r')
	o_loc_split = o_loc.split(",")
	x = o_loc_split[0]
	y = o_loc_split[1]
	grid_point[int(y)][int(x)] -= 100
	reward[int(x), int(y)] = grid_point[int(y)][int(x)]

start_loc_arr = []
end_loc_arr = []
for i in range(n):
	p = f.readline().rstrip('\n').rstrip('\r').split(",")
	start_loc_arr.append((int(p[0]),int(p[1])))

for i in range(n):
	p = f.readline().rstrip('\n').rstrip('\r').split(",")
	end_loc_arr.append((int(p[0]),int(p[1])))

#print("size of grid:"+ str(s))
#print("number of cars:"+str(n))
#print("number of obstacles:"+str(o))
#print(grid_point)
#print(reward)
#print(start_loc_arr)
#print(end_loc_arr)

def turn_right(direction_index):
	if direction_index == 3:
		return 0
	else: 
		return direction_index + 1

def turn_left(direction_index):
	if direction_index == 0:
		return 3
	else:
		return direction_index - 1

def vector_add(p1,p2):
	x = int(p1[0])+int(p2[0])
	y = int(p1[1])+int(p2[1])
	return (x,y)

def check_out_of_boundary(new_point):
	if(new_point[0]<0 or new_point[1]<0 or new_point[0]>=s or new_point[1]>=s):
		return True
	else:
		return False


def value_iteration(start,end):
	global reward
	U1 = {}
	for st in states:
		U1[st] = 0
	epsilon = 0.1
	gamma = 0.9
	reward[end] = 99
	U1[end] = 99
	while True:
		delta = 0
		U = U1.copy()
		for st in states:
			if st == end:
				continue
			#up right down left
			new_point = [(0,0),(0,0),(0,0),(0,0)]
			values = numpy.array([0,0,0,0],dtype=numpy.float64)
			for i in range(4):
				new_point[i] = vector_add(st,direction[i])
				if check_out_of_boundary(new_point[i]) == True:
					values[i] = U[st]
				else:
					point = new_point[i]
					values[i] = U[point]
			direction_values = numpy.array([0,0,0,0],dtype=numpy.float64)
			# up right down left
			direction_values[0] = 0.7*values[0] + 0.1*(values[1]+values[2]+values[3])
			direction_values[1] = 0.7*values[1] + 0.1*(values[0]+values[2]+values[3])
			direction_values[2] = 0.7*values[2] + 0.1*(values[0]+values[1]+values[3])
			direction_values[3] = 0.7*values[3] + 0.1*(values[0]+values[2]+values[1])
			U1[st] = reward[st] + gamma * numpy.max(direction_values)
			delta = max(delta, abs(U1[st] - U[st]))	
		if delta < epsilon * (1 - gamma) / gamma:
			return U


def best_policy(U,end):
	pi = {}
	for st in states:
		if st == end:
			pi[st] = "G"
			continue
		new_U = expected_utility(st,U)
		max_index = numpy.argmax(new_U)
		if max_index == 0:
			pi[st] = "^"
		if max_index == 1:
			pi[st] = "v"
		if max_index == 2:
			pi[st] = ">"
		if max_index == 3:
			pi[st] = "<"
	return pi

def expected_utility(st, U):
	sums = numpy.array([0,0,0,0],dtype=numpy.float64)
	
	new_point = [(0,0),(0,0),(0,0),(0,0)]
	values = [0,0,0,0]
	for i in range(4):
		"""up right down left"""
		new_point[i] = vector_add(st,direction[i])
		if check_out_of_boundary(new_point[i]) == True:
			values[i] = U[st]
		else:
			point = new_point[i]
			values[i] = U[point]
	#if tie, order: North, South, East, West
	""" North ^ """
	sums[0] = 0.7*values[0] + 0.1*(values[1]+values[2]+values[3])
	""" South v """
	sums[1] = 0.7*values[2] + 0.1*(values[0]+values[1]+values[3])
	""" East > """
	sums[2] = 0.7*values[1] + 0.1*(values[0]+values[2]+values[3])
	""" West < """
	sums[3] = 0.7*values[3] + 0.1*(values[0]+values[1]+values[2])

	return sums


def print_direction(policy):
	arr = [[0 for x in range(s)] for y in range(s)]
	for st in states:
		arr[st[1]][st[0]] = policy[st]
	for i in range(s):
		for j in range(s):
			print str(arr[i][j]),
		print("")

"""
final_U = value_iteration(start_loc_arr[0],end_loc_arr[0])
policy = best_policy(final_U,end_loc_arr[0])
print_direction(policy)

"""
output = []

for i in range(n): 
	ten_times_money_sum = 0
	final_U = value_iteration(start_loc_arr[i],end_loc_arr[i])
	policy = best_policy(final_U,end_loc_arr[i])
	print("--------------------")
	print_direction(policy)
	for j in range(10):
		money = 0
		pos = start_loc_arr[i]
		if pos == end_loc_arr[i]:
			money = 100
			continue
		numpy.random.seed(j)
		swerve = numpy.random.random_sample(1000000)
		k=0
		#print("seed:"+str(j)+" ^^^^^^^^^^^^^^^^^^^")
		#print("start point:"+str(pos))
		while pos != end_loc_arr[i]:	
			move = policy[pos]
			move_index = char_direction.index(move)
			new_move_index = -1
			if swerve[k] > 0.7:
				if swerve[k] > 0.8:
					if swerve[k] > 0.9:
						new_move_index = turn_right(turn_right(move_index))
						new_pos = vector_add(pos, direction[new_move_index])
						if check_out_of_boundary(new_pos) == True:
							new_pos = pos
						money += reward[new_pos]
						#print("turn left and turn left")
						#print(direction[new_move_index])
						#print(char_direction[new_move_index])
					else:
						new_move_index = turn_right(move_index)
						new_pos = vector_add(pos, direction[new_move_index])
						if check_out_of_boundary(new_pos) == True:
							new_pos = pos
						money += reward[new_pos]
						#print("turn left")
						#print(direction[new_move_index])
						#print(char_direction[new_move_index])
				else:
					new_move_index = turn_left(move_index)
					new_pos = vector_add(pos, direction[new_move_index])
					if check_out_of_boundary(new_pos) == True:
						new_pos = pos
					money += reward[new_pos]
					#print("turn right")
					#print(direction[new_move_index])
					#print(char_direction[new_move_index])
			else:
				new_pos = vector_add(pos, direction[move_index])
				if check_out_of_boundary(new_pos) == True:
					new_pos = pos
				money += reward[new_pos]
				#print(direction[move_index])
			
			#print("------")
			#print(money)
			pos = new_pos	
			k+=1
		ten_times_money_sum += money

	reward[end_loc_arr[i]] = -1
	single_output = numpy.floor(ten_times_money_sum/10.0)
	#print("output: "+str(single_output))
	#print("#####################################################\n")
	output.append(int(single_output))

print(output)


f2 = open("output.txt", "w")
for i in range(n):
	f2.write(str(output[i])+"\n")

end = datetime.datetime.now()
print (end-start)
