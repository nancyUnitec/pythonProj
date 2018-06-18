
sales = {}
fee_uw = {}
sales["all_21"] = 7712
sales["rate_period_36"] = {}
sales["rate_period_36"]["sm1"] = 4086

sales["mp3_25"] = 805

sales["dvd_22"] = 65
sales["dvd_25"] = 42

sales["gps_21"] = 405
sales["center_22"] = 664

fee_uw["mp3_25"] = 8460

fee_uw["all_1"] = 24467

fee_uw["all_22"] = 51791.25
fee_uw["all_25"] = 89429.5
fee_uw["rate_period_36"] = {}
fee_uw["rate_period_36"]["sm1"] = 24467


# step 1:
# add mp3_25 100
fee_uw["all_25"] += 100*sales["mp3_25"]   #169929.5   ok
# fee_uw["rate_period_36"]["sm1"] = fee_uw["rate_period_36"]["sm1"]+100.0*sales["rate_period_36"]["sm1"]
fee_uw["rate_period_36"]["sm1"] += 100.0*sales["rate_period_36"]["sm1"]

# new_lr_uw for each cm is: old_lr_uw/(1+(delta_fee*sales/old_fee_uw))
old_lr_uw = {}
old_lr_uw["sm25"] = {}
old_lr_uw["sm1"] = {}
old_lr_uw["rate_period_36"] = {}
old_lr_uw["sm25"]["cm2"] = 101.12
old_lr_uw["sm1"]["cm1"] = 139.25

old_lr_uw["rate_period_36"]["cm1"] = 139.25


new_lr_uw = {}
new_lr_uw["sm1"] = {}

# ??????????  68.6152032408  
# new_lr_uw["cm2"] = old_lr_uw["sm25"]["cm2"]/(1+(100*sales["mp3_25"]/fee_uw["all_25"]))
new_lr_uw["sm1"]["cm1"] = old_lr_uw["sm1"]["cm1"]/(1+(100*sales["rate_period_36"]["sm1"]/fee_uw["all_1"]))
# res = old_lr_uw["sm1"]["cm1"]/(1+(100*sales["rate_period_36"]["sm1"]/fee_uw["all_1"]))

#step 2:
# add dvd 100
# fee_uw["all_22"] += 100*sales["dvd_22"]   #58291.25     ok    
# fee_uw["all_25"] += 100*sales["dvd_25"]   #174129.5     ok

# sales["mp3"] = 805

# add mp3

# add dvd
# fee_uw["all_25"] += 100*sales["mp3_25"]


# add mp3 and dvd, block centre and GPS


res = new_lr_uw["sm1"]["cm1"]

# res = fee_uw["all_22"]
# res = new_lr_uw["cm2"]
print(res)



