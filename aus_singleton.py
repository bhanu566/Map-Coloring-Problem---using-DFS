#AUS map coloring using singleton with heuristic
import copy
import random
# WA  = 'western australia'
# NT  = 'northwest territories'
# SA  = 'southern australia'
# Q   = 'queensland'
# NSW = 'new south wales'
# V   = 'victoria'
# T   = 'tasmania'
from flask import Flask, jsonify, render_template, request
import json
import time
app = Flask(__name__)

final_list_to_js=[]
final_color_to_js=[]

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

australia_negh = {
    SA:  [WA, NT, Q, NSW, V],
    Q:   [NT, SA, NSW],
    NT:  [WA, Q, SA],
    NSW: [Q, SA, V],
    WA: [NT, SA],
    V: [SA, NSW],
    T:   []
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
notconfirmed={}
assigned={}
stored={}
backtrack_count=0
#select the state to be colored
def select_var():
    global australia_negh,australia_colors,assigned,notconfirmed
    # print(australia_colors)
    #
    # oo=list(australia_negh.keys())
    #
    # for i in oo:
    #     if not i in list(assigned.keys()):
    #         return i
    # # print(var)
    if bool(australia_colors) != False:
        temp=[]
        least_value=4
        for i,j in australia_colors.items():
            if len(j) < least_value:
                temp.clear()
            if len(j) <= least_value:
                temp.append(i)
                least_value=len(j)
        high_value=0
        temp2=[]
        for i,j in australia_negh.items():
            if i in temp:
                if i not in assigned.keys():
                    if len(j)>high_value:
                        temp2.clear()
                    if len(j) >= high_value:
                        temp2.append(i)
                        high_value=len(j)
        # print(temp2)
        var=random.choice(temp2)
        return var
    elif bool(notconfirmed) !=False:
        for i in list(notconfirmed.keys()):
            return i


#Backtracking check
def check_backtrack(next_var,colour1):
    global australia_negh, australia_colors, assigned, stored
    for i in list(australia_colors.values()):
        if not i:
            return 1
    return 0



#Forward checking
def forward_checking(next_var,colour1):
    global australia_negh, australia_colors, assigned, stored,notconfirmed
    val = list(australia_negh[next_var])
    for i in val:
        if i not in list(assigned.keys()):
            if i not in list(notconfirmed.keys()):
                if colour1 in australia_colors[i]:
                    australia_colors[i].remove(colour1)



#Assign color for a state using forward checking and singleton check
def select_color(next_var):
    global australia_negh,australia_colors,assigned,stored,notconfirmed,final_color_to_js,final_list_to_js,aus_name
    if australia_colors[next_var]:
        # colour=australia_colors[next_var]
        colour1=australia_colors[next_var][0]
        colour2=australia_colors[next_var][1:]
        colour_list1={next_var:colour1}
        colour_list2={next_var:colour2}
        print("fixing colour to ",next_var,"----",colour1)
        final_list_to_js.append(next_var)
        final_color_to_js.append(colour1)
        aus_name.append(aus_naming[next_var])
        assigned.update(colour_list1)
        stored.update(colour_list2)
        # print(next_var,colour1)
        forward_checking(next_var, colour1)
        del(australia_colors[next_var])
        # print(australia_colors)
        check = 1
        while check != 0:
            check = singleton()



    return colour1


#Singleton check
def singleton():
    global australia_colors,australia_negh,notconfirmed
    for i, j in australia_colors.items():
        # print(j)
        if len(j) == 1:
            mm = list(australia_negh[i])
            cc = j[0]
            print("temporarly assigning colour to ", i, "----", cc)
            t = {i: cc}
            notconfirmed.update(t)
            del (australia_colors[i])
            # forward_checking(i,cc)

            for k in mm:
                if k in list(australia_colors.keys()):
                    australia_colors[k].remove(cc)

                    # print(notconfirmed)
            return 1


    return 0

#Main function to select a state,assign color and check for backtracking
def  solve():
    global australia_colors,australia_negh,notconfirmed,final_color_to_js,final_list_to_js
    global australia_colors,australia_negh
    global backtrack_count
    start = time.time()
    flag_backtrack=0
    while bool(australia_colors) != False or bool(notconfirmed) != False:

        if flag_backtrack != 1:
            next_var = select_var()
            if next_var not in list(notconfirmed.keys()):
                color = select_color(next_var)
            if next_var in list(notconfirmed.keys()):
                print("confirming colour to ",next_var,"----",notconfirmed[next_var])
                final_list_to_js.append(next_var)
                final_color_to_js.append(notconfirmed[next_var])
                aus_name.append(aus_naming[next_var])
                assigned.update({next_var:notconfirmed[next_var]})
                del (notconfirmed[next_var])
                next_var=select_var()



        flag_backtrack = check_backtrack(next_var, color)
        if flag_backtrack ==1:
            a=list(stored.items())
            g=list(a[-1])
            d = {g[0]: g[1]}
            australia_colors.update(d)
            del(assigned[next_var])
            del(stored[next_var])

    end = time.time()
    print("Total time taken", (end - start) * (10 ** 6), " micro seconds")
    print("total number of backtracks", backtrack_count)

    app.run()

@app.route('/')
#Visualization
def index():
    global final_list_to_js,final_color_to_js,aus_name
    title="Forward_checking and singleton _with_heuristic"

    return render_template('index.html',title=title,a=json.dumps(final_list_to_js),c=json.dumps(final_color_to_js),z=json.dumps(aus_name))


def main():
    solve()


if __name__ == "__main__":
    main()