import uuid
from exception import NameValueError
class MedicalRecord:
    def __init__(self) -> None:
        self.__patient_name=None
        self.__patient_age=None
        self.__patient_id=uuid.uuid1()


    @property
    def patient_name(self):
        return self.__patient_name
    
    @patient_name.setter
    def patient_name(self,value):
        if not isinstance(value,str):
            raise NameValueError
        else:
            self.__patient_name=value
    # @patient_name.getter
    # def patient_name(self):
    #     return self.patient_name

    @property
    def patient_age(self):
        return self.__patient_age
    @patient_age.setter
    def patient_age(self,value):
        if not isinstance(value,str):
            raise NameValueError
        else:
            self.__patient_age=value
    # @patient_age.getter
    # def patient_age(self):
    #     return self.__patient_age
    
    @property
    def patient_id(self):
        return self.__patient_id
    # @patient_id.setter
    # def patient_age(self,value):
    #     if not isinstance(value,str):
    #         raise NameValueError
    #     else:
    #         self.patient_age=value
    # @patient_age.getter
    # def patient_name(self):
    #     return self.patient_age

    def dispaly(self):
        print(f"patient_name: {self.patient_name}")
        print(f'patient_age: {self.patient_age}')
        print(f'patient_id: {self.patient_id}')

a=MedicalRecord()
a.patient_name='hassan'
a.patient_age='26'
a.dispaly()

