
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'dataCOMMA DEAD DOUBT EJECT MEMBER NONE NUMBER SEMI SKIP TRUST\n    data : participants SEMI meetings SEMI\n    \n    participants : members\n    \n    members : MEMBER\n            | members COMMA MEMBER\n    \n    meetings : meeting\n             | meetings SEMI meeting\n    \n    meeting : dead_info SEMI conclusion\n            | dead_info SEMI testimonies SEMI conclusion\n    \n    dead_info : DEAD NONE\n              | DEAD MEMBER\n    \n    testimonies : testimony\n                | testimonies SEMI testimony\n    \n    testimony : members TRUST members\n              | members DOUBT members\n    \n    conclusion : SKIP\n               | EJECT MEMBER\n    '
    
_lr_action_items = {'MEMBER':([0,6,10,13,20,23,25,26,],[4,11,15,4,24,4,4,4,]),'$end':([1,12,],[0,-1,]),'SEMI':([2,3,4,7,8,9,11,14,15,16,17,18,19,21,24,27,28,29,30,],[5,-2,-3,12,-5,13,-4,-9,-10,-6,-7,23,-15,-11,-16,-8,-12,-13,-14,]),'COMMA':([3,4,11,22,29,30,],[6,-3,-4,6,6,6,]),'TRUST':([4,11,22,],[-3,-4,25,]),'DOUBT':([4,11,22,],[-3,-4,26,]),'DEAD':([5,12,],[10,10,]),'NONE':([10,],[14,]),'SKIP':([13,23,],[19,19,]),'EJECT':([13,23,],[20,20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'data':([0,],[1,]),'participants':([0,],[2,]),'members':([0,13,23,25,26,],[3,22,22,29,30,]),'meetings':([5,],[7,]),'meeting':([5,12,],[8,16,]),'dead_info':([5,12,],[9,9,]),'conclusion':([13,23,],[17,27,]),'testimonies':([13,],[18,]),'testimony':([13,23,],[21,28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> data","S'",1,None,None,None),
  ('data -> participants SEMI meetings SEMI','data',4,'p_data','ah_yacc.py',24),
  ('participants -> members','participants',1,'p_participants','ah_yacc.py',34),
  ('members -> MEMBER','members',1,'p_members','ah_yacc.py',41),
  ('members -> members COMMA MEMBER','members',3,'p_members','ah_yacc.py',42),
  ('meetings -> meeting','meetings',1,'p_meetings','ah_yacc.py',52),
  ('meetings -> meetings SEMI meeting','meetings',3,'p_meetings','ah_yacc.py',53),
  ('meeting -> dead_info SEMI conclusion','meeting',3,'p_meeting','ah_yacc.py',63),
  ('meeting -> dead_info SEMI testimonies SEMI conclusion','meeting',5,'p_meeting','ah_yacc.py',64),
  ('dead_info -> DEAD NONE','dead_info',2,'p_dead_info','ah_yacc.py',74),
  ('dead_info -> DEAD MEMBER','dead_info',2,'p_dead_info','ah_yacc.py',75),
  ('testimonies -> testimony','testimonies',1,'p_testimonies','ah_yacc.py',85),
  ('testimonies -> testimonies SEMI testimony','testimonies',3,'p_testimonies','ah_yacc.py',86),
  ('testimony -> members TRUST members','testimony',3,'p_testimony','ah_yacc.py',96),
  ('testimony -> members DOUBT members','testimony',3,'p_testimony','ah_yacc.py',97),
  ('conclusion -> SKIP','conclusion',1,'p_conclusion','ah_yacc.py',104),
  ('conclusion -> EJECT MEMBER','conclusion',2,'p_conclusion','ah_yacc.py',105),
]
