
def caculateAfterSingleConditions():
    sales = {}

    # sales["all_21"] = ???
    sales["rate_period_36"] = {}
    sales["rate_period_36"]["sm1"] = 4086

    # step 1:
    # add mp3_25 100
    # old_fee_uw["sm25"] += 100*sales["mp3_25"]   #169929.5   ok
    # fee_uw["rate_period_36"]["sm1"] = fee_uw["rate_period_36"]["sm1"]+100.0*sales["rate_period_36"]["sm1"]
    
    #add all product in sm1 by 100
    old_fee_uw = {}
    old_fee_uw["rate_period_36"] = {}    
    temp = 100.0*(sales["rate_period_36"]["sm1"])
    old_fee_uw["rate_period_36"]["sm1"] = 24467.25
    # new_fee_uw["rate_period_36"]["sm1"] += temp

    old_lr_uw = {}
    new_fee_uw = {}
    new_lr_uw = {}
    new_lr_uw["sm1"] = {}
    # # new_lr_uw for each cm is: old_lr_uw/(1+(delta_fee*sales/old_fee_uw))
    # old_lr_uw["sm25"] = {}
    old_lr_uw["sm1"] = {}
    # old_lr_uw["rate_period_36"] = {}
    # old_lr_uw["sm25"]["cm2"] = 101.12
    old_lr_uw["sm1"]["cm14"] = 127.59
    new_lr_uw["sm1"]["cm14"] = old_lr_uw["sm1"]["cm14"]/(1+(100*sales["rate_period_36"]["sm1"]/old_fee_uw["rate_period_36"]["sm1"]))
    print("new_lr_uw = ",new_lr_uw["sm1"]["cm14"])

def caculateAfterSingleConditions_1():
    # block the center product
    if True:

        # distribution data
        cfd = {}
        cfd["cm19"] = 0.23726374699999997

        # cover data
        old_fee_uw = {}
        sales = {}
        fee_uw = {}
        new_fee_uw = {}

        sales["rate_period_36"] = {}
        sales["rate_period_36"]["sm1"] = 4086

        fee_uw["center"] = {}
        fee_uw["center"]["sm11"] = 2403

        fee_uw["all_1"] = 24467

        fee_uw["rate_period_36"] = {}
        fee_uw["rate_period_36"]["sm1"] = 24467

        old_fee_uw["sm11"] = 38327.25
        # print("new_fee_uw_sm11",new_fee_uw["sm11"])

        #claim data
        claim_cost = {}
        claim_cost["center"] = {}
        claim_cost["center"]["sm11"] = {}
        # claim_cost["center"]["sm11"]["cm19"] = 213.19
        claim_cost["center"]["sm11"]["cm19"] = 202.62
        # claim_cost["center"]["sm11"]["cm19"] = 415.81
        
        old_claim_cost = {}
        old_claim_cost["sm11"] = {}
        old_claim_cost["sm11"]["cm19"] = 7500.0
        new_claim_cost = {}
        new_claim_cost["sm11"] = old_claim_cost["sm11"]["cm19"]-claim_cost["center"]["sm11"]["cm19"]
        # print("new_claim_cost_sm11 = ",new_claim_cost["sm11"])

    # mp3,200,DVD,200 add 5 and 10 respectively
    # center,200 and GPS 700 block
    new_fee_uw["sm11"] = old_fee_uw["sm11"]- fee_uw["center"]["sm11"]
    old_lr_uw = old_claim_cost["sm11"]["cm19"]/(old_fee_uw["sm11"]*cfd["cm19"])
    new_lr_uw = new_claim_cost["sm11"]/(new_fee_uw["sm11"]*cfd["cm19"])

    print("444444 old_lr_uwwwwwwww = ",old_lr_uw)
    print("444444 new_lr_uwwwwwwww = ",new_lr_uw)

