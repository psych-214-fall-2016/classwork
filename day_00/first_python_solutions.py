# Define a “number_of_subjects” and assign value 20 to it.

# Your code here.
number_of_subjects = 20

# Display the statement: "We have x subjects where “x” is the number of
# subjects.

# Your code here
print("We have {} subjects".format(number_of_subjects))

# Define two variable: “control_subjects” and “drug_subjects” and assign values
# 18 and 22 respectively.

# Now define a new variable “all_subjects” which is a sum of the two.

# Your code here
control_subjects = 18
drug_subjects = 22
all_subjects = control_subjects + drug_subjects

# Print a list of subject identifiers for each subject from the previous
# exercise. Subject identifiers go from “sub001”, “sub002”, to “sub030”.

for i in range(all_subjects):
    print("sub{:03d}".format(i + 1))

# Create a variable “list_of_subjects” containing a list of identifiers you
# just printed.

list_of_subjects = []
for i in range(all_subjects):
    list_of_subjects.append("sub{:03d}".format(i))
list_of_subjects

# Unfortunately the data from some subjects were corrupted. Create another
# variable "list_of_excluded_subjects" containing identifiers “sub005” and
# “sub008”.

list_of_excluded_subjects = ['sub005', 'sub008']

# Now create a list of all subjects apart from those in the
# “list_of_excluded_subjects”. Print the identifiers in it. Tip: use the for
# loop.

good_subjects = []
for i in range(all_subjects):
    subject = list_of_subjects[i]
    if subject in list_of_excluded_subjects:
        continue
    good_subjects.append(subject)
good_subjects

# Do we expect the same identifier to be on the list of subjects twice? If not
# what other data structure could we use to contain the subjects? Modify your
# code accordingly, to create your collection of subjects and remove the
# excluded subjects.

excluded_subjects = set(list_of_excluded_subjects)
good_subjects = set(list_of_subjects) - excluded_subjects

# For the next step, make sure your subjects are in a sorted list.  If you used
# another data type above, convert it to a sorted list.  Now write out your
# ordered subjects to text file called “usable_subjects.txt”. Write one subject
# identifier per line.

good_list = sorted(good_subjects)
fobj = open('usable_subjects.txt', 'wt')
for i in range(len(good_list)):
    fobj.write(good_list[i] + '\n')
fobj.close()

# For the rest of the class we would like you to work on the following task:
#
# You are given a log file called "24719.f3_beh_CHYM.csv".  It contains the
# results from a behavioral experiment.
#
# The first line in the file contains the header, giving the names of the
# variables.  Each line after the first corresponds to one trial of the
# experiment. We are interested in the average response time on trials where
# response was the “space” key and displayed shape (“trial_shape”) was a red
# square.  Here are the first few lines of this file:
#
# response,response_time,trial_ISI,trial_shape
# None,0,2000,red_star
# None,0,1000,red_circle
# None,0,2500,green_triangle
# None,0,1500,yellow_square
#
# Hints:
#  * when you read lines from a text file, they end with a carriage return;
#  * remember split;
#  * strings are not numbers.

rt = 0.
n = 0
fobj = open("24719.f3_beh_CHYM.csv", 'rt')
lines = fobj.readlines()
for i in range(1, len(lines)):
    line = lines[i].strip()
    parts = line.split(',')
    if parts[0] == 'space' and parts[3] == 'red_square':
        rt += int(parts[1])
        n += 1
print(rt / n)
assert round(rt / n) == 382

# Bonus exercise: Have a look at the pandas package especially the read_csv
# method. Could you solve the previous exercise using this functionality?
