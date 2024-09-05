import re
from dataclasses import dataclass, field
from typing import List, Dict, Any

class Invalidname(Exception):
    pass

class InvalidAge(Exception):
    pass

class InvalidTimeType(Exception):
    pass

class InvalidSalary(Exception):
    pass

class InvalidIndex(Exception):
    pass

class InvalidSkillList(Exception):
    pass


@dataclass
class Job:
    job_name: str = ""
    job_min_age: int = 0
    job_max_age: int = 0
    job_time_type: str = ""
    job_salary: str = ""
    skills_job: List[str] = field(default_factory=list)
    objects = {}
    _id: int = 1

    def __post_init__(self):
        self.validate()
        self._id = Job._id
        Job.objects[self._id] = self
        Job._id += 1

    def validate(self):
        if not re.match(r'^[A-Za-z]{1,10}$', self.job_name):
            raise Invalidname
        if not (0 <= self.job_min_age <= 200) or self.job_min_age > self.job_max_age:
            raise InvalidAge
        if not (0 <= self.job_max_age <= 200):
            raise InvalidAge
        if self.job_time_type not in ['FULLTIME', 'PARTTIME', 'PROJECT']:
            raise InvalidTimeType
        if not re.match(r'^(?!0$)([1-9]\d{0,8}|0)(000)$', str(self.job_salary)):
            raise InvalidSalary

    def __str__(self) -> str:
        return f'job id is <{self._id}>'

    @classmethod
    def add_job_skill(cls, job_id, skill):
        if job_id not in cls.objects:
            return "invalid index"
        elif skill not in d:
            return "invalid skill"
        elif skill in cls.objects[job_id].skills_job:
            return "repeated skill"
        else:
            cls.objects[job_id].skills_job.append(skill)
            return "skill added"

@dataclass
class User:
    user_name: str = ""
    user_age: int = 0
    user_time_type: str = ""
    user_salary: str = ""
    _id: int = 1
    skills_user: List[str] = field(default_factory=list)
    objects= {}

    def __post_init__(self):
        self.validate()
        self._id = User._id
        User.objects[self._id] = self
        User._id += 1

    def validate(self):
        if not re.match(r'^[A-Za-z]{1,10}$', self.user_name):
            raise Invalidname
        if not (0 <= self.user_age <= 200):
            raise InvalidAge
        if self.user_time_type not in ['FULLTIME', 'PARTTIME', 'PROJECT']:
            raise InvalidTimeType
        if not re.match(r'^(?!0$)([1-9]\d{0,8}|0)(000)$', str(self.user_salary)):
            raise InvalidSalary

    def __str__(self) -> str:
        return f'user id is <{self._id}>'

    @classmethod
    def add_user_skill(cls, user_id, skill):
        if user_id not in cls.objects:
            return "invalid index"
        elif skill not in d:
            return "invalid skill"
        elif skill in cls.objects[user_id].skills_user:
            return "repeated skill"
        else:
            cls.objects[user_id].skills_user.append(skill)
            return "skill added"

@dataclass
class View:
    user_id: int
    job_id: int

    def __str__(self) -> str:
        if self.user_id not in User.objects or self.job_id not in Job.objects:
            raise InvalidIndex
        return "tracked"

def Job_Status(job_id):
    job = Job.objects.get(job_id)
    if job is None:
        raise InvalidIndex
    
    job_name = job.job_name
    total_views = sum(1 for view in View.objects if view.job_id == job_id)
    
    skill_views = {skill: sum(1 for view in View.objects if view.job_id == job_id and skill in User.objects[view.user_id].skills_user) for skill in job.skills_job}

    skill_views = sorted(skill_views.items(), key=lambda x: (-x[1], x[0]))

    skill_output = ', '.join(f"{skill[0]} - {skill[1]}" for skill in skill_views)
    return f"{job_name} - {total_views} - {skill_output}"

class Skills_list1:
    def __init__(self, number, *args) -> None:
        self.number = number
        self.list_1 = list(args)
        if len(self.list_1) != self.number:
            raise InvalidSkillList

    def __iter__(self):
        return self

    def __next__(self):
        if self.list_1:
            return self.list_1.pop()
        else:
            raise StopIteration

s = Skills_list1(3, 'python', 'java', 'hassan')
d = [next(s) for i in range(s.number)]

try:
    j = Job('Developer', 22, 35, 'FULLTIME', 500000)
    o = User('hassan', 26, 'FULLTIME', 500000)
    r = User('hosein', 33, 'FULLTIME', 502000)

    print(Job.add_job_skill(1, 'python'))
    print(Job.add_job_skill(1, 'ccc'))
    print(Job.add_job_skill(2, 'python'))

    print(User.add_user_skill(1, 'python'))
    print(User.add_user_skill(1, 'ccc'))
    print(User.add_user_skill(2, 'python'))

    print(View(1, 1))

    print(Job.objects)
    print(User.objects)

    print(Job_Status(1))

except Exception as e:
    print(e)
