
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'D432485DDA329815B73D09FC58ED7610'
    
_lr_action_items = {'LPAREN':([0,4,9,10,11,15,21,22,23,24,25,26,29,31,32,33,43,44,45,50,54,59,61,],[9,25,9,-5,-6,33,9,9,9,9,9,43,25,25,9,9,9,54,9,9,9,9,9,]),'OPERATOR':([0,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,27,29,30,31,32,33,35,36,38,39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,59,60,61,62,64,65,66,],[10,23,-12,-13,-14,-15,-16,10,10,-6,-33,-34,-35,-20,-21,-22,-23,-24,10,10,10,10,10,23,-12,23,-12,10,10,-28,23,-26,23,23,-7,10,-17,10,57,23,23,-27,10,-25,-8,23,10,23,10,23,10,-9,23,23,-10,]),'NAME':([0,9,10,21,22,23,24,25,32,33,43,45,46,50,54,59,61,],[11,11,11,11,11,11,11,11,11,11,11,11,58,11,11,11,11,]),'BAR':([0,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,30,31,32,33,35,38,39,41,43,44,45,47,49,50,51,52,54,55,59,61,62,64,65,66,],[15,-13,26,-15,-16,15,15,-6,-33,-34,-35,-20,-21,-22,-23,-24,15,15,15,15,15,-38,-12,15,15,-28,-26,-36,-7,15,-17,15,-29,-27,15,-25,-8,15,-30,15,15,-9,-18,-19,-10,]),'NUMBER':([0,9,10,21,22,23,24,25,32,33,43,45,50,54,59,61,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'STRING':([0,9,10,21,22,23,24,25,32,33,43,45,50,54,59,61,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'LBRACKET':([0,9,10,21,22,23,24,25,32,33,43,45,50,54,59,61,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'LBRACE':([0,9,10,21,22,23,24,25,32,33,43,45,50,54,59,61,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'$end':([1,2,3,4,5,6,7,8,10,11,12,13,14,16,17,18,19,20,23,30,31,35,38,39,40,41,44,47,49,51,52,55,62,64,65,66,],[0,-1,-2,-12,-13,-14,-15,-16,-5,-6,-33,-34,-35,-20,-21,-22,-23,-24,-37,-38,-12,-28,-26,-36,-11,-7,-17,-29,-27,-25,-8,-30,-9,-18,-19,-10,]),'COLON':([4,10,11,],[24,-5,-6,]),'RPAREN':([5,6,7,8,10,11,12,13,14,16,17,18,19,20,23,25,27,29,30,31,35,36,38,39,41,42,44,47,49,51,52,54,55,60,62,63,64,65,66,],[-13,-14,-15,-16,-5,-6,-33,-34,-35,-20,-21,-22,-23,-24,-37,41,44,-12,-38,-12,-28,-3,-26,-36,-7,52,-17,-29,-27,-25,-8,62,-30,-4,-9,66,-18,-19,-10,]),'RBRACKET':([5,6,7,8,10,11,12,13,14,16,17,18,19,20,21,23,30,31,34,35,36,38,39,41,44,47,49,51,52,55,60,62,64,65,66,],[-13,-14,-15,-16,-5,-6,-33,-34,-35,-20,-21,-22,-23,-24,35,-37,-38,-12,49,-28,-3,-26,-36,-7,-17,-29,-27,-25,-8,-30,-4,-9,-18,-19,-10,]),'COMMA':([5,6,7,8,10,11,12,13,14,16,17,18,19,20,23,28,29,30,31,34,35,36,37,38,39,41,42,44,47,49,51,52,55,56,57,58,60,62,63,64,65,66,],[-13,-14,-15,-16,-5,-6,-33,-34,-35,-20,-21,-22,-23,-24,-37,46,-31,-38,-12,50,-28,-3,50,-26,-36,-7,50,-17,-29,-27,-25,-8,-30,-32,-5,-6,-4,-9,50,-18,-19,-10,]),'RBRACE':([5,6,7,8,10,11,12,13,14,16,17,18,19,20,22,23,30,31,35,36,37,38,39,41,44,47,49,51,52,55,60,62,64,65,66,],[-13,-14,-15,-16,-5,-6,-33,-34,-35,-20,-21,-22,-23,-24,38,-37,-38,-12,-28,-3,51,-26,-36,-7,-17,-29,-27,-25,-8,-30,-4,-9,-18,-19,-10,]),'RPAREN_MAPSTO':([5,6,7,8,10,11,12,13,14,16,17,18,19,20,23,28,29,30,31,35,38,39,41,44,47,48,49,51,52,53,55,56,57,58,62,64,65,66,],[-13,-14,-15,-16,-5,-6,-33,-34,-35,-20,-21,-22,-23,-24,-37,45,-31,-38,-12,-28,-26,-36,-7,-17,-29,59,-27,-25,-8,61,-30,-32,-5,-6,-9,-18,-19,-10,]),'MAPSTO':([11,],[32,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'assign':([0,],[2,]),'expression':([0,9,10,21,22,23,24,25,32,33,43,45,50,54,59,61,],[3,27,30,36,36,39,40,36,47,48,53,55,60,36,64,65,]),'name':([0,9,10,21,22,23,24,25,32,33,43,45,46,50,54,59,61,],[4,29,31,31,31,31,31,31,31,31,31,31,56,31,31,31,31,]),'operator_invocation':([0,9,10,21,22,23,24,25,32,33,43,45,50,54,59,61,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'conditional':([0,9,10,21,22,23,24,25,32,33,43,45,50,54,59,61,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'call':([0,9,10,21,22,23,24,25,32,33,43,45,50,54,59,61,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'literal':([0,9,10,21,22,23,24,25,32,33,43,45,50,54,59,61,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'operator_invocation_postfix':([0,9,10,21,22,23,24,25,32,33,43,45,50,54,59,61,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'operator_invocation_prefix':([0,9,10,21,22,23,24,25,32,33,43,45,50,54,59,61,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'operator_invocation_infix':([0,9,10,21,22,23,24,25,32,33,43,45,50,54,59,61,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'list':([0,9,10,21,22,23,24,25,32,33,43,45,50,54,59,61,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'set':([0,9,10,21,22,23,24,25,32,33,43,45,50,54,59,61,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'lambda':([0,9,10,21,22,23,24,25,32,33,43,45,50,54,59,61,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'capture_list':([9,],[28,]),'arglist':([21,22,25,54,],[34,37,42,63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> assign','statement',1,'p_statment','myth_parse.py',91),
  ('statement -> expression','statement',1,'p_statment','myth_parse.py',92),
  ('arglist -> expression','arglist',1,'p_arglist','myth_parse.py',103),
  ('arglist -> arglist COMMA expression','arglist',3,'p_arglist','myth_parse.py',104),
  ('name -> OPERATOR','name',1,'p_name','myth_parse.py',113),
  ('name -> NAME','name',1,'p_name','myth_parse.py',114),
  ('call -> name LPAREN RPAREN','call',3,'p_call_name','myth_parse.py',120),
  ('call -> name LPAREN arglist RPAREN','call',4,'p_call_name','myth_parse.py',121),
  ('call -> LPAREN expression RPAREN LPAREN RPAREN','call',5,'p_call_expression','myth_parse.py',130),
  ('call -> LPAREN expression RPAREN LPAREN arglist RPAREN','call',6,'p_call_expression','myth_parse.py',131),
  ('assign -> name COLON expression','assign',3,'p_assign','myth_parse.py',140),
  ('expression -> name','expression',1,'p_expression_name','myth_parse.py',146),
  ('expression -> operator_invocation','expression',1,'p_expression','myth_parse.py',152),
  ('expression -> conditional','expression',1,'p_expression','myth_parse.py',153),
  ('expression -> call','expression',1,'p_expression','myth_parse.py',154),
  ('expression -> literal','expression',1,'p_expression','myth_parse.py',155),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','myth_parse.py',156),
  ('conditional -> BAR LPAREN expression RPAREN_MAPSTO expression','conditional',5,'p_conditional','myth_parse.py',165),
  ('conditional -> conditional BAR LPAREN expression RPAREN_MAPSTO expression','conditional',6,'p_conditional','myth_parse.py',166),
  ('literal -> NUMBER','literal',1,'p_literal','myth_parse.py',175),
  ('literal -> list','literal',1,'p_literal','myth_parse.py',176),
  ('literal -> set','literal',1,'p_literal','myth_parse.py',177),
  ('literal -> lambda','literal',1,'p_literal','myth_parse.py',178),
  ('literal -> STRING','literal',1,'p_literal','myth_parse.py',179),
  ('set -> LBRACE arglist RBRACE','set',3,'p_set','myth_parse.py',185),
  ('set -> LBRACE RBRACE','set',2,'p_set','myth_parse.py',186),
  ('list -> LBRACKET arglist RBRACKET','list',3,'p_list','myth_parse.py',195),
  ('list -> LBRACKET RBRACKET','list',2,'p_list','myth_parse.py',196),
  ('lambda -> NAME MAPSTO expression','lambda',3,'p_lambda','myth_parse.py',205),
  ('lambda -> LPAREN capture_list RPAREN_MAPSTO expression','lambda',4,'p_lambda','myth_parse.py',206),
  ('capture_list -> name','capture_list',1,'p_capture_list','myth_parse.py',215),
  ('capture_list -> capture_list COMMA name','capture_list',3,'p_capture_list','myth_parse.py',216),
  ('operator_invocation -> operator_invocation_postfix','operator_invocation',1,'p_operator_invocation','myth_parse.py',225),
  ('operator_invocation -> operator_invocation_prefix','operator_invocation',1,'p_operator_invocation','myth_parse.py',226),
  ('operator_invocation -> operator_invocation_infix','operator_invocation',1,'p_operator_invocation','myth_parse.py',227),
  ('operator_invocation_infix -> expression OPERATOR expression','operator_invocation_infix',3,'p_operator_invocation_infix','myth_parse.py',233),
  ('operator_invocation_postfix -> expression OPERATOR','operator_invocation_postfix',2,'p_operator_invocation_postfix','myth_parse.py',239),
  ('operator_invocation_prefix -> OPERATOR expression','operator_invocation_prefix',2,'p_operator_invocation_prefix','myth_parse.py',245),
]
