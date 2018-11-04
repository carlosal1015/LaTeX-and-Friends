## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file 10112018.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_5 = Integer(5); _sage_const_9 = Integer(9); _sage_const_10 = Integer(10); _sage_const_16 = Integer(16); _sage_const_19 = Integer(19)## This file (10112018.sagetex.sage) was *autogenerated* from 10112018.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('10112018', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_3 
_st_.blockbegin()
try:
 __tmp__=var("x"); f = symbolic_expression(exp(x) * sin(_sage_const_2 *x)).function(x)
except:
 _st_.goboom(_sage_const_5 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_9 
 _st_.inline(_sage_const_0 , latex(f(x)))
except:
 _st_.goboom(_sage_const_9 )
try:
 _st_.current_tex_line = _sage_const_10 
 _st_.inline(_sage_const_1 , latex(diff(f, x, _sage_const_2 )(x)))
except:
 _st_.goboom(_sage_const_10 )
_st_.current_tex_line = _sage_const_16 
_st_.blockbegin()
try:
 plt  = plot(f, -_sage_const_1 , _sage_const_1 )
 plt.save("MyPic.pdf")
except:
 _st_.goboom(_sage_const_19 )
_st_.blockend()
_st_.endofdoc()

