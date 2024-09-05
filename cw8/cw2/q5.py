class VariableScopeDemo:
    class_var = 0  

    def __init__(self, instance_var):
        self.instance_var = instance_var  

    def access_class_var(self):
        print(f"Accessing class-level variable: {self.class_var}")
        print(f"Accessing class-level variable: {VariableScopeDemo.class_var}")

    def modify_class_var(self):
        self.class_var += 1  
        print(f"Modified class-level variable: {self.class_var}")
        print(f"Modified class-level variable: {VariableScopeDemo.class_var}")

    def access_instance_var(self):
        print(f"Accessing instance-level variable: {self.instance_var}")

    def modify_instance_var(self):
        self.instance_var += 1  
        print(f"Modified instance-level variable: {self.instance_var}")

obj1 = VariableScopeDemo(10)
obj1.access_class_var()  
obj1.modify_class_var()  
obj1.access_instance_var()  
obj1.modify_instance_var()  

obj2 = VariableScopeDemo(20)
obj2.access_class_var()  
obj2.access_instance_var()  
