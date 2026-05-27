cbook={"john":1278563910,"jeny":2314354675,"zara":4325167263,"alora":2354172839,"zooya":2314357618}
print(cbook.get("jeny"))
cbook["zara"]=6789341678
print(cbook)
del cbook["john"]
print(cbook)
for name  in sorted(cbook.keys()):
 print(name)
