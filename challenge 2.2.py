def averageRuns(runs, matches, notout):
 
    out = matches - notout;
 
    if (out == 0):
        return -1;
 
    avg = runs // out;
 
    return avg;
 
runs = 12000;
matches = 600;
notout = 90;
 
avg = averageRuns(runs, matches, notout);
 
if (avg == -1):
    print("NA");
else:
    print(avg);
 