# Part Two: Soccer League Table (Refactored)

import Shared

result = Shared.ExecuteQuery("data/football.dat", Shared.Query(1, 6, 8))

if result.DisplayName == "":
    print "No data found."
else:    
    print "Team {} has the smallest difference: {}".format(result.DisplayName, result.Difference)

Shared.ReadKey()