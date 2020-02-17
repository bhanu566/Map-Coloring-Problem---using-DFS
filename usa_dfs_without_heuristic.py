#USA map coloring using dfs without heuristic

import copy
import random
from flask import Flask, jsonify, render_template, request
import json
import time
app = Flask(__name__)
back=0
AL = "US.AL"
AK = "US.AK"
AZ = "US.AZ"
AR = "US.AR"
CA = "US.CA"
CO = "US.CO"
CT = "US.CT"
DE = "US.DE"
FL = "US.FL"
GA = "US.GA"
HI = "US.HI"
ID = "US.ID"
IL = "US.IL"
IN = "US.IN"
IA = "US.IA"
KS = "US.KS"
KY = "US.KY"
LA = "US.LA"
ME = "US.ME"
MD = "US.MD"
MA = "US.MA"
MI = "US.MI"
MN = "US.MN"
MS = "US.MS"
MO = "US.MO"
MT = "US.MT"
NE = "US.NE"
NV = "US.NV"
NH = "US.NH"
NJ = "US.NJ"
NM = "US.NM"
NY = "US.NY"
NC = "US.NC"
ND = "US.ND"
OH = "US.OH"
OK = "US.OK"
OR = "US.OR"
PA = "US.PA"
RI = "US.RI"
SC = "US.SC"
SD = "US.SD"
TN = "US.TN"
TX = "US.TX"
UT = "US.UT"
VT = "US.VT"
VA = "US.VA"
WA = "US.WA"
WV = "US.WV"
WI = "US.WI"
WY = "US.WY"

usa_naming = {AL: 'alabama',
AK: 'alaska',
AZ: 'arizona',
AR: 'arkansas',
CA: 'california',
CO: 'colorado',
CT: 'connecticut',
DE: 'delaware',
FL: 'florida',
GA: 'georgia',
HI: 'hawaii',
ID: 'idaho',
IL: 'illinois',
IN: 'indiana',
IA: 'iowa',
KS: 'kansas',
KY: 'kentucky',
LA: 'louisiana',
ME: 'maine',
MD: 'maryland',
MA: 'massachusetts',
MI: 'michigan',
MN: 'minnesota',
MS: 'mississippi',
MO: 'missouri',
MT: 'montana',
NE: 'nebraska',
NV: 'nevada',
NH: 'newHampshire',
NJ: 'newJersey',
NM: 'newMexico',
NY: 'newYork',
NC: 'northCarolina',
ND: 'northDakota',
OH: 'ohio',
OK: 'oklahoma',
OR: 'oregon',
PA: 'pennsylvania',
RI: 'rhodeIsland',
SC: 'southCarolina',
SD: 'southDakota',
TN: 'tennessee',
TX: 'texas',
UT: 'utah',
VT: 'vermont',
VA: 'virginia',
WA: 'washington',
WV: 'westVirginia',
WI: 'wisconsin',
WY: 'wyoming'}

usa_name=[]
final_list_to_js=[]
final_color_to_js=[]

usa_negh = {
NE: [SD, WY, CO, KS, MO, IA],
IA: [MN, SD, NE, MO, WI, IL],
OK: [KS, CO, NM, TX, AR, MO],
    TN: [KY, MO, AR, MS, MO, AL, GA, NC],
    MO: [IA, NE, KS, OK, AR, IL, KY, TN],
AR: [MO, OK, TX, LA, TN, MS],
WY: [MT, SD, NE, CO, UT, ID],
    KY: [IN, IL, MO, TN, OH, WV, VA],
    CO: [WY, NE, KS, OK, NM, AZ, UT],
ID: [WA, MT, OR, WY, UT, NV],
UT: [ID, NV, WY, CO, AZ, NM],

    IL: [WI, IA, MO, KY, IN, MI],
    PA: [NY, OH, WV, DE, MD, NJ],
SD: [ND, MT, WY, NE, MN, IA],

HI: [],
    AK: [],
VA: [WV, KY, NC,MD,TN],
GA: [SC, NC, TN, AL, FL],
NY: [PA,VT,CT,MA,NJ],

AZ: [CA, NV, UT, CO, NM],
    IN: [MI, WI, IL, KY, OH],
OH: [MI, IN, KY, WV],
    WV: [OH, VA, KY, PA, MD],
MA: [NY,RI,VT,NH,CT],

    MS: [TN, AR, LA, AL],
KS: [NE, CO, OK, MO],
NM: [AZ, UT, CO, OK, TX],
NV: [OR, ID, UT, AZ, CA],

MD: [VA,WV,DE,PA],
    OR: [WA, ID, NV, CA],
    WI: [MN, IA, IL, MI],
    AL: [GA, FL, TN, MS],

CT: [NY,RI,MA],
NJ: [NY,PA,DE],
MI: [IL, WI, IN, OH],
    NC: [GA, TN, SC, VA],
MN: [ND, SD, IA, WI],
    MT: [ID, WY, SD, ND],
    TX: [OK, NM, AR, LA],
LA: [AR, TX, MS],
    DE: [NJ, PA, MD],
    NH: [VT, ME, MA],
    FL: [AL, GA],

VT: [NH,NY,MA],
ND: [MT, SD, MN],
CA: [OR, NV, AZ],
    RI: [MA, CT],
    WA: [OR, ID],

SC: [GA, NC],
    ME: [NH],




}


