"""
A module devoted to exceptions and dynamic typing

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


# PART 1
def get_previous(filename):
    """
    Returns the number before the one stored in the file filename.

    By number before, we mean that the number is an int, and the result subtracts one
    from the int in the file.

    If the file does not contain an int, this function returns the contents of the file.

    If the file does not exist or cannot be opened, this function returns None.

    Parameter filename: The name of the file to open
    Precondition: filename is a string
    """
    # IMPLEMENT ME
    assert type(filename) == str, 'wrong parameter type'
    try:
        file=open(filename)
        content=file.read()
        int(content)
        number=int(content)
        return number-1
    except ValueError:
        return content
    except Exception:
        return None



# Part 2
# IMPLEMENT A NEW EXCEPTION CALLED LimitedUnavailableError HERE
class LimitedUnavailableError(RuntimeError):
    """ A custom error class """
    pass



class Limited(object):
    """
    A class that only allows you to make a limited number of objects.

    This class has a class attribute named AVAILABLE.  Every time an object is
    created, this attribute is decremented by one.  When each reaches 0, no more
    objects can be created.  Further constructor calls will raise a
    LimitedUnavailableError.

    INSTANCE ATTRIBUTE:
        x: A simple number [int or float]
    """

    # How many objects are left (starts at 4)
    AVAILABLE = 4

    def __init__(self,x):
        """
        Initializes a new Limited object

        The initializer checks to see if the object can be created (is AVAILABLE > 0).
        If so, it creates  a new object with attribute x and decrements AVAILABLE by 1.
        Otherwise, it raises a LimitedUnavailableError with x as the error.

        Parameter x: The object x value
        Precondition: x is an int or float
        """
        assert type(x) == int or type(x) == float
        if Limited.AVAILABLE > 0:
            Limited.AVAILABLE -= 1
            self.x = x
        else:
            raise LimitedUnavailableError(x)


# Part 3
class Point2(object):
    """
    A class to represent a point in 2D space

    Attribute x: the x-coordinate
    Invariant: x is a float

    Attribute y: the x-coordinate
    Invariant: y is a float
    """

    def __init__(self,x,y):
        """
        Initializes a new Point

        Parameter x: The x-coordinate
        Precondition: x is a float

        Parameter y: The y-coordinate
        Precondition: y is a float
        """
        assert type(x) in [int,float], '%s is not a number' % repr(x)
        assert type(y) in [int,float], '%s is not a number' % repr(y)
        self.x = x
        self.y = y

    def equals1(self,other):
        """
        Returns True is other is an instance of Point2 and equal to this one.

        Two points are equivalent if they share the same x and y values.

        Parameter other: The object to compare
        Precondition: other can be anything
        """
        # IMPLEMENT ME
        if isinstance(other, Point2) == False:
            return False
        if self.x != other.x :
            return False
        if self.y != other.y :
            return False
        return True

        pass

    def equals2(self,other):
        """
        Returns True is other is duck-equivalent to this Point2.

        An object is duck-equivalent to a Point2 object if (1) it has attributes x
        and y and (2) those values are the same as this object.

        Parameter other: The object to compare
        Precondition: other can be anything
        """
        # IMPLEMENT ME
        if not hasattr(other, 'x'):
            return False
        if not hasattr(other, 'y'):
            return False
        if getattr(self, 'x') != getattr(other, 'x'):
            return False
        if getattr(self, 'y') != getattr(other, 'y'):
            return False
        return True
