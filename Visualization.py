from random import random
from math import ceil, sqrt, nan
import matplotlib.pyplot as plt 
from matplotlib.ticker import MaxNLocator

def create_chart_combination(n: int, k:int)->list[list[int], list[int], list[int]]:
    """
    Premise (See the accompanying PDF)
    -----------------------------------------------------------------------------
    | n     | k     | y                                                         |
    -----------------------------------------------------------------------------
    | Even  | n//2  | y = (a-1)\times n//2 - a\times x                          |
    | Even  | n//2-l| y = (a-1)\times n//2 + l \times (a+1) - a\times x         |
    | Even  | n//2+m| y = (a-1)\times n//2 - m \times (a+1) - a\times x         |
    | Odd   | n//2  | y = (a-1)\times n//2 + a - a\times x                      |
    | Odd   | n//2-l| y = (a-1)\times n//2 + a + l\times(a+1) - a\times x       |
    | Odd   | n//2+m| y = (a-1)\times n//2 + a -m\times(a+1) - a\times x        |
    -----------------------------------------------------------------------------
    The chart can be made in the following step.
    1. Decide n is even or odd.
    2. given k and n, decide if l or m is there and if yes what value.
    3. Get range of x such that 0 <= x <= (n-k-1)
    4. Solve for a(s) and y(s) for each x with restrain that 1 <= y <= (n-k).
    5. Return a list of three lists [x, y, a] # for plotting
    """
    IS_EVEN = n%2 == 0
    l, not_l_m, m = n//2-k if k < n//2 else None, n//2 if k==n//2 else None, k-n//2 if k > n//2 else None
    x = list(range(0,n-k,1))
    y = []
    solution_params = []    
    for each_x in x:
        a = []
        starting_guess = 1
        indiv_solution_params = []
        if IS_EVEN:
            if not_l_m:
                while True:
                    y_ = (starting_guess-1)*n//2 - (starting_guess*each_x)
                    if y_ > (2*(n//2)-k):
                        break                    
                    if y_ >= 1:
                        a.append(starting_guess)
                        indiv_solution_params.append((l,not_l_m,m,starting_guess))
                    starting_guess += 1
                y_s = list(map(lambda a_dash: (a_dash-1)*n//2 - (a_dash*each_x),a))
                y.append(y_s)
            elif l:
                while True:
                    y_ = (starting_guess-1)*(n//2) + l*(starting_guess+1) - (starting_guess*each_x)
                    if y_ > (2*(n//2)-k):
                        break
                    if y_ >= 1:
                        a.append(starting_guess)
                        indiv_solution_params.append((l,not_l_m,m,starting_guess))
                    starting_guess += 1
                y_s = list(map(lambda a_dash: (a_dash-1)*(n//2) +l*(a_dash+1) - (a_dash*each_x),a))
                y.append(y_s)    
            elif m:
                while True:
                    y_ = (starting_guess-1)*(n//2) -m*(starting_guess+1) - (starting_guess*each_x)
                    if y_ > (2*(n//2)-k):
                        break                    
                    if y_ >= 1:
                        a.append(starting_guess)
                        indiv_solution_params.append((l,not_l_m,m,starting_guess))
                    starting_guess += 1
                y_s = list(map(lambda a_dash: (a_dash-1)*(n//2) -m*(a_dash+1) - (a_dash*each_x),a))
                y.append(y_s)  
        else:
            if not_l_m:
                while True:
                    y_ = (starting_guess-1)*(n//2) +starting_guess - (starting_guess*each_x)
                    if y_ > ((2*(n//2)+1)-k):
                        break                    
                    if y_ >= 1:
                        a.append(starting_guess)
                        indiv_solution_params.append((l,not_l_m,m,starting_guess))
                    starting_guess += 1
                y_s = list(map(lambda a_dash: (a_dash-1)*(n//2)+a_dash - (a_dash*each_x),a))
                y.append(y_s)
            elif l:
                while True:
                    y_ = (starting_guess-1)*(n//2) +starting_guess + l*(starting_guess+1) - (starting_guess*each_x)
                    if y_ > ((2*(n//2)+1)-k):
                        break                    
                    if y_ >= 1:
                        a.append(starting_guess)
                        indiv_solution_params.append((l,not_l_m,m,starting_guess))
                    starting_guess += 1
                y_s = list(map(lambda a_dash: (a_dash-1)*(n//2)+a_dash +l*(a_dash+1) - (a_dash*each_x),a))
                y.append(y_s)    
            elif m:
                while True:
                    y_ = (starting_guess-1)*(n//2) +starting_guess -m*(starting_guess+1) - (starting_guess*each_x)
                    if y_ > ((2*(n//2)+1)-k):
                        break                    
                    if y_ >= 1:
                        a.append(starting_guess)
                        indiv_solution_params.append((l,not_l_m,m,starting_guess))
                    starting_guess += 1
                y_s = list(map(lambda a_dash: (a_dash-1)*(n//2)+a_dash -m*(a_dash+1) - (a_dash*each_x),a))
                y.append(y_s) 
        solution_params.append(indiv_solution_params)
    returned_x = []
    returned_y = []
    returned_params = []
    for each_y_list_index, each_y_list in enumerate(y):
        solution_params_ = solution_params[each_y_list_index]
        for each_y_index, each_y in enumerate(each_y_list):
            returned_x.append(x[each_y_list_index])
            returned_y.append(each_y)
            returned_params.append(solution_params_[each_y_index])
    returned_results = [returned_x, returned_y, returned_params]
    return returned_results

def create_one_case_graph(n: int, k: int)->None:
    max = n
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12,12))
    ax.set_xlim(right=n+1)
    ax.set_xlim(left=-1)
    ax.set_ylim(top=n+1)
    ax.set_ylim(bottom=0)
    ax.set_xticks(ticks=list(range(1,n-k,1)), labels=[str(i) for i in range(1,n-k,1)])
    ax.yaxis.set_major_locator(MaxNLocator(integer=True, min_n_ticks=1))
    ax.xaxis.set_major_locator(MaxNLocator(integer=True, min_n_ticks=1))
    x, y, params = create_chart_combination(n,k)
    ax.scatter(x=x, y=y, c=[[0,0,0]], marker='o')
    ax.grid(which='both')
    ax.set_title('$ ^{%d}C_{%d}$'%(n,k))
    for data_index, _ in enumerate(params):
        param = _
        annotation = f"a={param[3]}"
        xy = (x[data_index], y[data_index])
        ax.annotate(annotation, xy=xy, xytext=(10,-20),textcoords='offset pixels')
    ax.set_xlabel('x as in denominator (n-k-x)')
    ax.set_ylabel('y as in numerator (k+y)')
    fig.savefig(f'./{n}_{k}_alone.png')
    plt.close()

def create_all_cases_graph(n: list[int, int])->None:
    """
    Supplied one even and one add number. 0th index should be even while 1st index should be odd.
    """
    assert n[0]%2==0 and n[1]%2
    markers = ["o","v","1","s","p","P","*","H","D","X"]
    fig, axs1 = plt.subplots(nrows=int(ceil(sqrt(n[0]))),ncols=int(ceil(sqrt(n[0]))), sharey=True, sharex=True)
    for axs_row in axs1:
        for axs_col in axs_row:
            axs_col.yaxis.set_major_locator(MaxNLocator(integer=True, min_n_ticks=1))
            axs_col.xaxis.set_major_locator(MaxNLocator(integer=True, min_n_ticks=1))
    ## Draw for even numbers
    counter = 0
    for k in range(1,n[0],1):
        if(k%int(ceil(sqrt(n[0])))==0):
            counter += 1        
        x, y, params = create_chart_combination(n[0],k)
        axs1[counter][k%int(ceil(sqrt(n[0])))].scatter(x=x, y=y, c=[[0,0,0]], marker=markers[k%(len(markers)-1)])
        axs1[counter][k%int(ceil(sqrt(n[0])))].grid(which='both')
        axs1[counter][k%int(ceil(sqrt(n[0])))].set_title('$ ^{%d}C_{%d}$'%(n[0],k))
        for data_index, _ in enumerate(params):
            param = _
            annotation = f"a={param[3]}"
            xy = (x[data_index], y[data_index])
            axs1[counter][k%int(ceil(sqrt(n[0])))].annotate(annotation, xy=xy, xytext=(10,-10),textcoords='offset pixels')
    fig.suptitle("Graph for various nCk, where n is even")
    fig.supxlabel("x as in denominator (n-k-x)")
    fig.supylabel("y as in numerator (k+y)")
    
    fig, axs2 = plt.subplots(nrows=int(ceil(sqrt(n[1]))),ncols=int(ceil(sqrt(n[1]))), sharey=True, sharex=True)
    for axs_row in axs2:
        for axs_col in axs_row:
            axs_col.yaxis.set_major_locator(MaxNLocator(integer=True, min_n_ticks=1))
            axs_col.xaxis.set_major_locator(MaxNLocator(integer=True, min_n_ticks=1))    
    ## Draw for odd numbers
    counter = 0
    for k in range(1,n[1],1):
        if(k%int(ceil(sqrt(n[1])))==0):
            counter += 1        
        x, y, params = create_chart_combination(n[1],k)
        axs2[counter][k%int(ceil(sqrt(n[1])))].scatter(x=x, y=y, c=[[0,0,0]], marker=markers[k%(len(markers)-1)])
        axs2[counter][k%int(ceil(sqrt(n[1])))].grid(which='both')
        axs2[counter][k%int(ceil(sqrt(n[1])))].set_title('$ ^{%d}C_{%d}$'%(n[1],k))
        for data_index, _ in enumerate(params):
            param = _
            annotation = f"a={param[3]}"
            xy = (x[data_index], y[data_index]) 
            axs2[counter][k%int(ceil(sqrt(n[1])))].annotate(annotation, xy=xy, xytext=(10,-10),textcoords='offset pixels')       
    fig.suptitle("Graph for various nCk, where n is odd")
    fig.supxlabel("x as in denominator (n-k-x)")
    fig.supylabel("y as in numerator (k+y)")

    plt.show()        


                    
if __name__ == "__main__":
    create_all_cases_graph([2,3])
    create_all_cases_graph([4,5])
    create_all_cases_graph([6,7])
    create_all_cases_graph([8,9])
    create_all_cases_graph([10,11])  
    create_all_cases_graph([12,13])
    
    n=25
    for k in range(1,n,1):
        create_one_case_graph(n, k)