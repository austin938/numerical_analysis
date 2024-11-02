from numerical.lecture.lecture_6.solver_6 import golden_section_search, successive_parabolic_interpolation as suc, newton

path = r"C:\Users\austi\OneDrive - NTHU\NTHU\physics\computer\numerical\lecture\lecture_6\data_1\\"


# parameters
nmax = 50
eps = 1.e-6
err = 1.e99
N = 0

# golden section search
a = 0.0
b = 2.0

# Newton's initial guess
x = 1

# successive parabolic interpolation
x_0 = 0.0
x_1 = 1.3
x_2 = (x_0 + x_1)/2

with open(path + 'gol_sec_1.txt', 'w') as file1:
    file1.write("# N, a, f(a), b, f(b) \n")
    while(err > eps):
        a, b, f_a, f_b, err = golden_section_search(a, b)
        N += 1
        file1.write(f"{N}, {a}, {f_a}, {b}, {f_b} \n")
        if N > nmax:
            print("The problem is not converged within", nmax)
            break

with open(path + 'suc_par_1.txt', 'w') as file2:
    file2.write("# N, x, f(x) \n")
    while(err > eps):
        x_0, x_1, x_2, f2, err = suc(x_0, x_1, x_2)
        N += 1
        file2.write(f"{N}, {x_2}, {f2}, {err} \n")
        if N > nmax:
            print("The problem is not converged within", nmax)
            break

with open(path + 'newton_1.txt', 'w') as file3:
    file3.write("# N, x, f(x) \n")
    while(err > eps):
        x, f, err = newton(x)
        N += 1
        file3.write(f"{N}, {x}, {f}, {err} \n")
        if N > nmax:
            print("The problem is not converged within", nmax)
            break