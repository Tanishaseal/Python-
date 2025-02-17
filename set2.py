class Student: 
    def __init__(self, name, college_name, roll_no): 
        try: 
            if not isinstance(name, str): 
                raise TypeError("Name must be a string.") 
            self.name = name 
            self.college_name = college_name 
            self.roll_no = roll_no
        except TypeError as e:
            