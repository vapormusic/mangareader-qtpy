### thank you koreader
def getmodel():
 import subprocess
 kindle_sn = subprocess.check_output('cat /proc/usid', shell=True)   

 ## NOTE: Attempt to sanely differentiate v1 from v2,
 ##      c.f., https://github.com/NiLuJe/FBInk/commit/8a1161734b3f5b4461247af461d26987f6f1632e
 kindle_sn_lead = kindle_sn[:1]

 ## NOTE: Update me when new devices come out :)
 ##       c.f., https://wiki.mobileread.com/wiki/Kindle_Serial_Numbers for identified variants
 ##       c.f., https://github.com/NiLuJe/KindleTool/blob/master/KindleTool/kindle_tool.h#L174 for all variants
 k2_set =  { "02", "03" }
 dx_set =  { "04", "05" }
 dxg_set =  { "09" }
 k3_set = { "08", "06", "0A" }
 k4_set =  { "0E", "23" }
 touch_set =  { "0F", "11", "10", "12" }
 pw_set =  { "24", "1B", "1D", "1F", "1C", "20" }
 pw2_set =  { "D4", "5A", "D5", "D6", "D7", "D8", "F2", "17",
                  "60", "F4", "F9", "62", "61", "5F" }
 kt2_set =  { "C6", "DD" }
 kv_set = { "13", "54", "2A", "4F", "52", "53" }
 pw3_set =  { "0G1", "0G2", "0G4", "0G5", "0G6", "0G7",
                  "0KB", "0KC", "0KD", "0KE", "0KF", "0KG", "0LK", "0LL" }
 koa_set = { "0GC", "0GD", "0GR", "0GS", "0GT", "0GU" }
 koa2_set =  { "0LM", "0LN", "0LP", "0LQ", "0P1", "0P2", "0P6",
                  "0P7", "0P8", "0S1", "0S2", "0S3", "0S4", "0S7", "0SA" }
 kt3_set =  { "0DU", "0K9", "0KA" }
 pw4_set =  { "0PP", "0T1", "0T2", "0T3", "0T4", "0T5", "0T6",
                  "0T7", "0TJ", "0TK", "0TL", "0TM", "0TN", "102", "103",
                  "16Q", "16R", "16S", "16T", "16U", "16V" }
 kt4_set =  { "10L", "0WF", "0WG", "0WH", "0WJ", "0VB" }
 koa3_set =  { "11L", "0WQ", "0WP", "0WN", "0WM", "0WL" }

 if kindle_sn_lead == "B" or kindle_sn_lead == "9" :
    kindle_devcode = kindle_sn[2:4]

    if kindle_devcode in k2set:
        return 'Kindle2'
    elif kindle_devcode in dx_set:
        return 'Kindle2'
    elif kindle_devcode in dxg_set :
        return 'KindleDXG'
    elif kindle_devcode in k3_set :
        return 'Kindle3'
    elif kindle_devcode in k4_set :
        return 'Kindle4'
    elif kindle_devcode in touch_set :
        return 'KindleTouch'
    elif kindle_devcode in pw_set :
        return 'KindlePaperWhite'
    elif kindle_devcode in pw2_set :
        return 'KindlePaperWhite2'
    elif kindle_devcode in kt2_set :
        return 'KindleBasic'
    elif kindle_devcode in kv_set :
        return 'KindleVoyage'
 else:
    kindle_devcode_v2 = kindle_sn[3:6]
    if kindle_devcode_v2 in pw3_set :
        return 'KindlePaperWhite3'
    elif kindle_devcode_v2 in koa_set :
        return 'KindleOasis'
    elif kindle_devcode_v2 in koa2_set :
        return 'KindleOasis2'
    elif kindle_devcode_v2 in kt3_set :
        return 'KindleBasic2'
    elif kindle_devcode_v2 in pw4_set :
        return 'KindlePaperWhite4'
    elif kindle_devcode_v2 in kt4_set :
        return 'KindleBasic3'
    elif kindle_devcode_v2 in koa3_set :
        return 'KindleOasis3'