usa_colors = {
    AL: ["red", "green", "blue","yellow"],
    AK: ["red", "green", "blue","yellow"],
    AZ: ["red", "green", "blue","yellow"],
    AR: ["red", "green", "blue","yellow"],
    CA: ["red", "green", "blue","yellow"],
    CO: ["red", "green", "blue","yellow"],
    CT: ["red", "green", "blue","yellow"],
    DE: ["red", "green", "blue","yellow"],
    FL: ["red", "green", "blue","yellow"],
    GA: ["red", "green", "blue","yellow"],
    HI: ["red", "green", "blue","yellow"],
    ID: ["red", "green", "blue","yellow"],
    IL: ["red", "green", "blue","yellow"],
    IN: ["red", "green", "blue","yellow"],
    IA: ["red", "green", "blue","yellow"],
    KS: ["red", "green", "blue","yellow"],
    KY: ["red", "green", "blue","yellow"],
    LA: ["red", "green", "blue","yellow"],
    ME: ["red", "green", "blue","yellow"],
    MD: ["red", "green", "blue","yellow"],
    MA: ["red", "green", "blue","yellow"],
    MI: ["red", "green", "blue","yellow"],
    MN: ["red", "green", "blue","yellow"],
    MS: ["red", "green", "blue","yellow"],
    MO: ["red", "green", "blue","yellow"],
    MT: ["red", "green", "blue","yellow"],
    NE: ["red", "green", "blue","yellow"],
    NV: ["red", "green", "blue","yellow"],
    NH: ["red", "green", "blue","yellow"],
    NJ: ["red", "green", "blue","yellow"],
    NM: ["red", "green", "blue","yellow"],
    NY: ["red", "green", "blue","yellow"],
    NC: ["red", "green", "blue","yellow"],
    ND: ["red", "green", "blue","yellow"],
    OH: ["red", "green", "blue","yellow"],
    OK: ["red", "green", "blue","yellow"],
    OR: ["red", "green", "blue","yellow"],
    PA: ["red", "green", "blue","yellow"],
    RI: ["red", "green", "blue","yellow"],
    SC: ["red", "green", "blue","yellow"],
    SD: ["red", "green", "blue","yellow"],
    TN: ["red", "green", "blue","yellow"],
    TX: ["red", "green", "blue","yellow"],
    UT: ["red", "green", "blue","yellow"],
    VT: ["red", "green", "blue","yellow"],
    VA: ["red", "green", "blue","yellow"],
    WA: ["red", "green", "blue","yellow"],
    WV: ["red", "green", "blue","yellow"],
    WI: ["red", "green", "blue","yellow"],
    WY: ["red", "green", "blue","yellow"],
}


assigned={}
stored={}

#select the state to be colored
def select_var():
    global usa_negh, usa_colors, assigned
    # print(usa_colors)
    temp = []
    oo = list(usa_negh.keys())
    for i in oo:
        if not i in list(assigned.keys()):
            return i


#Backtracking check
def check_backtrack(next_var,colour1):
    global usa_negh, usa_colors, assigned, stored,back
    p=usa_negh[next_var]
    # print(p)
    for i in p:
        if i in assigned:
            if assigned[i]==colour1:
                print("backtracking")
                back=back+1
                return 1
    return 0

#Choose the color for a state
def select_color(next_var):
    global usa_negh,usa_colors,assigned,stored,final_color_to_js,final_list_to_js
    if usa_colors[next_var]:
        # colour=usa_colors[next_var]
        colour1=usa_colors[next_var][0]
        colour2=usa_colors[next_var][1:]
        colour_list1={next_var:colour1}
        colour_list2={next_var:colour2}
        print("Assigning colour to ",next_var,"----",colour1)
        final_list_to_js.append(next_var)
        final_color_to_js.append(colour1)
        usa_name.append(usa_naming[next_var])
        assigned.update(colour_list1)
        stored.update(colour_list2)
        del(usa_colors[next_var])

        return colour1


#Main function to select a state,assign color and check for backtracking
def  solve():
    global usa_colors,usa_negh,back
    global back
    start = time.time()
    flag_backtrack=0
    while bool(usa_colors) != False:
        if flag_backtrack != 1:
            next_var = select_var()

        color2=select_color(next_var)
        flag_backtrack = check_backtrack(next_var, color2)
        if flag_backtrack ==1:
            a=list(stored.items())
            g=list(a[-1])
            d = {g[0]: g[1]}
            if g[1]==[]:
                d={g[0]:["red", "green", "blue","yellow"]}
                del(assigned[g[0]])
                del(stored[g[0]])
                next_var=list(a[-2])[0]
                t=list(a[-2])[1]
                usa_colors.update({next_var:t})
            usa_colors.update(d)
            del(assigned[next_var])
            del(stored[next_var])

    end = time.time()
    print("Total time taken",(end-start)* (10**6)," micro seconds")
    print("total number of backtracks", back)

    app.run()

#Visualization
@app.route('/')
def index():
    global final_list_to_js,final_color_to_js,usa_name
    title="Depth first search without heuristic"

    return render_template('index2.html',title=title,a=json.dumps(final_list_to_js),c=json.dumps(final_color_to_js),z=json.dumps(usa_name))


def main():
    solve()


if __name__ == "__main__":
    main()