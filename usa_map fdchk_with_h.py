#USA map coloring using forwardchecking with heuristic
import copy
import random
from flask import Flask, jsonify, render_template, request
import json
import time
back=0  #variable to store backtracking
app = Flask(__name__)

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
    MO: [IA, NE, KS, OK, AR, IL, KY, TN],
    TN: [KY, MO, AR, MS, MO, AL, GA, NC],
    KY: [IN, IL, MO, TN, OH, WV, VA],
    CO: [WY, NE, KS, OK, NM, AZ, UT],
ID: [WA, MT, OR, WY, UT, NV],
UT: [ID, NV, WY, CO, AZ, NM],
AR: [MO, OK, TX, LA, TN, MS],
WY: [MT, SD, NE, CO, UT, ID],
    IL: [WI, IA, MO, KY, IN, MI],
    PA: [NY, OH, WV, DE, MD, NJ],
SD: [ND, MT, WY, NE, MN, IA],
NE: [SD, WY, CO, KS, MO, IA],
IA: [MN, SD, NE, MO, WI, IL],
OK: [KS, CO, NM, TX, AR, MO],

VA: [WV, KY, NC,MD,TN],
NM: [AZ, UT, CO, OK, TX],
NV: [OR, ID, UT, AZ, CA],
GA: [SC, NC, TN, AL, FL],
NY: [PA,VT,CT,MA,NJ],
AZ: [CA, NV, UT, CO, NM],
    IN: [MI, WI, IL, KY, OH],
    WV: [OH, VA, KY, PA, MD],
MA: [NY,RI,VT,NH,CT],
OH: [MI, IN, KY, WV],
    MS: [TN, AR, LA, AL],
KS: [NE, CO, OK, MO],
MD: [VA,WV,DE,PA],
MI: [IL, WI, IN, OH],
    NC: [GA, TN, SC, VA],
MN: [ND, SD, IA, WI],
    MT: [ID, WY, SD, ND],
    TX: [OK, NM, AR, LA],
    OR: [WA, ID, NV, CA],
    WI: [MN, IA, IL, MI],
    AL: [GA, FL, TN, MS],
CT: [NY,RI,MA],
ND: [MT, SD, MN],
CA: [OR, NV, AZ],
NJ: [NY,PA,DE],
VT: [NH,NY,MA],
LA: [AR, TX, MS],
    DE: [NJ, PA, MD],
    NH: [VT, ME, MA],
    FL: [AL, GA],
    RI: [MA, CT],
    WA: [OR, ID],
SC: [GA, NC],
    ME: [NH],
HI: [],
    AK: [],



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
    temp = []
    least_value = 4
    for i, j in usa_colors.items():
        if len(j) < least_value:
            temp.clear()
        if len(j) <= least_value:
            temp.append(i)
            least_value = len(j)
    high_value = 0
    temp2 = []
    for i, j in usa_negh.items():
        if i in temp:
            if i not in assigned.keys():
                if len(j) > high_value:
                    temp2.clear()
                if len(j) >= high_value:
                    temp2.append(i)
                    high_value = len(j)
    # print(temp2)
    var = random.choice(temp2)
    return var


#Backtracking check
def check_backtrack(next_var,colour1):
    global usa_negh, usa_colors, assigned, stored
    for i in list(usa_colors.values()):
        if not i:
            return 1
    return 0


#Forward checking
def forward_checking(next_var,colour1):
    global usa_negh, usa_colors, assigned, stored
    val = list(usa_negh[next_var])
    for i in val:
        if i not in list(assigned.keys()):
            if colour1 in usa_colors[i]:
                usa_colors[i].remove(colour1)

#Assign color for a state using forward checking
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
        forward_checking(next_var, colour1)
        del(usa_colors[next_var])


    return colour1


#Main function to select a state,assign color and check for backtracking
def  solve():
    global usa_colors,usa_negh,back
    flag_backtrack=0
    start=time.time()
    while bool(usa_colors) != False:
        if flag_backtrack != 1:
            next_var = select_var()

        color=select_color(next_var)

        flag_backtrack = check_backtrack(next_var, color)
        if flag_backtrack ==1:
            a=list(stored.items())
            g=list(a[-1])
            d = {g[0]: g[1]}
            usa_colors.update(d)
            del(assigned[next_var])
            del(stored[next_var])

    end=time.time()
    print("Total time taken", (end - start) * (10 ** 6), " micro seconds")
    print("total number of backtracks", back)

    app.run()



@app.route('/')
#Visualization
def index():
    global final_list_to_js,final_color_to_js,usa_name
    title="Forward_checking_with_heuristic"

    return render_template('index2.html',title=title,a=json.dumps(final_list_to_js),c=json.dumps(final_color_to_js),z=json.dumps(usa_name))


def main():
    solve()


if __name__ == "__main__":
    main()