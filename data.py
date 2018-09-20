from collections import OrderedDict

class timetable(OrderedDict):
    def __init__(self, name, fixedslots = False):
        self.name = name
        self.roomno = ''
        self.dept = ''
        self.final = OrderedDict()
        for day in 'monday', 'tuesday', 'wednesday', 'thursday', 'friday':
            self[day] = OrderedDict({1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''})
            self.final[day] = OrderedDict({1: fixedslots, 2: fixedslots, 3: fixedslots, 4: fixedslots, 5: fixedslots, 6: fixedslots, 7: fixedslots, 8: fixedslots})
        self['saturday'] = {1: '', 2: '', 3: '', 4: ''}
        self.final['saturday'] = OrderedDict({1: fixedslots, 2: fixedslots, 3: fixedslots, 4: fixedslots})
        self.workload = 0

    def calc_workload(self):
      workload = 0
      for day in 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday':
        for timeslot in self[day]:
          if self.final[day][timeslot] == True:
            workload += 1
      self.workload += workload
      self.workload /= 44

faculty = { 'Dr. Anitha T N': timetable('Dr. Anitha T N'),
    'Dr. Bharathi M': timetable('Dr. Bharathi M'),
    'Mr. Srinivasa Murthy H': timetable('Mr. Srinivasa Murthy H'),
    'Mr. Pampana': timetable('Mr. Pampana'),
    'Mr. Vijay GR': timetable('Mr. Vijay GR'),
    'Dr. Murthy SVN': timetable('Dr. Murthy SVN'),
    'Mr. Manjunath M': timetable('Mr. Manjunath M'),
    'Mr. M Seshaiah': timetable('Mr. M Seshaiah'),
    'Mr. Diwakar KM': timetable('Mr. Diwakar KM'),
    'Mr. Harshavardhan': timetable('Mr. Harshavardhan'),
    'Mr. Girish BG': timetable('Mr. Girish BG'),
    'Mr. Srihari MR': timetable('Mr. Srihari MR'),
    'Mr. Ajay N': timetable('Mr. Ajay N'),
    'Mr. Jagadish N': timetable('Mr. Jagadish N'),
    'Mr. Srinath GM': timetable('Mr. Srinath GM'),
    'Mr. Pradeep Kumar': timetable('Mr. Pradeep Kumar'),
    'Mrs. Archana N': timetable('Mrs. Archana N'),
    'Mr. Sashikanth TS': timetable('Mr. Sashikanth TS'),
    'Mr. Venkatesh KM': timetable('Mr. Venkatesh KM'),
    'Mr. Ajay HC': timetable('Mr. Ajay HC'),
    'Mrs. Rashmi KM': timetable('Mrs. Rashmi KM'),
    'Mr. Apoorva S': timetable('Mr. Apoorva S'),
    'Mrs. Vinutha K': timetable('Mrs. Vinutha K'),
    'Mr. Vikas Reddy S': timetable('Mr. Vikas Reddy S'),
    'Dr. Mohammed Javed': timetable('Dr. Mohammed Javed'),
    'Mr. Chandra Naik': timetable('Mr. Chandra Naik'),
    'Mrs. Anisha P Rodrigues': timetable('Mrs. Anisha P Rodrigues'),
    'Mr. K R Raghunandan': timetable('Mr. K R Raghunandan'),
    'Mrs. Minu P Abraham': timetable('Mrs. Minu P Abraham'),
    'Mr. Sampath Kini': timetable('Mr. Sampath Kini'),
    'Mr. Mahesh Kini': timetable('Mr. Mahesh Kini'),
    'Mr. H R Manjunath Prasad': timetable('Mr. H R Manjunath Prasad'),
    'Mr. Naveen Chandavarkar': timetable('Mr. Naveen Chandavarkar'),
    'Mr. Pawan Hegde': timetable('Mr. Pawan Hegde'),
    'Mrs. Keerthana B C': timetable('Mrs. Keerthana B C'),
    'Mr. Sunil Kumar Aithal': timetable('Mr. Sunil Kumar Aithal'),
    'Mr. Shashank Shetty': timetable('Mr. Shashank Shetty'),
    'Mr. Puneeth R P': timetable('Mr. Puneeth R P'),
    'Mrs. Shilpa M K': timetable('Mrs. Shilpa M K'),
    "Mrs. Divya Jennifer D'Souza": timetable("Mrs. Divya Jennifer D'Souza"),
    'Mrs. Rajalaxmi Hegde': timetable('Mrs. Rajalaxmi Hegde'),
    'Mr. Sandeep Hegde': timetable('Mr. Sandeep Hegde'),
    'Ms. Swathi Pai M': timetable('Ms. Swathi Pai M'),
    'Ms. Ankitha A Nayak': timetable('Ms. Ankitha A Nayak'),
    'Ms. Rajashree': timetable('Ms. Rajashree'),

    # maths
    'Ms. Smitha G V': timetable('Ms. Smitha G V', fixedslots = True),
    'Dr. Shashirekha B Rai': timetable('Dr. Shashirekha B Rai', fixedslots = True),
    'Ms. Anitha D Bayar': timetable('Ms. Anitha D Bayar', fixedslots = True),
    "Ms. Apoorva D'Souza": timetable("Ms. Apoorva D'Souza", fixedslots = True),
    #humanities
    'Mr. Rama Krishna': timetable('Mr. Rama Krishna'),
    'Humanities': timetable('', fixedslots = True),

    '': timetable('')
}


