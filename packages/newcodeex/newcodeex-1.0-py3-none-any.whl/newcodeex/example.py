#--- IMPORT DEPENDENCIES ------------------------------------------------------+
 
import random
 
#--- TEST FUNCTIONS ---------------------------------------------------+
 
def func1(x):
    # Sphere function, bounds, f(0,...,0)=0
    return sum([x[i]**2 for i in range(len(x))])
 
def func2(x):
    # Beale's function, use bounds=[(-4.5, 4.5),(-4.5, 4.5)], f(3,0.5)=0.
    term1 = (1.500 - x[0] + x[0]*x[1])**2
    term2 = (2.250 - x[0] + x[0]*x[1]**2)**2
    term3 = (2.625 - x[0] + x[0]*x[1]**3)**2
    return term1 + term2 + term3
 
def fobj1(x):
    # Objective function for kharif season, bounds = [(0, 1075), (0, 3040), (0, 217.6), (35, 112), (386.4, 579.6), (5, 15)] 
     
     return (16.85 * x[0] + 14.32 * x[1] +  4.79 * x[2] + 25.74 * x[3] + 13.97 * x[4] + 11.53 * x[5])
    
      
def fobj2(x):
    #Objective function for rabi season, bounds = [(1759.85,4100),(34.7,111.04),(2.5,8),(15.5,49.6),(75,240),(10,32),(6.5,20.8)] 
    
    return (4.13 * x[0] + 19.63 * x[1] + 2.17 * x[2] + 1.93 * x[3] + 3.67 * x[4] + 1.44 * x[5] + 1.54 * x[6])

def wsm(x):
    return (0.5* f1(x) + 0.5 * f2(x))
def f1(x) :
                return (-(16.85 * x[0] + 14.32 * x[1] +  4.79 * x[2] + 25.74 * x[3] + 13.97 * x[4] + 11.53 * x[5]))
def f2(x):        
               return (10261*x[0]+11292*x[1]+7349*x[2]+11761*x[3]+10371*x[4]+3674*x[5])

  

#--- FUNCTIONS ----------------------------------------------------------------+
 
def ensure_bounds(vec, bounds):
 
    vec_new = []
    # examine each variable in vector 
    for i in range(len(vec)):
 
        # variable exceedes the minimum bound
        if vec[i] < bounds[i][0]:
            vec_new.append(bounds[i][0])
 
        # variable exceedes the maximum bound
        if vec[i] > bounds[i][1]:
            vec_new.append(bounds[i][1])
 
        # the variable is within bounds
        if bounds[i][0] <= vec[i] <= bounds[i][1]:
            vec_new.append(vec[i])
        
    return vec_new


def DominanceFilter(F,C):
    Xpop = len(F)
    Nobj = len(F[0])
    Nvar = len(C[0])
    PFront = np.zeros((Xpop,Nobj))
    PSet = np.zeros((Xpop,Nvar))
    k = 0
    for xpop in range(Xpop):
        Dominated = 0

        for comp in range(Xpop):
            if ((F[xpop,:]==F[comp,:]).all()):
                if(xpop>comp):
                    Dominated = 1
                    break
            elif ((F[xpop,:]>=F[comp,:]).all()):
                Dominated = 1
                break
        
        if(Dominated==0) :
            PFront[k,:] = F[xpop,:]
            PSet[k,:] = C[xpop,:]
            k+=1
    
    PFront = PFront[:k,:]
    PSet = PSet[:k,:]

    return (PFront,PSet)

 
 
#--- MAIN ---------------------------------------------------------------------+
 
def main(obj_func, bounds, popsize, mut, CR, maxiter):
 
    #--- INITIALIZE POPULATION (step #1) ----------------+
    
    population = []
    for i in range(0,popsize):
        indv = []
        for j in range(len(bounds)):
            indv.append(random.uniform(bounds[j][0],bounds[j][1]))
        population.append(indv)
            
    #--- SOLVE --------------------------------------------+
 
    # cycle through each generation (step #2)
    for i in range(1,maxiter+1):
        print( 'GENERATION:',i)
 
        gen_scores = [] # array to keep the fitnes score
 
        # cycle through each individual in the population
        for j in range(0, popsize):
 
            #--- MUTATION (step #3.A) ---------------------+
            
            # select three random vectors index positions within range (0, popsize), excluding current vector (j)
            canidates = list(range(0,popsize))
            canidates.remove(j)
            random_index = random.sample(canidates, 3)
 
            x_1 = population[random_index[0]]
            x_2 = population[random_index[1]]
            x_3 = population[random_index[2]]
            x_t = population[j]     # target vector
            
            #--- APPLYING MUTATION STRATEGY DE/RAND/1/BIN)----------------+
            
            # subtract x3 from x2, and create a new vector (x_diff)(vector differential)
            x_diff = [x_2_i - x_3_i for x_2_i, x_3_i in zip(x_2, x_3)]
 
            # multiply vector differential x_diff by the mutation factor (F) and add to x_1
            vec_donor = [x_1_i + mut * x_diff_i for x_1_i, x_diff_i in zip(x_1, x_diff)]
            vec_donor = ensure_bounds(vec_donor, bounds)
 
            #--- CROSSOVER (step #3.B) ----------------+
 
            vec_trial = []
            for k in range(len(x_t)):
                crossover = random.random()
                if crossover <= CR:
                    vec_trial.append(vec_donor[k])
 
                else:
                    vec_trial.append(x_t[k])
                    
            #--- print scores or obj function value -------------+
 
            score_trial  = obj_func(vec_trial)
            score_target = obj_func(x_t)
           
            print ('f1 >',f1(vec_trial))
            print ('f2 >',f2(vec_trial))
            print ('f1 target >', f1(x_t))
            print ('f2 target >', f2(x_t))

         #--- SELECTION (step #3.C) -------------+

            if score_trial > score_target:
                population[j] = vec_trial
                gen_scores.append(score_trial)
                print ('   <',score_trial, vec_trial)
 
            else:
                print ('   <',score_target, x_t)
                gen_scores.append(score_target)

            PFront= score_target
            PSet= x_t
 
        #--- STORE THE FITNESS VALUE  --------------------------------+
 
        gen_avg = sum(gen_scores) / popsize                         # avg. fitness of the current generation 
        gen_best = max(gen_scores)                                  # fitness of best individual for current generation
        gen_sol = population[gen_scores.index(max(gen_scores))]     # solution of best individual
 
        print ('      ● GENERATION AVERAGE:',gen_avg)
        print ('      ● GENERATION BEST:',gen_best)
        print ('      ● BEST SOLUTION:',gen_sol,'\n')
        
 
    return gen_sol
 
#--- CONSTANTS ----------------------------------------------------------------+
 
obj_func = wsm                    # Objective function
 
# Bounds [(x1_min, x1_max), (x2_min, x2_max),...] 
 
bounds = [(0, 1075), (0, 3040), (0, 217.6), (35, 112), (386.4, 579.6), (5, 15)]
#bounds = [(1759.85,4100),(34.7,111.04),(2.5,8),(15.5,49.6),(75,240),(10,32),(6.5,20.8)] 
popsize = 20                        # Population size (NP), must be >= 4 (Decided by the programmer through hit and trial)
mut = 0.8                           # Mutation factor(F) [0,2]
CR = 0.5                            # Crossover rate (CR) [0,1]
maxiter = 60                      # Max number of generations (maxiter)
 
#--- RUN ----------------------------------------------------------------------+
 
#main(obj_func, bounds, popsize, mut, CR, maxiter)
 
