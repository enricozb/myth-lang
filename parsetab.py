
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '5A71933CDB48B29F5F59D712E6D05AAC'
    
_lr_action_items = {'NAME':([0,7,11,12,13,14,27,31,32,34,],[4,17,21,21,21,21,21,21,21,21,]),'LPAREN':([0,4,7,11,12,13,14,17,21,25,27,31,32,34,],[7,13,7,7,7,7,7,13,13,31,7,7,7,7,]),'NUMBER':([0,7,11,12,13,14,27,31,32,34,],[8,8,8,8,8,8,8,8,8,8,]),'LBRACKET':([0,7,11,12,13,14,27,31,32,34,],[11,11,11,11,11,11,11,11,11,11,]),'$end':([1,2,3,4,5,6,8,9,10,19,21,22,24,29,30,36,37,38,],[0,-1,-2,-8,-9,-10,-11,-12,-13,-15,-8,-7,-16,-14,-5,-18,-17,-6,]),'COLON':([4,],[12,]),'MAPSTO':([4,17,21,26,28,],[14,14,14,32,34,]),'RPAREN':([5,6,8,9,10,15,16,17,19,20,21,23,24,29,30,33,35,36,37,38,],[-9,-10,-11,-12,-13,25,26,28,-15,-3,-8,30,-16,-14,-5,-4,38,-18,-17,-6,]),'COMMA':([5,6,8,9,10,15,16,17,18,19,20,21,23,24,29,30,33,35,36,37,38,],[-9,-10,-11,-12,-13,-3,27,-8,27,-15,-3,-8,27,-16,-14,-5,-4,27,-18,-17,-6,]),'RBRACKET':([5,6,8,9,10,11,18,19,20,21,24,29,30,33,36,37,38,],[-9,-10,-11,-12,-13,19,29,-15,-3,-8,-16,-14,-5,-4,-18,-17,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'assign':([0,],[2,]),'expression':([0,7,11,12,13,14,27,31,32,34,],[3,15,20,22,20,24,33,20,36,37,]),'call':([0,7,11,12,13,14,27,31,32,34,],[5,5,5,5,5,5,5,5,5,5,]),'literal':([0,7,11,12,13,14,27,31,32,34,],[6,6,6,6,6,6,6,6,6,6,]),'list':([0,7,11,12,13,14,27,31,32,34,],[9,9,9,9,9,9,9,9,9,9,]),'lambda':([0,7,11,12,13,14,27,31,32,34,],[10,10,10,10,10,10,10,10,10,10,]),'arglist':([7,11,13,31,],[16,18,23,35,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> assign','statement',1,'p_statment','myth.py',80),
  ('statement -> expression','statement',1,'p_statment','myth.py',81),
  ('arglist -> expression','arglist',1,'p_arglist','myth.py',89),
  ('arglist -> arglist COMMA expression','arglist',3,'p_arglist','myth.py',90),
  ('call -> NAME LPAREN arglist RPAREN','call',4,'p_call_name','myth.py',99),
  ('call -> LPAREN expression RPAREN LPAREN arglist RPAREN','call',6,'p_call_expression','myth.py',105),
  ('assign -> NAME COLON expression','assign',3,'p_assign','myth.py',111),
  ('expression -> NAME','expression',1,'p_expression_name','myth.py',117),
  ('expression -> call','expression',1,'p_expression','myth.py',123),
  ('expression -> literal','expression',1,'p_expression','myth.py',124),
  ('literal -> NUMBER','literal',1,'p_literal_number','myth.py',130),
  ('literal -> list','literal',1,'p_literal_number','myth.py',131),
  ('literal -> lambda','literal',1,'p_literal_number','myth.py',132),
  ('list -> LBRACKET arglist RBRACKET','list',3,'p_list','myth.py',138),
  ('list -> LBRACKET RBRACKET','list',2,'p_list','myth.py',139),
  ('lambda -> NAME MAPSTO expression','lambda',3,'p_lambda_singlearg','myth.py',148),
  ('lambda -> LPAREN NAME RPAREN MAPSTO expression','lambda',5,'p_lambda_singlearg','myth.py',149),
  ('lambda -> LPAREN arglist RPAREN MAPSTO expression','lambda',5,'p_lambda','myth.py',158),
]
