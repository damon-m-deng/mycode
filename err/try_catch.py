#!/usr/bin/env python3

list1=["apple",33,{"potaYto":"poTaHto","tomatO":"toMAHto"}]

for item in list1:
    try:
        plusone = item+1
        print(plusone)
        import fakename # testing catch all
    except TypeError as t_err:
        print(t_err, "Incompatible types.")
    except Exception as err: # catch all
        print("Hmm.. something else went wrong")
    finally:
        print("All done.") # will always execute whether successful, or received any exceptions