def caculateAfterMultipleConditions_0():
    # mp3,200,DVD,200 add 5 and 10 respectively
    # center,200 and GPS 700 block

    if True:

        # distribution data
        cfd = {}
        cfd["cm19"] = 0.23726374699999997

        # cover data
        old_fee_uw = {}
        sales = {}
        fee_uw = {}
        new_fee_uw = {}

        sales["all_21"] = 7712
        sales["rate_period_36"] = {}
        sales["rate_period_36"]["sm1"] = 4086

        sales["mp3_25"] = 805
        sales["mp3_200"] = {}
        sales["mp3_200"]["sm11"] = 38 
        sales["dvd_200"] = {}
        sales["dvd_200"]["sm11"] = 129

        sales["dvd_22"] = 65
        sales["dvd_25"] = 42

        sales["gps_21"] = 405
        sales["center_22"] = 664

        fee_uw["mp3_25"] = 8460

        fee_uw["center_200"] = {}
        fee_uw["center_200"]["sm11"] = 1323
        fee_uw["gps_700"] = {}
        fee_uw["gps_700"]["sm11"] = 94.5

        fee_uw["all_1"] = 24467

        fee_uw["all_22"] = 51791.25
        fee_uw["all_25"] = 89429.5
        fee_uw["rate_period_36"] = {}
        fee_uw["rate_period_36"]["sm1"] = 24467

        old_fee_uw["sm11"] = 38327.25
        # print("new_fee_uw_sm11",new_fee_uw["sm11"])

        #claim data
        claim_cost = {}
        claim_cost["center_200"] = {}
        claim_cost["center_200"]["sm11"] = {}
        claim_cost["center_200"]["sm11"]["cm19"] = 202.62
        claim_cost["gps_700"] = {}
        claim_cost["gps_700"]["sm11"] = {}
        claim_cost["gps_700"]["sm11"]["cm19"] = 0.0

        old_claim_cost = {}
        old_claim_cost["sm11"] = {}
        old_claim_cost["sm11"]["cm19"] = 7500.0
        new_claim_cost = {}
        new_claim_cost["sm11"] = old_claim_cost["sm11"]["cm19"]-claim_cost["center_200"]["sm11"]["cm19"] - claim_cost["gps_700"]["sm11"]["cm19"]
        # print("new_claim_cost_sm11 = ",new_claim_cost["sm11"])

    # mp3,200,DVD,200 add 5 and 10 respectively
    # center,200 and GPS 700 block
    new_fee_uw["sm11"] = old_fee_uw["sm11"]+sales["mp3_200"]["sm11"]*5.0+sales["dvd_200"]["sm11"]*10.0 - fee_uw["center_200"]["sm11"] - fee_uw["gps_700"]["sm11"]
    old_lr_uw = old_claim_cost["sm11"]["cm19"]/(old_fee_uw["sm11"]*cfd["cm19"])
    new_lr_uw = new_claim_cost["sm11"]/(new_fee_uw["sm11"]*cfd["cm19"])

    print("old_lr_uwwwwwwww = ",old_lr_uw)
    print("new_lr_uwwwwwwww = ",new_lr_uw)

def caculateAfterMultipleConditions_1():
    # mp3 all price,DVD all price add 5 and 10 respectively
    # center,200 and GPS 700 block

    if True:

        # distribution data
        cfd = {}
        cfd["cm19"] = 0.23726374699999997

        # cover data
        old_fee_uw = {}
        sales = {}
        fee_uw = {}
        new_fee_uw = {}

        # sales["all_21"] = 7712
        sales["rate_period_36"] = {}
        sales["rate_period_36"]["sm1"] = 4086

        sales["mp3"] = {}
        sales["mp3"]["sm11"] = 70
        sales["dvd"] = {}
        sales["dvd"]["sm11"] = 457

        # sales["dvd_22"] = 65
        # sales["dvd_25"] = 42

        # sales["gps_21"] = 405
        # sales["center_22"] = 664

        # fee_uw["mp3_25"] = 8460

        fee_uw["center"] = {}
        fee_uw["center"]["sm11"] = 2403.75
        fee_uw["gps"] = {}
        fee_uw["gps"]["sm11"] = 273.75

        # fee_uw["all_1"] = 24467

        # fee_uw["all_22"] = 51791.25
        # fee_uw["all_25"] = 89429.5
        fee_uw["rate_period_36"] = {}
        fee_uw["rate_period_36"]["sm1"] = 24467

        old_fee_uw["sm11"] = 38327.25
        # print("new_fee_uw_sm11",new_fee_uw["sm11"])

        #claim data
        claim_cost = {}
        claim_cost["center"] = {}
        claim_cost["center"]["sm11"] = {}
        claim_cost["center"]["sm11"]["cm19"] = 202.62
        claim_cost["gps"] = {}
        claim_cost["gps"]["sm11"] = {}
        claim_cost["gps"]["sm11"]["cm19"] = 0

        old_claim_cost = {}
        old_claim_cost["sm11"] = {}
        old_claim_cost["sm11"]["cm19"] = 7500.0
        new_claim_cost = {}
        new_claim_cost["sm11"] = old_claim_cost["sm11"]["cm19"]-claim_cost["center"]["sm11"]["cm19"] - claim_cost["gps"]["sm11"]["cm19"]
        # print("new_claim_cost_sm11 = ",new_claim_cost["sm11"])

    # mp3,200,DVD,200 add 5 and 10 respectively
    # center,200 and GPS 700 block
    new_fee_uw["sm11"] = old_fee_uw["sm11"]+sales["mp3"]["sm11"]*5.0+sales["dvd"]["sm11"]*10.0 - fee_uw["center"]["sm11"] - fee_uw["gps"]["sm11"]
    old_lr_uw = old_claim_cost["sm11"]["cm19"]/(old_fee_uw["sm11"]*cfd["cm19"])
    new_lr_uw = new_claim_cost["sm11"]/(new_fee_uw["sm11"]*cfd["cm19"])

    print("old_lr_uwwwwwwww = ",old_lr_uw)
    print("new_lr_uwwwwwwww = ",new_lr_uw)

