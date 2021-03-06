# Group 6: Neighbhor Joining Algorithm (and corresponding problems)

# Authors: Josh Nixon
#          Alex Pearson
#          Bidit Acharya
#          Tracy Lou

import matplotlib.pyplot as plt
import numpy as np

"""
Constructs a transition Matrix with a specified alpha level a
Args:
     a: alpha level for the Jukes Cantor Matrix
Returns:
     Transition Matrix corresponding to the Jukes-Cantor Algorithm
"""

def transition_matrix(a):
    b = a/3
    M = np.array([[1-a, b, b, b],
                 [b, 1-a, b, b],
                 [b, b, 1-a, b],
                 [b, b, b, 1-a]])
    return M

def rand_vector(n):
    a = np.random.rand(n)
    return a/sum(a)

"""
Finds the equilibrium point of a transition Matrix

Args:
    M: the transition Matrix for the Jukes Cantor Algorithm 

Returns:
    The equilibrium point of a transition Matrix
"""

def find_eq(M):
    D, V = np.linalg.eig(M)
    for x in xrange(D.size):
        if abs(D[x] - 1) < .0001:
            return V[:, x]/sum(V[:, x])

"""
Counts the number of time steps until the Jukes-Counter Algorithm
raches a steady state.

Args:
          M: the transition Matrix for the Jukes Cantor Algorithm 
        p_t: the initial probability vector specified by 4.4.3
    epsilon: the acceptable error bound on the equilibrium value

Returns:
    Number of iterations required for the model to converge 
    to within epsilon of the equilibrium value
"""
def counter(epsilon, p_t, M):
    p_eq = find_eq(M)
    def is_within_epsilon(p_t):
        t = True
        for i in xrange(p_t.size):
            t = t and abs(p_eq[i] - p_t[i]) < epsilon
        return t
    count = 0
    while not is_within_epsilon(p_t):
        p_t = M.dot(p_t)
        count += 1
    return count

"""
Performs simulations for all of the specific examples in problem 443

Args:
          p: probability vector

Returns:
    Number of iterations required for the model to converge 
    to within epsilon of the equilibrium value
"""
def problem_443(p):
    M     = transition_matrix(.3)
    large = counter(0.05, p, M)
    small = counter(0.01, p, M)
    print('------------------------------------------------------------')
    print('number of iterations to get within epsilon = .05 is:')
    print(large)
    print('-------------------------------------------------------------')
    print('number of iterations to get with epsilon = .01 is:')
    print(small)
    print('-------------------------------------------------------------')


"""
Performs simulations for a set of random probability vectors

Returns:
    Average Number of iterations required for the model to converge 
    to within epsilon of the equilibrium value
"""
def simulate_convergence(a, iter):
    small = np.zeros(iter)
    large = np.zeros(iter)
    M     = transition_matrix(a)
    
    for x in xrange(iter):
        p      = rand_vector(4)
        large[x] = counter(0.05, p, M)
        small[x] = counter(0.01, p, M)
    return [small, large]
def problem_443_rand(a, name):
    iter = 10000
    small, large = simulate_convergence(a, iter)
    print('------------------------------------------------------------')
    print('average number of iterations to get within epsilon = .05 is:')
    print(sum(large)/iter)
    print('-------------------------------------------------------------')
    print('average number of iterations to get within epsilon = .01 is:')
    print(sum(small)/iter)
    print('-------------------------------------------------------------')
    plt.figure(10*a)
    n, bins, patches = plt.hist(large, 7)
    plt.plot(bins)
    plt.xlabel('number of iterations')
    plt.ylabel('frequency')
    plt.title('large' + name)
    plt.figure(10*a +1)
    n, bins, patches = plt.hist(small, 9)
    plt.plot(bins)
    plt.xlabel('number of iterations')
    plt.ylabel('frequency')
    plt.title('small' + name)
# Solves Problem 443 by calling necessary functions
p_a = np.array([.2, .3, .4, .1])
p_c = np.array([.25, .25, .25, .25])
p_d = np.array([0, 1, 0, 0])
print('Problem 443a using probability vector')
print(p_a)
print('we get')
problem_443(p_a)
print('443b using random probability vectors to obatain')
print('average number of iterations to get within epsilon')
problem_443_rand(.3, 'alpha .3')
print('Problem 443c using probability vector')
print(p_c)
print('we get')
problem_443(p_c)
print('Problem 443c using probability vector')
print(p_d)
print('we get')
problem_443(p_d)

print ('trying alphas')

problem_443_rand(.6, 'alpha .6')
alphasLarge = []
alphasSmall = []
iter = 50
for a in xrange(1, iter):
    small, large = simulate_convergence(float(a)/iter, iter*40)
    alphasSmall.append(sum(small)/(iter*40))
    alphasLarge.append(sum(large)/(iter*40))
plt.figure(0)
n, bins, patches = plt.hist(alphasSmall, 50)
plt.plot(bins)
plt.xlabel('alpha')
plt.ylabel('avg convergence')
plt.title('small alpha variation')
plt.figure(1)
n, bins, patches = plt.hist(alphasLarge, 50)
plt.plot(bins)
plt.xlabel('alpha')
plt.ylabel('avg convergence')
plt.title('large alpha variation')
plt.show()
