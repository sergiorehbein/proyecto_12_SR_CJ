#!/usr/bin/env python
# coding: utf-8

# # $\Phi$-SO demo (quick SR)

# In[1]:


# External packages
import numpy as np
import matplotlib.pyplot as plt
import torch
# Internal code import
import physo


# ### Fixing seed

# In[2]:

if __name__ == '__main__':

    # Seed
    seed = 0
    np.random.seed(seed)
    torch.manual_seed(seed)


    # ### Dataset

    # In[3]:

    def nguyen1(x):
        return x**3 + x**2 + x

    def nguyen2(x):
        return x**4 + x**3 + x**2 + x

    def nguyen3(x):
        return x**5 + x**4 + x**3 + x**2 + x

    def nguyen4(x):
        return x**6 + x**5 + x**4 + x**3 + x**2 + x

    def nguyen5(x):
        return np.sin(x**2) * np.cos(x) - 1

    def nguyen6(x):
        return np.sin(x) + np.sin(x + x**2)

    def nguyen7(x):
        # Exclude -1 to avoid log(0)
        return np.log(x + 1) + np.log(x**2 + 1)

    def nguyen8(x):
        # Start from a very small positive number to avoid sqrt of negative numbers
        return np.sqrt(x)
    # Dataset
    #z = np.random.uniform(-10, 10, 50)
    #v = np.random.uniform(-10, 10, 50)


    X =np.random.uniform(-1, 1, [1, 100])

    nguyen_functions = [nguyen1]

    for func in nguyen_functions:
    # Generar datos X, y para la función actual
   
        y = func(X[0])

       
        expression, logs = physo.SR(X, y,
                                    X_units = [ [0, 0, 0] ],
                                    y_units = [0,0 , 0],
                                    fixed_consts       = [ 0 ],
                                    fixed_consts_units = [ [0,0,0] ],
                                    free_consts_units  = [ [0, 0, 0] , [0, 0, 0] ],                          
        )
        print(expression.get_infix_pretty(do_simplify=True))



        # Inspecting the best expression found
        # In ascii
        print("\nIn ascii:")
        print(expression.get_infix_pretty(do_simplify=True))
        # In latex
        print("\nIn latex")
        print(expression.get_infix_latex(do_simplify=True))
        # Free constants values
        print("\nFree constants values")
        print(expression.free_const_values.cpu().detach().numpy())


    