subjects = {'4A': (
                   ('Probability Theory and Numberical Methods', 0, 'Ms. Smitha G V', 'Maths'),
                   ('Design & Analysis of Algorithms', 5, 'Dr. Anitha T N', 'DAA'),
                   ('Finite Automata & Formal languages', 5, 'Dr. Bharathi M', 'FAFL'),
                   ('Data Communications', 5, 'Mr. Srinivasa Murthy H', 'DC'),
                   ('Computer Organization & Architecture', 5, 'Mr. Pampana', 'CO'),
                   ('Unix Programming', 5, 'Mr. Vijay GR', 'Unix'),
                   ('', 0, ('Dr. Anitha T N', 'Mr. Vijay GR'), 'DAA/Unix Lab'),
                   ('', 0, 'Humanities', 'ESC')
                   ),
             '4B': (
                   ('Probability Theory and Numberical Methods', 0, 'Dr. Shashirekha B Rai', 'Maths'),
                   ('Design & Analysis of Algorithms', 4, 'Dr. Murthy SVN', 'DAA'),
                   ('Finite Automata & Formal languages', 4, 'Mr. Srinivasa Murthy H', 'FAFL'),
                   ('Data Communications', 4, 'Mr. Manjunath M', 'DC'),
                   ('Computer Organization & Architecture', 4, 'Mr. M Seshaiah', 'CO'),
                   ('Unix Programming', 4, 'Mr. Diwakar KM', 'Unix'),
                   ('', 0, ('Mr. Diwakar KM', 'Dr. Murthy SVN'), 'DAA/Unix Lab'),
                   ('', 0, 'Humanities', 'ESC')
                   ),

             '6A': (
                    ('', 5, 'Mrs. Shilpa M K', 'CG'),
                    ('', 5, 'Mrs. Vinutha K', 'CN'),
                    ('', 5, 'Mr. Sandeep Hegde', 'JIT'),
                    ('', 5, 'Mr. Mahesh Kini', 'ST'),
                    ('', 0, 'Dr. Murthy SVN', 'CCIM'),
                    ('', 0, 'Dr. Bharathi M', 'MC'),
                    ('', 1, 'Mrs. Archana N', 'ESD'),
                    ('', 0, ('Mrs. Shilpa M K', 'Mrs. Vinutha K'), 'CG/CN Lab'),
                    ('', 0, ('Mr. Sandeep Hegde',), 'JIT Lab')
                    ),
            '6B': (
                    ('', 4, 'Mr. Vijay GR', 'CG'),
                    ('', 4, 'Mr. Chandra Naik', 'CN'),
                    ('', 4, 'Mr. Pradeep Kumar', 'JIT'),
                    ('', 3, 'Mrs. Rajalaxmi Hegde', 'ST'),
                    ('', 0, 'Mrs. Minu P Abraham', 'CCIM'),
                    ('', 0, 'Mr. Manjunath M', 'MC'),
                    ('', 1, 'Mr. Sunil Kumar Aithal', 'ESD'),
                    ('', 0, ('Mr. Vijay GR', 'Mr. Chandra Naik'), 'CG/CN Lab'),
                    ('', 0, ('Mr. Pradeep Kumar',), 'JIT Lab')
                    ),


             '8A': (
                     ('', 5, 'Mr. Rama Krishna', 'EM'),
                    ('', 5, 'Dr. Mohammed Javed', 'BA'),
                     ('', 5, 'Mr. Naveen Chandavarkar', 'BAI'),
                     ('', 5, '', 'OE'),
                     ),
             '8B': (
                     ('', 5, 'Mr. Rama Krishna', 'EM'),
                     ('', 5, 'Mrs. Anisha P Rodrigues', 'BA'),
                     ('', 5, 'Mr. Sunil Kumar Aithal', 'BAI'),
                     ('', 5, '', 'OE'),
                     ),
            # '8C': (
            #         ('', 3, 'Mr. Rama Krishna', 'EM'),
            #         ('', 3, 'Mrs. Pallavi K N', 'IOT'),
            #         ('', 3, "Mrs. Divya Jennifer D'Souza", 'SIC'),
            #         ('', 3, '', 'OE'),
            #         ),
            # '8D': (
            #         ('', 3, 'Mr. Rama Krishna', 'EM'),
            #         ('', 3, 'Mrs. Asmitha Poojari', 'IOT'),
            #         ('', 3, 'Mr. Vijay Murari T', 'SIC'),
            #         ('', 3, '', 'OE'),
            #         )
}
