import math

ball_1 = (0, 0, 1)
ball_2 = (3, 3, 1)
ball_a = (5, 5, 2)
ball_b = (2, 8, 3)

def collision(ball_x, ball_z):
	base = math.fabs(ball_x[0] - ball_z[0]) 	
	height = math.fabs(ball_x[1] - ball_z[1])
	distance = math.sqrt(base**2 + height**2)
	sum_of_radii = ball_x[2]+ball_z[2]
	if distance > sum_of_radii:
		print "%s and %s are not colliding" % (ball_x, ball_z)
	else: 
		print "%s and %s are colliding" % (ball_x, ball_z)

collision(ball_1, ball_2)
collision(ball_a, ball_b)