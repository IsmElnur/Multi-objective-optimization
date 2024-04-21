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

## Progress of work

We'll create a vector of criterion weights using a scale of 1-10.  

| Scholarship | Qualification | Cost of living in the city | Diploma |
| :---:       |     :---:     |            :---:           |  :---:  |
| 4  |  6     | 2    | 8 |

By normalizing, we get the vector $\alpha=(0.2, 0.3, 0.1, 0.4)$.

#### 1) Method of replacing criteria with restrictions

We'll create a scoring matrix $A$ for the alternatives.

|       | 1     | 2     | 3     | 4     |
| :---: | :---: | :---: | :---: | :---: |
| A     | 1     | 10    | 1     | 4     |
| B     | 7     | 9     | 4     | 8     |
| C     | 5     | 7     | 7     | 6     |
| D     | 3     | 3     | 10    | 3     |

We'll choose the prestige of the diploma as the main criterion (criterion 4).

We'll set minimum acceptable levels for the remaining criteria:  
— The scholarship amount is not less than $0.2·A_{max1}$;  
— Teacher qualifications are at least $0.5·A_{max3}$;  
— The cost of living in the city is at least $0.3·A_{max4}$.  

We'll normalize the matrix (except for the column of the main criterion) using the formula:
$$A_{ij}=\frac{A_{ij}-A_{minj}}{A_{maxj}-A_{minj}}$$
where $A_{minj}$ and $A_{maxj}$ are minimum and maximum value in the column respectively.

|       | 1     | 2     | 3     | 4     |
| :---: | :---: | :---: | :---: | :---: |
| A     | 0     | 1    | 0     | 10     |
| B     | 1     | 0.85     | 1/3    | 8     |
| C     | 2/3     | 0.57     | 2/3     | 6     |
| D     | 1/3     | 0     | 1    | 3     |

Under the given conditions, alternatives are acceptable: MSU (B), MIPT (C). We'll choose MSU since this alternative has a higher score.

#### Formation and narrowing of the Pareto set

We'll choose the qualifications of teachers and the cost of living in the city as the main criteria. We'll generate the Pareto set using the graphical method.

![image](https://github.com/IsmElnur/Multi-objective-optimization/assets/37519575/4030c4f5-a860-4f0a-bdb3-abdb46fbdd3c)

Based on the graphics, we can say that the Manhattan geometry to the point of utopia is minimal for an alternative to MIPT. Therefore, this alternative is optimal.

#### Weighting and combining criteria

We'll compile a matrix of ratings of alternatives according to criteria using a scale of 1÷10.

|       | 1     | 2     | 3     | 4     |
| :---: | :---: | :---: | :---: | :---: |
| A     | 1     | 10    | 1     | 10     |
| B     | 7     | 9     | 4    | 8     |
| C     | 5     | 5     | 5     | 6     |
| D     | 3     | 3     | 10    | 3     |

We normalize the table:

|       | 1     | 2     | 3     | 4     |
| :---: | :---: | :---: | :---: | :---: |
| A     | 0.063     | 0.345    | 0.045     | 0.370     |
| B     | 0.438     | 0.310     | 0.182   | 0.296     |
| C     | 0.313     | 0.241     | 0.318     | 0.222     |
| D     | 0.188     | 0.103     | 0.455    | 0.111     |

We'll compile a matrix of criterion priority assessments and obtain a normalized vector of all criterion weights:

|       | 1     | 2     | 3     | 4     | amount per line | the normalized amount per line |
| :---: | :---: | :---: | :---: | :---: | :---:| :---: | 
| 1     | 1     | 0.667    | 2     | 0.5 | 4.167| 0.208 |
| 2     | 1.5     | 1     | 3   | 0.75   | 6.25| 0.313 |
| 3     | 0.5     | 0.33     | 1     | 0.25 | 2.08| 0.104 |
| 4     | 2     | 1.33     | 4    | 1     | 8.33| 0.417 |

The normalized vector of criteria weights $\alpha=(0.208, 0.313, 0.104, 0.417)$.

We'll multiply the normalized matrix by the normalized vector of criterion weights and obtain the values of the combined criterion for all alternatives:

``` math
\begin{pmatrix}
 0.063  &0.345 &0.045  &0.370  \\
 0.438  &0.310 &0.182  &0.296  \\
 0.313  &0.241  &0.318  &0.222  \\ 
 0.188  &0.103  &0.455  &0.111
\end{pmatrix}
\times \begin{pmatrix}
 0.063  \\
 0.313 \\
 0.104 \\
 0.417
\end{pmatrix}=\begin{pmatrix}
 0.280  \\
 0.331 \\
 0.266 \\
 0.165
\end{pmatrix}
```

The most acceptable alternative is MSU.




The algorithm for solving the multi-objective optimization problem is implemented in the Python programming language.  
