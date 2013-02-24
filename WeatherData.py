# Part One - Weather Data (Refactored)

import Shared

result = Shared.ExecuteQuery("data/weather.dat", Shared.Query(0, 1, 2))

if result.DisplayName == "":
    print "No data found."
else:    
    print "Day {} has the smallest spread: {}".format(result.DisplayName, result.Difference)

Shared.ReadKey()
