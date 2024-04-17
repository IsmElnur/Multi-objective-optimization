# Multi-objective optimization  

This is the process of simultaneous optimization of two or more conflicting objective functions within a given domain of definition.  

Multi-objective optimization problems are found in many areas of science, technology and economics.  

## Formulation of the problem  

To choose the best of the alternatives for solving the proposed task of the specified criteria using the following methods:  

1. replacing criteria with restrictions;
2. formation and narrowing of the Pareto set;  
3. method of weighing and combining criteria;  
4. hierarchy analysis method.

Choosing a university for admission:  

Alternatives:  

A. Oxford  
B. MSU  
C. MIPT  
D. TSU  

  
Description of preferences:  

1. Scholarship amount  
2. Teacher qualifications  
3. Cost of living in the city
4. Prestige of the diploma


Criteria:

1. Scholarship amount: Oxford doesn't pay scholarships to students, at the TSU the scholarship is small, at the MIPT – more, at the MSU – significantly more.  
2. Teacher qualifications: the most qualified teachers are at Oxford, slightly less qualified at the MSU, less qualified at the MIPT, and the lowest qualified teachers at the TSU.  
3. Cost of living in the city: the lowest cost of living is in Tomsk, significantly higher in Dolgoprudny, much higher in Moscow, the highest cost of living is in London.  
4. Prestige of the diploma: the most prestigious diploma is at Oxford, slightly less at the MSU, less prestigious at the MIPT, and the least prestigious at the TSU.  


We compose a vector of criterion weights using a scale of 1-10.  

| Scholarship | Qualification | Cost of living in the city | Diploma |
| :---:       |     :---:     |            :---:           |  :---:  |
| 6   | 8     | 4    | 2 |

By normalizing, we get the vector $α = (0.3, 0.4, 0.2, 0.1)$.

The algorithm for solving the multi-objective optimization problem is implemented in the Python programming language.  
