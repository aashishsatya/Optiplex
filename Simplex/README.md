# Simplex

The script implements simplex method for solving linear programs (LPs) in Python. The reference used will mostly be Understanding and Using Linear Programming by Matousek et al. Focus will be conceptual rather than on speed and performance.

#### Running the program:

Write the coefficients of the variables in the objective function in cT.txt.

Write out the matrices A and b in the file Ab.txt. In particular, line 1 will contain A[0][0], A[0][1],...,A[0][n - 1] (where n is the number of variables), and b[0] at the end. Feeding in input in any other form is likely to give a dimension error.

Finally, run

```
python Simplex.py
```

to obtain the results.

Feel free to get in touch with me if you have suggestions/queries :)
