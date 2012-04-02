# Created by Christopher Bess

class FormulaItem(object):
    """Represents a formula for the calculator
    This formula item has required fields, based on the desired calculation. Once
    the calculation is complete, the applicable fields will be populated with
    the appropriate result values.
    """
    def __init__(self):
        super(FormulaItem, self).__init__()
        pass
        
    def validate(self):
        """Validates the current formula item for the expected calculation
        @return tuple (success, message) True, if the validation passes and the forumla can be used in a
        calculation, False otherwise
        """
        raise NotImplementedError

    def calculate(self):
        """Calculates the formula
        """
        if not self.validate():
            return None
        raise NotImplementedError


class BandwidthFormulaItem(FormulaItem):
    """Represents the formula to calculate traffic bandwidth
    """
    # the number of users per day
    users_per_day = 0
    # resources accessed per user
    resources_per_user = 0
    # the overall size of each resource accessed by a user
    resource_size = 0

    def validate(self):
        if not self.users_per_day:
            return False, 'no users per day'
        if not self.resource_size:
            return False, 'no resource size'
        if not self.resources_per_user:
            return False, 'no resources per user'
        return True, None


class Calculator:
    """Represents the calculator
    """
    def calculate(self, forumla):
        pass