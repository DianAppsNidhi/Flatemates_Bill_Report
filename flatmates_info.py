

class FlatMates:
    """this class object  is created for flatmates information
    """

    def __init__(self, name , stay_duration):
        self.name = name
        self.stay_duration = stay_duration

    def pays(self, flatmate2, bill):
        """_summary_

        Args:
            flatmate2 (_type_): enter flatmate name
            bill (_type_): _description_

        Returns:
            _type_: _description_
        """



        return self.stay_duration/(self.stay_duration + flatmate2.stay_duration)*bill.amount



