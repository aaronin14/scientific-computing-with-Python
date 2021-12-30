import copy
import random
# Consider using the modules imported above.

class Hat():
	contents = list()
	def __init__(self,**kwargs):
		self.contents = []
		for ball,amount in kwargs.items():
			self.contents.extend(ball for i in range(amount))

	def draw(self,amount):
		drawn = list()
		if amount <= len(self.contents):
			for i in range(amount):
				drawn_ball_index = random.randint(0,len(self.contents)-1)
				drawn.append(self.contents.pop(drawn_ball_index))
		else:
			return self.contents
		return drawn

def expected_balls_list(expected_balls):
	balls_list = list()
	for (ball,amount) in expected_balls.items():
		for i in range(amount):
			balls_list.append(ball)
	return balls_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	count = 0
	for time in range(num_experiments):	
		tmp = copy.deepcopy(hat)	
		actual_drawn = tmp.draw(num_balls_drawn)
		success = True
		for key in expected_balls.keys():
			if actual_drawn.count(key) < expected_balls[key]:
				success = False
				break
		if success:
			count += 1

	return count/num_experiments