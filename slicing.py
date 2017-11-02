l = [i ** 2 for i in range(1, 11)]
# print the selected items

print l[2:9:2]


""" [start:end:stride]
 start describes where the slice starts (inclusive), 
end is where it ends (exclusive), and stride describes the 
space between items in the sliced list."""