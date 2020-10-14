import os

def run_script():
    alphas = [1, 2]
    betas = [1, 2]
    tees = [0.1, 0.2]
    # File = "output.txt"
    # for alpha, beta, t in zip(alphas, betas, tees):
    for alpha in alphas:
        for beta in betas:
            for t in tees:
                file_name = "output_{0}_{1}_{2}.txt".format(alpha, beta, t)
                print("Executing: \t")
                print("python main.py -s mnist -a {0} -b {1} -t {2} > {3}".format(alpha, beta, t, file_name))
                # os.system("python main.py -s mnist -a {0} -b {1} -t {2} > {3}".format(alpha, beta, t, file_name))


if __name__ == '__main__':
    run_script()