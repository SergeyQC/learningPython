gs = input()
a = gs.upper().count('g'.upper())
b = gs.upper().count('c'.upper())

print((a + b)/len(gs) * 100)
