# Efficient Data Engine
## Features

1. Matrix Multiplication/Adding/Subtracting of N matrices
2. Sizing of a Matrix by filling with zeroes/custom input
3. Statistics Basics: Mean, Median, Mode, Standard Deviation, Variance
4. File Summarising (learn more below)

### File Summarising:
You can upload a basic csv file (give filepath) that contains data which will have the first row as labels and everything else as numbers. The following can be done on it:
- Calculation of all mean median mode (etc) of all labels
- Calculate of a particular statistical tendency of all the labels
- The same for any particular label

## List of commands:

<strong>
NOTE: 
datatype: int or float
<br> data: either space separated or comma separated </strong> 

### NORMAL MODE:

>  - `matmul` "datatype"     "number_of_matrices"

>  - `mean`  data 

>  - `median` data  (similarly for other tendencies)

>  - `std_dev` data  

>  - `var` data

Can calculate more than one tendency too

>  - `mode` `std_dev` data

### FILE MODE:
>  - `load`

After this, a prompt allows giving the file path.
Make sure your label has no spaces.

>  - `mean` label
>  - `mean`  (for overall file)
>  - `median` label2

>  - `file.close` to close the file and go back to normal mode


