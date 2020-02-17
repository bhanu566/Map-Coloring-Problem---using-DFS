#AUS map coloring using dfs without heuristic
import copy
import time
from flask import Flask, jsonify, render_template, request
import json
app = Flask(__name__)

# WA  = 'western australia'
# NT  = 'northwest territories'
# SA  = 'southern australia'
# Q   = 'queensland'
# NSW = 'new south wales'
# V   = 'victoria'
# T   = 'tasmania'

WA  = 'AU.WA'
NT  = 'AU.NT'
SA  = 'AU.SA'
Q   = 'AU.QL'
NSW = 'AU.NS'
V   = 'AU.VI'
T   = 'AU.TS'

aus_naming = {WA: 'western australia', NT: 'northwest territories', SA: 'southern australia',
              Q: 'queensland'
    , NSW: 'new south wales',  V: 'victoria', T: 'tasmania'}

aus_name=[]
final_list_to_js=[]        #list to store final output order of states
final_color_to_js=[]        #lIST TO STORE final output state colorS
backtrack_count=0
australia_negh = {
    NT: [WA, Q, SA],
    SA:  [WA, NT, Q, NSW, V],
    NSW: [Q, SA, V],
    WA: [NT, SA],
    V: [SA, NSW],
    T: [],
    Q:   [NT, SA, NSW]



              }

australia_colors = {
    T: ["red", "green", "blue"],
    WA: ["red", "green", "blue"],
    NT: ["red", "green", "blue"],
    SA: ["red", "green", "blue"],
    Q: ["red", "green", "blue"],
    NSW: ["red", "green","blue"],
    V: ["red", "green", "blue"]
}

assigned={}
stored={}
#select the state to be colored
def select_var():
    global australia_negh, australia_colors, assigned
    # print(australia_colors)
    temp = []
    oo = list(australia_negh.keys())
    for i in oo:
        if not i in list(assigned.keys()):
            return i
    # print(var)


#Backtracking check
def check_backtrack(next_var,colour1):
    global australia_negh, australia_colors, assigned, stored,backtrack_count
    p=australia_negh[next_var]
    # print(p)
    for i in p:
        if i in assigned:
            if assigned[i]==colour1:
                print("backtracking")
                backtrack_count=backtrack_count+1
                return 1
    return 0


#Choose the color for a state
def select_color(next_var):
    global australia_negh,australia_colors,assigned,stored,final_color_to_js,final_list_to_js
    if australia_colors[next_var]:
        # colour=australia_colors[next_var]
        colour1=australia_colors[next_var][0]
        colour2=australia_colors[next_var][1:]
        colour_list1={next_var:colour1}
        colour_list2={next_var:colour2}
        print("Assigning colour to ",next_var,"----",colour1)
        final_list_to_js.append(next_var)
        final_color_to_js.append(colour1)
        aus_name.append(aus_naming[next_var])
        assigned.update(colour_list1)
        stored.update(colour_list2)
        del(australia_colors[next_var])

    return colour1



#Main function to select a state,assign color and check for backtracking
def  solve():
    global backtrack_count
    start = time.time()
    global australia_colors,australia_negh,final_color_to_js,final_list_to_js
    flag_backtrack=0
    while bool(australia_colors) != False:
        if flag_backtrack != 1:
            next_var = select_var()

        color=select_color(next_var)
        flag_backtrack = check_backtrack(next_var, color)
        if flag_backtrack ==1:
            a=list(stored.items())
            g=list(a[-1])
            d = {g[0]: g[1]}
            australia_colors.update(d)
            del(assigned[next_var])
            del(stored[next_var])

    end = time.time()
    print("Total time taken",(end-start)* (10**6)," micro seconds")
    print("total number of backtracks", backtrack_count)

    app.run()


#Visualization
@app.route('/')
def index():
    global final_list_to_js,final_color_to_js,aus_name
    title="Depth first searach without heuristic"

    return render_template('index.html',title=title,a=json.dumps(final_list_to_js),c=json.dumps(final_color_to_js),z=json.dumps(aus_name))


def main():

    solve()


if __name__ == "__main__":
    main()