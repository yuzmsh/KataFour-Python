import sys

class Query(object):
    """ This class represent a possible query """

    """ The position in the row of the display name """
    DisplayNamePosition = 0

    """ The position in the row of the max value """
    MaxValuePosition = 1

    """ The position in the row of the min value """
    MinValuePosition = 2

    def __init__(self, displayNamePosition=0, maxValuePosition=1, minValuePosition=2):
        """ Initialize a Query object """
        self.DisplayNamePosition = displayNamePosition
        self.MaxValuePosition = maxValuePosition
        self.MinValuePosition = minValuePosition

class Result(object):
    """ This class contains the result of a query """

    """ The name to display """
    DisplayName = ""

    """ The difference """
    Difference = sys.maxint
    

def ExecuteQuery(filepath, query):
    """ Execute a query on a specific file """

    result = Result()

    try:
        with open(filepath) as f:

            for line in f:
                items = line.split()

                try:
                    displayName = items[query.DisplayNamePosition]
                    max = int(items[query.MaxValuePosition].strip("*"))
                    min = int(items[query.MinValuePosition].strip("*"))
                    difference = max - min
                
                    if result.Difference > difference:
                        result.Difference = difference
                        result.DisplayName = displayName

                except:
                    continue
    except:
        print("Error: File not found.")

    return result

def ReadKey():
    """ Wait a user keypress """
    raw_input("\nPress Enter to continue...")
