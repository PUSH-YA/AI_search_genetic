# AI_search_genetic
repository to keep track of my journey of learning traditional AI. This repository currently keeps track of two things: 1) Search algorithms, 2) Stochastic Local Search Variant called the genetic algorithm. 

# Search algorithms

## Brief summary of search algorithms

Here we start with Depth-first search (DFS), and Breadth-first search (BFS) and then iteratively improve upon them to trade off the optimality, completeness, space complexity or time complexity. As Iterative deepening search (IDS) performs DFS with depth bound, making it complete and optimal.

We then introduce weighted arc costs, leading to the Lowest cost first search (LCFS) where instead of a queue, it uses a priority queue to sort the paths that we have to do, a primitive version of Dijkstra's. Best First Search (BestFS) introduces an admissible heuristic to it where we have a lower bound on how much it will cost to reach a goal. A* combines both BestFS and LCFS to create $f() = cost() + h()$, where f\_value combination of costs of the path until now and the heuristic value from the last node of the path.

We also have variants based on this Branch and Bound, ($BB$) performs DFS on the whole graph improving the Upper bound, $UB$, based on the lowest cost found so far and removing any path that has higher f\_value than the upper bound. Lastly, we have IDA* which iteratively increases our threshold based on the f\_values found so far, and Memory bound A*, ($MBA^{*}$) which keeps track of all the f_values found and updates them to be more accurate.

| algo                                                                       | complete?                       | optimal                      | O_s        | O_t     |
| -------------------------------------------------------------------------- | ------------------------------- | ---------------------------- | ---------- | ------- |
| DFS                                                                        | no                              | no                           | $b\cdot m$ | $b^{m}$ |
| BFS                                                                        | yes                             | yes (c = 0)                  | $b^{m}$    | $b^{m}$ |
| IDS                                                                        | yes                             | yes (c = 0)                  | $b\cdot m$ | $b^{m}$ |
| LCFS                                                                       | yes                             | yes (c > 0)                  | $b^{m}$    | $b^{m}$ |
| BestFS                                                                     | no (can be low, cycle)          | no (can be low, not true)    | $b^{m}$    | $b^{m}$ |
| A* (opt eff)                                                               | yes                             | yes (c > 0 , h>=0 , admiss.) | $b^{m}$    | $b^{m}$ |
| BB (DFS w $UB$)                                                           | no (init is DFS, $UB = \infty$) | yes                          | $b\cdot m$ | $b^{m}$ |
| IDA* (IDS $b_{new} = \min(\{\text{prvs} f(p)\})$ )                          | yes                             | yes                          | $b\cdot m$ | $b^{m}$ |
| Memory Bound A $h(p)\_{new} = \max(\text{minimum child f()}, h(p)_{old})$ | yes       | yes |  $b^{m}$ |  $b^{m}$ |

These are vanilla search algorithms and can be improved by introducing cycle checking by pruning repeated nodes in a path and using dynamic programming to keep track of repeated paths.

# Genetic Algorithm

## Stochastic Local Search variant

I learned about stochastic local search and how some of its variants can be used for finding a solution to constraint satisfaction problem such as Simmulated annealing or beam search. I found genetic algorithm to be the most interesting one as it simulates the evolutionary process. I have implemented a primitive version of the genetic algorithm where it chooses the variables based on the fitness score, cross breeds them and has a chance of mutation. This is best expressed by the picture below:
![Pasted image 20231211200436](https://github.com/PUSH-YA/AI_search_genetic/assets/91928008/e6ba549b-c896-44a2-a916-1d65be042277)
