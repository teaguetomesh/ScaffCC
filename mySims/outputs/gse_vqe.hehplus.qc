qubits 2
map q0, reg0
map q1, reg1
map b0, result0
map b1, result1
Rx reg0,0.000000
Rx reg1,0.000000
Rx reg0,0.000000
Rx reg1,0.000000
H reg0
cnot reg0, reg1
H reg1
cnot reg1, reg0
Rz reg0,0.000000
Rz reg1,0.000000
Rz reg0,0.000000
Rz reg1,0.000000
Rz reg0,0.000000
Rz reg1,0.000000
measure reg0
measure reg1
display
