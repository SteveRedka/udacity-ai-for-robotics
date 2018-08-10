# Write a program that will iteratively update and
# predict based on the location measurements
# and inferred motions shown below.

def update(mean1, var1, mean2, var2):
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1./(1./var1 + 1./var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig].

# Insert code here

def localize(mu, sig, measurements, motion):
    result = [mu, sig]
    if len(measurements) != len(motion):
        raise ValueError, "measurements vector is different from motion vector"
    for i in range(len(measurements)):
        result = update(result[0], result[1], measurements[i], measurement_sig)
        result = predict(result[0], result[1], motion[i], motion_sig)
    return result

print localize(mu, sig, measurements, motion)
