
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '0777CA0AB9F545CEE79B264C2596F58C'
    
_lr_action_items = {'LPAREN':([0,4,8,9,10,15,16,17,18,19,20,23,27,34,35,38,41,],[8,19,8,-5,-6,8,8,8,8,8,8,19,19,41,8,8,8,]),'OPERATOR':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,25,26,27,29,30,31,33,34,35,36,37,38,39,40,41,42,44,46,],[9,17,-10,-11,-12,-13,9,-5,-6,-15,-16,-17,-18,9,9,9,9,9,9,17,-10,-22,17,-10,-20,-27,17,17,-14,9,9,-21,9,-19,-7,9,17,17,-8,]),'NAME':([0,8,15,16,17,18,19,20,35,36,38,41,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'NUMBER':([0,8,15,16,17,18,19,20,35,38,41,],[11,11,11,11,11,11,11,11,11,11,11,]),'LBRACKET':([0,8,15,16,17,18,19,20,35,38,41,],[15,15,15,15,15,15,15,15,15,15,15,]),'LBRACE':([0,8,15,16,17,18,19,20,35,38,41,],[16,16,16,16,16,16,16,16,16,16,16,]),'$end':([1,2,3,4,5,6,7,9,10,11,12,13,14,25,27,29,30,31,33,34,37,39,40,42,46,],[0,-1,-2,-10,-11,-12,-13,-5,-6,-15,-16,-17,-18,-22,-10,-20,-27,-9,-23,-14,-21,-19,-7,-24,-8,]),'COLON':([4,9,10,],[18,-5,-6,]),'MAPSTO':([4,9,10,23,27,],[20,-5,-6,20,20,]),'RPAREN':([5,6,7,9,10,11,12,13,14,21,23,25,26,27,29,30,32,33,34,37,39,40,42,44,45,46,],[-11,-12,-13,-5,-6,-15,-16,-17,-18,34,-10,-22,-3,-10,-20,-27,40,-23,-14,-21,-19,-7,-24,-4,46,-8,]),'RBRACKET':([5,6,7,9,10,11,12,13,14,15,24,25,26,27,29,30,33,34,37,39,40,42,44,46,],[-11,-12,-13,-5,-6,-15,-16,-17,-18,25,37,-22,-3,-10,-20,-27,-23,-14,-21,-19,-7,-24,-4,-8,]),'COMMA':([5,6,7,9,10,11,12,13,14,22,23,24,25,26,27,28,29,30,32,33,34,37,39,40,42,43,44,45,46,],[-11,-12,-13,-5,-6,-15,-16,-17,-18,36,-25,38,-22,-3,-10,38,-20,-27,38,-23,-14,-21,-19,-7,-24,-26,-4,38,-8,]),'RBRACE':([5,6,7,9,10,11,12,13,14,16,25,26,27,28,29,30,33,34,37,39,40,42,44,46,],[-11,-12,-13,-5,-6,-15,-16,-17,-18,29,-22,-3,-10,39,-20,-27,-23,-14,-21,-19,-7,-24,-4,-8,]),'RPAREN_MAPSTO':([9,10,22,23,43,],[-5,-6,35,-25,-26,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'assign':([0,],[2,]),'expression':([0,8,15,16,17,18,19,20,35,38,41,],[3,21,26,26,30,31,26,33,42,44,26,]),'name':([0,8,15,16,17,18,19,20,35,36,38,41,],[4,23,27,27,27,27,27,27,27,43,27,27,]),'operator_invocation':([0,8,15,16,17,18,19,20,35,38,41,],[5,5,5,5,5,5,5,5,5,5,5,]),'call':([0,8,15,16,17,18,19,20,35,38,41,],[6,6,6,6,6,6,6,6,6,6,6,]),'literal':([0,8,15,16,17,18,19,20,35,38,41,],[7,7,7,7,7,7,7,7,7,7,7,]),'list':([0,8,15,16,17,18,19,20,35,38,41,],[12,12,12,12,12,12,12,12,12,12,12,]),'set':([0,8,15,16,17,18,19,20,35,38,41,],[13,13,13,13,13,13,13,13,13,13,13,]),'lambda':([0,8,15,16,17,18,19,20,35,38,41,],[14,14,14,14,14,14,14,14,14,14,14,]),'capture_list':([8,],[22,]),'arglist':([15,16,19,41,],[24,28,32,45,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> assign','statement',1,'p_statment','myth_parse.py',80),
  ('statement -> expression','statement',1,'p_statment','myth_parse.py',81),
  ('arglist -> expression','arglist',1,'p_arglist','myth_parse.py',92),
  ('arglist -> arglist COMMA expression','arglist',3,'p_arglist','myth_parse.py',93),
  ('name -> OPERATOR','name',1,'p_name','myth_parse.py',102),
  ('name -> NAME','name',1,'p_name','myth_parse.py',103),
  ('call -> name LPAREN arglist RPAREN','call',4,'p_call_name','myth_parse.py',109),
  ('call -> LPAREN expression RPAREN LPAREN arglist RPAREN','call',6,'p_call_expression','myth_parse.py',115),
  ('assign -> name COLON expression','assign',3,'p_assign','myth_parse.py',121),
  ('expression -> name','expression',1,'p_expression_name','myth_parse.py',127),
  ('expression -> operator_invocation','expression',1,'p_expression','myth_parse.py',133),
  ('expression -> call','expression',1,'p_expression','myth_parse.py',134),
  ('expression -> literal','expression',1,'p_expression','myth_parse.py',135),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','myth_parse.py',136),
  ('literal -> NUMBER','literal',1,'p_literal_number','myth_parse.py',145),
  ('literal -> list','literal',1,'p_literal_number','myth_parse.py',146),
  ('literal -> set','literal',1,'p_literal_number','myth_parse.py',147),
  ('literal -> lambda','literal',1,'p_literal_number','myth_parse.py',148),
  ('set -> LBRACE arglist RBRACE','set',3,'p_set','myth_parse.py',154),
  ('set -> LBRACE RBRACE','set',2,'p_set','myth_parse.py',155),
  ('list -> LBRACKET arglist RBRACKET','list',3,'p_list','myth_parse.py',164),
  ('list -> LBRACKET RBRACKET','list',2,'p_list','myth_parse.py',165),
  ('lambda -> name MAPSTO expression','lambda',3,'p_lambda','myth_parse.py',174),
  ('lambda -> LPAREN capture_list RPAREN_MAPSTO expression','lambda',4,'p_lambda','myth_parse.py',175),
  ('capture_list -> name','capture_list',1,'p_capture_list','myth_parse.py',184),
  ('capture_list -> capture_list COMMA name','capture_list',3,'p_capture_list','myth_parse.py',185),
  ('operator_invocation -> expression OPERATOR expression','operator_invocation',3,'p_operator_invocation','myth_parse.py',194),
]
