# QuantumParenthesis
A lispy quantum language experiment


Dependencies:
Python 3 
Numpy 


How to use:

Running qsch2.py launches a repl (read-eval-print loop) for the language that will interpret any expression given to it

``` 
qsch> (+ 2 2)
4
``` 

Vectors are represented by lists and operators/matrices by lists of lists.

For example, let's create a state of two qubits |01>, apply flip to the second one and measure them:

``` 
qsch> (define state (tensor (list 1 0) (list 0 1)))  ;our state is the tensor product of |0> and |1>

qsch> (define id (list     			     ;define identity and flip matrices
		  (list 1 0)
		  (list 0 1)))

qsch> (define flip (list
		    (list 0 1)
		    (list 1 0)))

qsch> (measure (apply (tensor id flip) state))       ;apply the tensor product ID (x) FLIP to our state (essentialy flipping the second bit) and measure
Probability of state 0 is 1.0
Probability of state 1 is 0.0
Probability of state 2 is 0.0
Probability of state 3 is 0.0
System collapsed to state: 0
0
``` 

As we can see, after our measurment we will always observe the state |00>.


Definitions can also be written on a seperate file which can be then loaded at repl

For example let's load deutsch.qsch (.qsch files are just plaintext files with a .qsch extension! You can edit them in any text editor)

``` 
qsch> (load "deutsch.qsch") 			     ;general syntax : (load "filename")

qsch> hadamard 					     ;invoking an operator defined in deutsch.qsch works as expected
(((0.7071067811865475+0i) (0.7071067811865475+0i)) 
((0.7071067811865475+0i) (-0.7071067811865475+0i)))
``` 