# last_fee = 139.25/(1.0+((100.0*4086.0)/24467.0))

#step 2:
# add dvd 100
# fee_uw["all_22"] += 100*sales["dvd_22"]   #58291.25     ok    
# fee_uw["all_25"] += 100*sales["dvd_25"]   #174129.5     ok

# sales["mp3"] = 805

# add mp3

# add dvd
# fee_uw["all_25"] += 100*sales["mp3_25"]


# add mp3 and dvd, block centre and GPS


# res = new_lr_uw["sm1"]["cm1"]

# res = fee_uw["all_22"]
# res = new_lr_uw["cm2"]
# print(last_fee)



def generateLR_UWList(n):
    # centre all, add 5
    lr_uw_list = []
    curr_lr = []
    cost = []
    for index in range (n):
        lr_list = []
        cost_list = []
        curr_lr.append(lr_list)
        cost.append(cost_list)
        
    # this data is from the experiment page, after event: READ_TENSOR_DEMO_FULFILLED 
    # in payload.data.claims
    curr_lr[0] = [76.6,71.07,86.12,84.01,73.76,77.43]
    curr_lr[1] = [125.61,82.88,70.28,64.05,57.67,49.29]
    curr_lr[2] = [99.37,85.37,62.99,55.87,58.55,61.69]
    curr_lr[3] = [62.6,76.83,77.1,80.26,70.12,60.89]
    curr_lr[4] = [30.46,34.18,59.47,51.47,45.01,44.96]
    curr_lr[5] = [37.21,39.07,50.28,47.58,41.55,39.33]
    #this data is from the tensor_demo page, change the selector to cumm_claim_cost
    # after event:READ_TENSOR_DEMO_FULFILLED
    # in payload.data.claims    
    cost[0] = [565.0,1458.0,2161.0,2776.0,2907.0]
    cost[1] = [1085.0,1479.0,1947.0,2410.0,2768.0]
    cost[2] = [1145.0,2068.0,2256.0,2605.0,4120.0]
    cost[3] = [852.0,2039.0,3037.0,3882.0,4199.0]
    cost[4] = [701.0,1023.0,2532.0,2945.0,3184.0]

    for num in range (n):
        print(" ============================================ ")
        def caculateLR_UW(n):
            lr_uw = 0.0
            total_cost = 0.0
            total_cost_fromLR = 0.0
            curr_cost = []
            # cost=[9055.32,12107.15,10129.89]
            fee=[19900.75,24852.25,30797.5,30635.0,35741.0,49591.5]
            cfd = [0.031849774,0.07179612199999999,0.11147420899999999,0.15142055699999998,0.19314717599999998,0.23726374699999997]
            total_fee = 0.0
            for i in range (n+1):
                arr = []
                curr_cost.append(arr)
                curr_cost[i] = fee[i]*cfd[n-i]*curr_lr[i][n-i]/100  
                print("i = ",i,"curr_cost[i]=",curr_cost[i],"fee[i]=",fee[i],"cfd[i]=",cfd[i])
                
                # total_cost+=cost[i][n-i]                
                total_cost_fromLR+=curr_cost[i]
                # cost[i] = fee[i]*cfd[n-i]*lr[n-i]
                total_fee += fee[i]*cfd[n-i]
            
            print("total_cost = ",total_cost,"total_fee=",total_fee)
            if total_fee == 0.0:
                print("n = ",n)
            else:
                lr_uw = total_cost/total_fee
                lr_uw_LR = total_cost_fromLR/total_fee
            return lr_uw_LR
        
        lr_uw_list.append(0)
        lr_uw_list[num] = caculateLR_UW(num)    
    
    print("lr_uw_list = ",lr_uw_list)
    return lr_uw_list

caculateAfterSingleConditions()
caculateAfterSingleConditions_1()

caculateAfterMultipleConditions_0()
caculateAfterMultipleConditions_1()

res = generateLR_UWList(6)
