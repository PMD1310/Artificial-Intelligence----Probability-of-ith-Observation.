import sys

class Hypothesis:
	def __init__(self, prior, cherry, lime):
		self.prior = prior
		self.cherry = cherry
		self.lime = lime

def main():
	if (len(sys.argv) > 2):
		print '[USAGE] python PP.py <Observation String>'
		sys.exit(0)
	r_file = open("result.txt", 'w')	# Creating a result file for storing the result
	# Creating the 5 hypothesis.
	h1 = Hypothesis(0.1, 1.0, 0.0)
	h2 = Hypothesis(0.2, 0.75, 0.25)
	h3 = Hypothesis(0.4, 0.5, 0.5)
	h4 = Hypothesis(0.2, 0.25, 0.75)
	h5 = Hypothesis(0.1, 0.0, 1.0)
	# Checking if the length of the arguements is correct
	if (len(sys.argv) != 2):
		try:
			r_file.write('Observation sequence Q: \r\n');
			r_file.write('Length of Q: 0\r\n\n');
			# Writnig the results for the final probability of each hypothesis
			r_file.write("P(h1 | Q) = %.5f \r\n" % (h1.prior))
			r_file.write("P(h2 | Q) = %.5f \r\n" % (h2.prior))
			r_file.write("P(h3 | Q) = %.5f \r\n" % (h3.prior))
			r_file.write("P(h4 | Q) = %.5f \r\n" % (h4.prior))
			r_file.write("P(h5 | Q) = %.5f \r\n\n" % (h5.prior))
			r_file.write("Probability that the next candy we pick will be Cherry, given Q: 0.50000\r\n")
			r_file.write("Probability that the next candy we pick will be Lime, given Q: 0.50000\r\n")
			r_file.close()
		except Exception:
			print 'Error creating a file'
			r_file.close()
		sys.exit(0)
	observation = sys.argv[1]  # getting the observations
	print(observation)
	observation_len = len(observation) 	# getting teh length of the string
	count_c = 0
	count_l = 0
	new_prior = 0.0
	qC0 = 0.0
	qL0 = 0.0
	r_file.write('Observation sequence Q: ' + observation + '\r\n');
	r_file.write('Length of Q: ' + str(observation_len) + '\r\n\n');
	for i in range(0, observation_len):
		#print("I am here")
		qC0 = (h1.prior*h1.cherry) + (h2.prior*h2.cherry) + (h3.prior*h3.cherry) + (h4.prior*h4.cherry) + (h5.prior*h5.cherry)
		qL0 = (h1.prior*h1.lime) + (h2.prior*h2.lime) + (h3.prior*h3.lime) + (h4.prior*h4.lime) + (h5.prior*h5.lime)
		if (observation[i] == 'c' or observation[i] == 'C'):
			new_prior = ( (h1.cherry * h1.prior) / qC0);
			h1.prior = new_prior
			new_prior = ( (h2.cherry * h2.prior) / qC0);
			h2.prior = new_prior
			new_prior = ( (h3.cherry * h3.prior) / qC0);
			h3.prior = new_prior
			new_prior = ( (h4.cherry * h4.prior) / qC0);
			h4.prior = new_prior
			new_prior = ( (h5.cherry * h5.prior) / qC0);
			h5.prior = new_prior
			count_c = count_c + 1;
		elif (observation[i] == 'l' or observation[i] == 'L'):
			new_prior = ( (h1.lime * h1.prior) / qL0);
			h1.prior = new_prior
			new_prior = ( (h2.lime * h2.prior) / qL0);
			h2.prior = new_prior
			new_prior = ( (h3.lime * h3.prior) / qL0);
			h3.prior = new_prior
			new_prior = ( (h4.lime * h4.prior) / qL0);
			h4.prior = new_prior
			new_prior = ( (h5.lime * h5.prior) / qL0);
			h5.prior = new_prior
			count_l = count_l + 1;
		else:
			print 'The inputs can only be a combination of C/c or L/l'
			r_file.close();
		        sys.exit(0)
		qC0 = (h1.prior*h1.cherry) + (h2.prior*h2.cherry) + (h3.prior*h3.cherry) + (h4.prior*h4.cherry) + (h5.prior*h5.cherry)
		qL0 = (h1.prior*h1.lime) + (h2.prior*h2.lime) + (h3.prior*h3.lime) + (h4.prior*h4.lime) + (h5.prior*h5.lime)
		try:
			#print("The Second try")
			# Writnig the results for the final probability of each hypothesis
			r_file.write("After Observation %d = %s\n" %(i+1,observation[i]))
			r_file.write("P(h1 | Q) = %.6f \r\n" %(h1.prior))
			r_file.write("P(h2 | Q) = %.6f \r\n" %(h2.prior))
			r_file.write("P(h3 | Q) = %.6f \r\n" %(h3.prior))
			r_file.write("P(h4 | Q) = %.6f \r\n" %(h4.prior))
			r_file.write("P(h5 | Q) = %.6f \r\n\n" %(h5.prior))
			r_file.write("Probability that the next candy we pick will be Cherry, given Q: %.6f \r\n" %(qC0))
			r_file.write("Probability that the next candy we pick will be Lime, given Q: %.6f \r\n" %(qL0))

		except Exception:
			print ("Error creating a file")
			r_file.close()
	r_file.close()

if (__name__ == '__main__'):
	main()