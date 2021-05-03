namespace nonlocal {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Math;
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Diagnostics;
    open Microsoft.Quantum.Logical;

    
    operation GenerateRandomBit() : Result {
        //Message("Hello quantum world!");
        use q = Qubit();
        H(q);
        let r = M(q);
        Reset(q);
        return r;
    }

    @EntryPoint()
    operation move(index:Int) : Result[] {
        if index == 0 {return move000();}
        elif index == 1 {return move001();}
        elif index == 2 {return move010();}
        elif index == 3 {return move011();}
        elif index == 4 {return move100();}
        elif index == 5 {return move101();}
        elif index == 6 {return move110();}
        elif index == 7 {return move111();}
        elif index == 8 {return cal00();}
        elif index == 9 {return cal01();}
        elif index == 10 {return cal10();}
        elif index == 11 {return cal11();}
        else {return [Zero];}
    }

    operation move000() : Result[] {
        // Allocate a qubit.
        use qb = Qubit[6]; 
        for n in 0..2 {
            H(qb[2*n]);
            CX(qb[2*n],qb[(2*n+1)%6]);
            CX(qb[2*n],qb[(2*n+5)%6]);
            H(qb[2*n]);
            }
        return MultiM(qb);
    }
  
    operation move001() : Result[] {
        // Allocate a qubit.
        use qb = Qubit[6]; 
        for n in 0..2 {
            H(qb[2*n]);
            CX(qb[2*n],qb[(2*n+1)%6]);
            CX(qb[2*n],qb[(2*n+5)%6]);
			}
		R(PauliZ, PI()/2.0, qb[4]);
		for n in 0..2 {
            H(qb[2*n]);
            }
        return MultiM(qb);
    }

    
    operation move010() : Result[] {
        // Allocate a qubit.
        use qb = Qubit[6]; 
        for n in 0..2 {
            H(qb[2*n]);
            CX(qb[2*n],qb[(2*n+1)%6]);
            CX(qb[2*n],qb[(2*n+5)%6]);
			}
		R(PauliZ, PI()/2.0, qb[2]);
		for n in 0..2 {
            H(qb[2*n]);
            }
        return MultiM(qb);
    }

    
    operation move011() : Result[] {
        // Allocate a qubit.
        use qb = Qubit[6]; 
        for n in 0..2 {
            H(qb[2*n]);
            CX(qb[2*n],qb[(2*n+1)%6]);
            CX(qb[2*n],qb[(2*n+5)%6]);
			}
		R(PauliZ, PI()/2.0, qb[4]);
		R(PauliZ, PI()/2.0, qb[2]);
		for n in 0..2 {
            H(qb[2*n]);
            }
        return MultiM(qb);
    }

    
    operation move100() : Result[] {
        // Allocate a qubit.
        use qb = Qubit[6]; 
        for n in 0..2 {
            H(qb[2*n]);
            CX(qb[2*n],qb[(2*n+1)%6]);
            CX(qb[2*n],qb[(2*n+5)%6]);
			}
		R(PauliZ, PI()/2.0, qb[0]);
		for n in 0..2 {
            H(qb[2*n]);
            }
        return MultiM(qb);
    }

    
    operation move101() : Result[] {
        // Allocate a qubit.
        use qb = Qubit[6]; 
        for n in 0..2 {
            H(qb[2*n]);
            CX(qb[2*n],qb[(2*n+1)%6]);
            CX(qb[2*n],qb[(2*n+5)%6]);
			}
		R(PauliZ, PI()/2.0, qb[4]);
		R(PauliZ,PI()/2.0,qb[0]);
		for n in 0..2 {
            H(qb[2*n]);
            }
        return MultiM(qb);
    }

    
    operation move110() : Result[] {
        // Allocate a qubit.
        use qb = Qubit[6]; 
        for n in 0..2 {
            H(qb[2*n]);
            CX(qb[2*n],qb[(2*n+1)%6]);
            CX(qb[2*n],qb[(2*n+5)%6]);
			}
		R(PauliZ, PI()/2.0, qb[2]);
		R(PauliZ,PI()/2.0,qb[0]);
		for n in 0..2 {
            H(qb[2*n]);
            }
        return MultiM(qb);
    }
    
    operation move111() : Result[] {
        // Allocate a qubit.
        use qb = Qubit[6]; 
        for n in 0..2 {
            H(qb[2*n]);
            CX(qb[2*n],qb[(2*n+1)%6]);
            CX(qb[2*n],qb[(2*n+5)%6]);
			}
		R(PauliZ, PI()/2.0, qb[4]);
		R(PauliZ, PI()/2.0, qb[2]);
		R(PauliZ,PI()/2.0,qb[0]);
		for n in 0..2 {
            H(qb[2*n]);
            }
        return MultiM(qb);
    }


    operation calibrate(index:Int) : Result[] {
        if index == 0 {return cal00();}
        elif index == 1 {return cal01();}
        elif index == 2 {return cal10();}
        elif index == 3 {return cal11();}
        else {return [Zero];}
    }


    operation cal00() : Result[] {
        // Allocate a qubit.
        use qb = Qubit[6]; 
        return MultiM(qb);
    }

    operation cal01() : Result[] {
        // Allocate a qubit.
        use qb = Qubit[6]; 
        for n in 0..2 {
            X(qb[2*n+1]);
            }
        return MultiM(qb);
    }

    operation cal10() : Result[] {
        // Allocate a qubit.
        use qb = Qubit[6];
        for n in 0..2 {
            X(qb[2*n]);
            } 
        return MultiM(qb);
    }

    operation cal11() : Result[] {
        // Allocate a qubit.
        use qb = Qubit[6];
        for n in 0..5 {
            X(qb[n]);
            } 
        return MultiM(qb);
    }
}
