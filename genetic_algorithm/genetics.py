import numpy as np

class genetic():
    def __init__(self, init_assign, genes):
        self.assign = init_assign # initial assignments
        self.pop = len(init_assign) # number of initial population
        self.genelength = len(init_assign[0]) # number of variables in 1 assignment
        self.gene_type = genes # domain of each variable

    def fitness_func(self, assignment):
        A, B, C, D, E, F, G, H = assignment
        fitness_score = 16
        # Checking the negative of each condition and subtracting 1
        if A <= G: fitness_score -= 1
        if A > H: fitness_score -= 1
        if abs(F - B) != 1: fitness_score -= 1 
        if G >= H: fitness_score -= 1 
        if abs(G - C) != 1: fitness_score -= 1
        if (H - C) % 2 == 1 and (C - H) % 2 == 1: fitness_score -= 1        
        if H == D: fitness_score -= 1
        if D < G: fitness_score -= 1
        if D == C:fitness_score -= 1 
        if E == C:fitness_score -= 1 
        if E >= (D - 1): fitness_score -= 1
        if E == (H - 2): fitness_score -= 1
        if G == F:fitness_score -= 1 
        if H == F: fitness_score -= 1
        if C == F: fitness_score -= 1
        if D == (F - 1): fitness_score -= 1
        if abs(F - E) % 2 == 0: fitness_score -=1
        return fitness_score
    
    def cross_over(self, crossover_point, parent1, parent2):
        # offsprings are made of from 0 to crosspoint from 1 parent
        # and from crosspoint till the end from the other parent
        # offspring numbers are arbitrary
        offspring1 = parent1[:crossover_point]
        offspring2 = parent2[:crossover_point]
        offspring1.extend(parent2[crossover_point:])
        offspring2.extend(parent1[crossover_point:])
        return offspring1, offspring2
        
    def iter(self, iters):
        for iter in range(iters):

            # SELECTION----------------------------------------
            # calculate fitness score for each assignment
            fit_scores = [self.fitness_func(i) for i in self.assign]
            # calculate probability using  fitness / total fitness score
            prob = fit_scores/np.sum(fit_scores)
            print(f" \n fitness score and probability for iteration {iter+1} : \n\t", fit_scores, "\n\t", prob)
            # generates random indices with probability above of population size
            new_assign_indices = np.random.choice(np.arange(0,self.pop), self.pop, p = prob)
            # generates a new assignment based on the indices above
            sel_assigns = [self.assign[i] for i in new_assign_indices]
            
            # CROSSOVER--------------------------------------
            print(" pairings of parents chosen")
            for i in range(0, len(sel_assigns), 2):
                crossover_point = np.random.randint(self.genelength)
                print("\t crossove point = ", crossover_point, sel_assigns[i], sel_assigns[i+1])
                self.assign[i], self.assign[i+1] = self.cross_over(crossover_point, sel_assigns[i], sel_assigns[i+1])

            #MUTATION-----------------------------------------
            print("mutation effects:")
            for ind, assign in enumerate(self.assign):
                # should the mutation occur
                mutation_occur = np.random.choice(np.arange(2), p = [0.7, 0.3])
                if mutation_occur == 1:
                    # gene to be changed
                    gene_ind = np.random.randint(self.genelength)
                    # which gene to change to
                    new_gene_value = self.gene_type[np.random.randint(len(self.gene_type))]
                    # to ensure that mutation does have an actual effect
                    while  assign[gene_ind] == new_gene_value:
                        new_gene_value = self.gene_type[np.random.randint(len(self.gene_type))]
                    assign[gene_ind] = new_gene_value
                    # pring the mutation effect
                    print("\t change the variable at possition", gene_ind, "to ",new_gene_value, " for offspring"+str(ind))
                    # for aesthetics so can differentiate between each iteration
            print("="*15, f"iteration{iter + 1} over", "="*15)
        return self.assign



# initial assignment given in Q2   
initial_assignment = [[1,1,1,1,1,1,1,1],
                    [2,2,2,2,2,2,2,2],
                    [3,3,3,3,3,3,3,3],
                    [4,4,4,4,4,4,4,4],
                    [1,2,3,4,1,2,3,4],
                    [4,3,2,1,4,3,2,1],
                    [1,2,1,2,1,2,1,2],
                    [3,4,3,4,3,4,3,4]]

# initialising the algorithm
genetic_algorithm = genetic(initial_assignment,[1,2,3,4])

# run 5 iterations
genetic_algorithm.iter(5)


                
                
