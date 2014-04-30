import cPickle

# Load matrices
data_matrix = cPickle.load(open('commuter_data_matrix'))
prob_matrix = cPickle.load(open('probability_matrix'))

# Load FIPS codes for counties in matrices
fips = [line.strip() for line in open('us_fips')]

# Index matrices using FIPS codes
data_matrix[fips.index('01001')][fips.index('01021')] # Commuters from 01001 -> 01021
prob_matrix[fips.index('48113')][fips.index('48453')] # Probability of journey from 48113 -> 48453