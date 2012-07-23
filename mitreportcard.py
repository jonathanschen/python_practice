classes = []
grades = []
num_classes = int(raw_input('How many classes did you take?'))
i = 0

while i < num_classes:
	class_names = raw_input('What classes did you take?')
	classes.append(class_names)
	print "What did you get in %s" %class_names
	results = int(raw_input('>> '))
	grades.append(results)
	i += 1

print "			REPORT CARD:                "

i = 0
while i < num_classes:
	your_class = classes[i]
	your_grade = grades[i]
	print your_class, "=", your_grade
	i += 1

total_scores = sum(grades) 
GPA = total_scores/num_classes
print "Your GPA is", GPA