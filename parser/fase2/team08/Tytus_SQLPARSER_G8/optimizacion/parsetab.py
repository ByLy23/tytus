
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIGUALMAYORQMENORQMAYOR_IGUALQMENOR_IGUALQDISTINTOleftMASMENOSleftEXPONENCIACIONleftPORDIVIDIDOleftMODULOARROBA BLANCO CADENA CADENA2 CARACTER COMA COMENTARIO_MULTILINEA COMENTARIO_SIMPLE COMILLAS CORDER CORIZQ DISTINTO DIVIDIDO DOS_PUNTOS ENTERO EXPONENCIACION FDECIMAL ID IGUAL LLAVEDER LLAVEIZQ MAS MAYORQ MAYOR_IGUALQ MENORQ MENOR_IGUALQ MENOS MODULO NAME None PARDER PARIZQ POR PUNTO as def ejecutar ejecutar_analisis false for from global goto if import in label main print return true with_gotoinit : instruccionesinstrucciones : instrucciones instruccion\n    instrucciones : instruccion\n    instruccion : def main PARIZQ PARDER DOS_PUNTOS\n                   | def ID PARIZQ PARDER DOS_PUNTOS  \n    instruccion : importacion\n                   | ldeclaracionesg\n                   | decorador\n    instruccion : if PARIZQ expre relacional expre PARDER DOS_PUNTOS \n                    | if NAME IGUAL IGUAL CADENA DOS_PUNTOS\n    decorador : ARROBA with_goto\n    sentGoto : goto PUNTO ID\n    sentLabel : label PUNTO ID\n    importacion : from goto import with_goto importas\n                    | from lidsp import POR importas\n                    | from lidsp import ID importas\n    importas : as ID\n                |\n    importacion : import lidsp importas\n    lidsp : lidsp PUNTO ID\n    lidsp : ID\n            | main\n            | ejecutar\n    ldeclarlocals : ldeclarlocals ldeclaracionesg \n    ldeclarlocals : ldeclaracionesg\n    ldeclaracionesg : global ID\n    ldeclaracionesg : lidsp PARIZQ ID COMA ID PARDER\n                    | lidsp PARIZQ PARDER\n    \n    ldeclaracionesg : ID PARIZQ PARDER\n                    | main PARIZQ PARDER\n    ldeclaracionesg : print PARIZQ expresiones PARDER\n    ldeclaracionesg : print PARIZQ ID CADENA PARDER\n    ldeclaracionesg : ID PUNTO ID IGUAL expre\n    ldeclaracionesg : lidsp IGUAL expresiones \n                    | ID CORIZQ expresiones CORDER IGUAL expresiones\n                    | ID PUNTO ID PARIZQ ID PARDER\n                    | ID PUNTO ejecutar PARIZQ ID COMA ID PARDER\n                    | ID PUNTO ID IGUAL CORIZQ CORDER\n    ldeclaracionesg : for ID in lidsp DOS_PUNTOS\n    ldeclaracionesg : return\n                    | sentGoto\n                    | sentLabel\n    expresiones : expresiones IGUAL expresiones\n            | expresiones MAYORQ expresiones\n            | expresiones MENORQ expresiones\n            | expresiones MAYOR_IGUALQ expresiones\n            | expresiones MENOR_IGUALQ expresiones\n            | expresiones DISTINTO expresiones \n            | expresiones MAS expresiones\n            | expresiones MENOS expresiones\n            | expresiones POR expresiones\n            | expresiones DIVIDIDO expresiones\n            | expresiones EXPONENCIACION expresiones\n            | expresiones MODULO expresiones\n    relacional : IGUAL IGUAL\n            |   MAYORQ\n            |   MENORQ\n            |   MAYOR_IGUALQ\n            |   MENOR_IGUALQ\n            |   DISTINTO\n    expresiones : expre\n    expre : ID\n            |  ENTERO\n            |  FDECIMAL\n            |  CARACTER\n            |  None\n            |  true\n            |  false\n    expre : CADENA\n    expre : ID CADENA\n    expre : CORIZQ CORDER\n            |  CORIZQ expresiones CORDER\n    expre : ID CORIZQ expresiones CORDER\n            |  ID PARIZQ expresiones PARDER\n            |  ejecutar_analisis PARIZQ ID PARDER\n            |  ID PUNTO ejecutar PARIZQ ID COMA ID PARDER\n            '
    
_lr_action_items = {'def':([0,2,3,7,8,9,17,19,20,21,24,35,36,38,42,45,49,50,53,56,57,58,59,60,61,62,63,69,70,73,74,75,79,85,89,113,114,115,116,118,121,122,123,130,132,133,134,135,136,137,138,139,140,141,142,143,148,149,150,152,153,154,155,157,158,160,161,163,164,167,168,171,],[4,4,-3,-6,-7,-8,-23,-40,-41,-42,-2,-21,-22,-18,-26,-11,-30,-29,-62,-61,-63,-64,-65,-66,-67,-68,-69,-12,-19,-28,-34,-20,-13,-70,-71,-18,-18,-18,-17,-31,-4,-5,-33,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-14,-15,-16,-32,-39,-38,-36,-73,-74,-35,-75,-10,-27,-9,-37,-76,]),'if':([0,2,3,7,8,9,17,19,20,21,24,35,36,38,42,45,49,50,53,56,57,58,59,60,61,62,63,69,70,73,74,75,79,85,89,113,114,115,116,118,121,122,123,130,132,133,134,135,136,137,138,139,140,141,142,143,148,149,150,152,153,154,155,157,158,160,161,163,164,167,168,171,],[10,10,-3,-6,-7,-8,-23,-40,-41,-42,-2,-21,-22,-18,-26,-11,-30,-29,-62,-61,-63,-64,-65,-66,-67,-68,-69,-12,-19,-28,-34,-20,-13,-70,-71,-18,-18,-18,-17,-31,-4,-5,-33,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-14,-15,-16,-32,-39,-38,-36,-73,-74,-35,-75,-10,-27,-9,-37,-76,]),'from':([0,2,3,7,8,9,17,19,20,21,24,35,36,38,42,45,49,50,53,56,57,58,59,60,61,62,63,69,70,73,74,75,79,85,89,113,114,115,116,118,121,122,123,130,132,133,134,135,136,137,138,139,140,141,142,143,148,149,150,152,153,154,155,157,158,160,161,163,164,167,168,171,],[11,11,-3,-6,-7,-8,-23,-40,-41,-42,-2,-21,-22,-18,-26,-11,-30,-29,-62,-61,-63,-64,-65,-66,-67,-68,-69,-12,-19,-28,-34,-20,-13,-70,-71,-18,-18,-18,-17,-31,-4,-5,-33,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-14,-15,-16,-32,-39,-38,-36,-73,-74,-35,-75,-10,-27,-9,-37,-76,]),'import':([0,2,3,7,8,9,17,19,20,21,24,33,34,35,36,38,42,45,49,50,53,56,57,58,59,60,61,62,63,69,70,73,74,75,79,85,89,113,114,115,116,118,121,122,123,130,132,133,134,135,136,137,138,139,140,141,142,143,148,149,150,152,153,154,155,157,158,160,161,163,164,167,168,171,],[13,13,-3,-6,-7,-8,-23,-40,-41,-42,-2,67,68,-21,-22,-18,-26,-11,-30,-29,-62,-61,-63,-64,-65,-66,-67,-68,-69,-12,-19,-28,-34,-20,-13,-70,-71,-18,-18,-18,-17,-31,-4,-5,-33,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-14,-15,-16,-32,-39,-38,-36,-73,-74,-35,-75,-10,-27,-9,-37,-76,]),'global':([0,2,3,7,8,9,17,19,20,21,24,35,36,38,42,45,49,50,53,56,57,58,59,60,61,62,63,69,70,73,74,75,79,85,89,113,114,115,116,118,121,122,123,130,132,133,134,135,136,137,138,139,140,141,142,143,148,149,150,152,153,154,155,157,158,160,161,163,164,167,168,171,],[15,15,-3,-6,-7,-8,-23,-40,-41,-42,-2,-21,-22,-18,-26,-11,-30,-29,-62,-61,-63,-64,-65,-66,-67,-68,-69,-12,-19,-28,-34,-20,-13,-70,-71,-18,-18,-18,-17,-31,-4,-5,-33,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-14,-15,-16,-32,-39,-38,-36,-73,-74,-35,-75,-10,-27,-9,-37,-76,]),'ID':([0,2,3,4,7,8,9,11,13,15,17,18,19,20,21,24,29,30,31,35,36,37,38,39,40,41,42,43,45,46,49,50,53,54,56,57,58,59,60,61,62,63,68,69,70,71,73,74,75,78,79,82,83,84,85,86,87,89,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,108,109,110,111,113,114,115,116,117,118,121,122,123,124,130,131,132,133,134,135,136,137,138,139,140,141,142,143,146,148,149,150,152,153,154,155,156,157,158,159,160,161,163,164,167,168,169,171,],[6,6,-3,26,-6,-7,-8,35,35,42,-23,44,-40,-41,-42,-2,51,53,53,-21,-22,69,-18,72,53,75,-26,77,-11,79,-30,-29,-62,53,-61,-63,-64,-65,-66,-67,-68,-69,115,-12,-19,116,-28,-34,-20,35,-13,53,125,126,-70,53,53,-71,53,53,53,53,53,53,53,53,53,53,53,53,144,53,-56,-57,-58,-59,-60,-18,-18,-18,-17,151,-31,-4,-5,-33,53,-72,53,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-14,-15,-16,-32,-39,-38,-36,165,-73,-74,166,-35,-75,-10,-27,-9,-37,170,-76,]),'main':([0,2,3,4,7,8,9,11,13,17,19,20,21,24,35,36,38,42,45,49,50,53,56,57,58,59,60,61,62,63,69,70,73,74,75,78,79,85,89,113,114,115,116,118,121,122,123,130,132,133,134,135,136,137,138,139,140,141,142,143,148,149,150,152,153,154,155,157,158,160,161,163,164,167,168,171,],[5,5,-3,25,-6,-7,-8,36,36,-23,-40,-41,-42,-2,-21,-22,-18,-26,-11,-30,-29,-62,-61,-63,-64,-65,-66,-67,-68,-69,-12,-19,-28,-34,-20,36,-13,-70,-71,-18,-18,-18,-17,-31,-4,-5,-33,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-14,-15,-16,-32,-39,-38,-36,-73,-74,-35,-75,-10,-27,-9,-37,-76,]),'print':([0,2,3,7,8,9,17,19,20,21,24,35,36,38,42,45,49,50,53,56,57,58,59,60,61,62,63,69,70,73,74,75,79,85,89,113,114,115,116,118,121,122,123,130,132,133,134,135,136,137,138,139,140,141,142,143,148,149,150,152,153,154,155,157,158,160,161,163,164,167,168,171,],[16,16,-3,-6,-7,-8,-23,-40,-41,-42,-2,-21,-22,-18,-26,-11,-30,-29,-62,-61,-63,-64,-65,-66,-67,-68,-69,-12,-19,-28,-34,-20,-13,-70,-71,-18,-18,-18,-17,-31,-4,-5,-33,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-14,-15,-16,-32,-39,-38,-36,-73,-74,-35,-75,-10,-27,-9,-37,-76,]),'for':([0,2,3,7,8,9,17,19,20,21,24,35,36,38,42,45,49,50,53,56,57,58,59,60,61,62,63,69,70,73,74,75,79,85,89,113,114,115,116,118,121,122,123,130,132,133,134,135,136,137,138,139,140,141,142,143,148,149,150,152,153,154,155,157,158,160,161,163,164,167,168,171,],[18,18,-3,-6,-7,-8,-23,-40,-41,-42,-2,-21,-22,-18,-26,-11,-30,-29,-62,-61,-63,-64,-65,-66,-67,-68,-69,-12,-19,-28,-34,-20,-13,-70,-71,-18,-18,-18,-17,-31,-4,-5,-33,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-14,-15,-16,-32,-39,-38,-36,-73,-74,-35,-75,-10,-27,-9,-37,-76,]),'return':([0,2,3,7,8,9,17,19,20,21,24,35,36,38,42,45,49,50,53,56,57,58,59,60,61,62,63,69,70,73,74,75,79,85,89,113,114,115,116,118,121,122,123,130,132,133,134,135,136,137,138,139,140,141,142,143,148,149,150,152,153,154,155,157,158,160,161,163,164,167,168,171,],[19,19,-3,-6,-7,-8,-23,-40,-41,-42,-2,-21,-22,-18,-26,-11,-30,-29,-62,-61,-63,-64,-65,-66,-67,-68,-69,-12,-19,-28,-34,-20,-13,-70,-71,-18,-18,-18,-17,-31,-4,-5,-33,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-14,-15,-16,-32,-39,-38,-36,-73,-74,-35,-75,-10,-27,-9,-37,-76,]),'ARROBA':([0,2,3,7,8,9,17,19,20,21,24,35,36,38,42,45,49,50,53,56,57,58,59,60,61,62,63,69,70,73,74,75,79,85,89,113,114,115,116,118,121,122,123,130,132,133,134,135,136,137,138,139,140,141,142,143,148,149,150,152,153,154,155,157,158,160,161,163,164,167,168,171,],[22,22,-3,-6,-7,-8,-23,-40,-41,-42,-2,-21,-22,-18,-26,-11,-30,-29,-62,-61,-63,-64,-65,-66,-67,-68,-69,-12,-19,-28,-34,-20,-13,-70,-71,-18,-18,-18,-17,-31,-4,-5,-33,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-14,-15,-16,-32,-39,-38,-36,-73,-74,-35,-75,-10,-27,-9,-37,-76,]),'ejecutar':([0,2,3,7,8,9,11,13,17,19,20,21,24,29,35,36,38,42,45,49,50,53,56,57,58,59,60,61,62,63,69,70,73,74,75,78,79,85,88,89,113,114,115,116,118,121,122,123,130,132,133,134,135,136,137,138,139,140,141,142,143,148,149,150,152,153,154,155,157,158,160,161,163,164,167,168,171,],[17,17,-3,-6,-7,-8,17,17,-23,-40,-41,-42,-2,52,-21,-22,-18,-26,-11,-30,-29,-62,-61,-63,-64,-65,-66,-67,-68,-69,-12,-19,-28,-34,-20,17,-13,-70,129,-71,-18,-18,-18,-17,-31,-4,-5,-33,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-14,-15,-16,-32,-39,-38,-36,-73,-74,-35,-75,-10,-27,-9,-37,-76,]),'goto':([0,2,3,7,8,9,11,17,19,20,21,24,35,36,38,42,45,49,50,53,56,57,58,59,60,61,62,63,69,70,73,74,75,79,85,89,113,114,115,116,118,121,122,123,130,132,133,134,135,136,137,138,139,140,141,142,143,148,149,150,152,153,154,155,157,158,160,161,163,164,167,168,171,],[12,12,-3,-6,-7,-8,33,-23,-40,-41,-42,-2,-21,-22,-18,-26,-11,-30,-29,-62,-61,-63,-64,-65,-66,-67,-68,-69,-12,-19,-28,-34,-20,-13,-70,-71,-18,-18,-18,-17,-31,-4,-5,-33,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-14,-15,-16,-32,-39,-38,-36,-73,-74,-35,-75,-10,-27,-9,-37,-76,]),'label':([0,2,3,7,8,9,17,19,20,21,24,35,36,38,42,45,49,50,53,56,57,58,59,60,61,62,63,69,70,73,74,75,79,85,89,113,114,115,116,118,121,122,123,130,132,133,134,135,136,137,138,139,140,141,142,143,148,149,150,152,153,154,155,157,158,160,161,163,164,167,168,171,],[23,23,-3,-6,-7,-8,-23,-40,-41,-42,-2,-21,-22,-18,-26,-11,-30,-29,-62,-61,-63,-64,-65,-66,-67,-68,-69,-12,-19,-28,-34,-20,-13,-70,-71,-18,-18,-18,-17,-31,-4,-5,-33,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-14,-15,-16,-32,-39,-38,-36,-73,-74,-35,-75,-10,-27,-9,-37,-76,]),'$end':([1,2,3,7,8,9,17,19,20,21,24,35,36,38,42,45,49,50,53,56,57,58,59,60,61,62,63,69,70,73,74,75,79,85,89,113,114,115,116,118,121,122,123,130,132,133,134,135,136,137,138,139,140,141,142,143,148,149,150,152,153,154,155,157,158,160,161,163,164,167,168,171,],[0,-1,-3,-6,-7,-8,-23,-40,-41,-42,-2,-21,-22,-18,-26,-11,-30,-29,-62,-61,-63,-64,-65,-66,-67,-68,-69,-12,-19,-28,-34,-20,-13,-70,-71,-18,-18,-18,-17,-31,-4,-5,-33,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-14,-15,-16,-32,-39,-38,-36,-73,-74,-35,-75,-10,-27,-9,-37,-76,]),'PARIZQ':([5,6,10,14,16,17,25,26,51,52,53,64,75,77,129,],[27,28,31,39,43,-23,47,48,83,84,87,104,-20,87,159,]),'IGUAL':([5,6,14,17,32,51,53,55,56,57,58,59,60,61,62,63,65,66,74,75,76,77,85,89,90,91,106,119,127,128,130,132,133,134,135,136,137,138,139,140,141,142,143,157,158,160,161,171,],[-22,-21,40,-23,66,82,-62,92,-61,-63,-64,-65,-66,-67,-68,-69,106,112,92,-20,92,-62,-70,-71,92,131,146,-70,92,92,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-73,-74,92,-75,-76,]),'PUNTO':([5,6,12,14,17,23,34,35,36,38,53,75,77,120,],[-22,29,37,41,-23,46,41,-21,-22,41,88,-20,88,41,]),'CORIZQ':([6,30,31,40,43,53,54,77,82,86,87,92,93,94,95,96,97,98,99,100,101,102,103,105,107,108,109,110,111,124,131,146,],[30,54,54,54,54,86,54,86,124,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,-56,-57,-58,-59,-60,54,54,-55,]),'NAME':([10,],[32,]),'as':([17,35,36,38,75,113,114,115,],[-23,-21,-22,71,-20,71,71,71,]),'DOS_PUNTOS':([17,35,36,75,80,81,120,147,162,],[-23,-21,-22,-20,121,122,153,163,167,]),'with_goto':([22,67,],[45,113,]),'PARDER':([27,28,39,47,48,53,56,57,58,59,60,61,62,63,76,77,85,89,119,125,128,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,151,157,158,161,165,170,171,],[49,50,73,80,81,-62,-61,-63,-64,-65,-66,-67,-68,-69,118,-62,-70,-71,152,155,158,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,161,162,164,-73,-74,-75,168,171,-76,]),'ENTERO':([30,31,40,43,54,82,86,87,92,93,94,95,96,97,98,99,100,101,102,103,105,107,108,109,110,111,124,131,146,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,-56,-57,-58,-59,-60,57,57,-55,]),'FDECIMAL':([30,31,40,43,54,82,86,87,92,93,94,95,96,97,98,99,100,101,102,103,105,107,108,109,110,111,124,131,146,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,-56,-57,-58,-59,-60,58,58,-55,]),'CARACTER':([30,31,40,43,54,82,86,87,92,93,94,95,96,97,98,99,100,101,102,103,105,107,108,109,110,111,124,131,146,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,-56,-57,-58,-59,-60,59,59,-55,]),'None':([30,31,40,43,54,82,86,87,92,93,94,95,96,97,98,99,100,101,102,103,105,107,108,109,110,111,124,131,146,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,-56,-57,-58,-59,-60,60,60,-55,]),'true':([30,31,40,43,54,82,86,87,92,93,94,95,96,97,98,99,100,101,102,103,105,107,108,109,110,111,124,131,146,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,-56,-57,-58,-59,-60,61,61,-55,]),'false':([30,31,40,43,54,82,86,87,92,93,94,95,96,97,98,99,100,101,102,103,105,107,108,109,110,111,124,131,146,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,-56,-57,-58,-59,-60,62,62,-55,]),'CADENA':([30,31,40,43,53,54,77,82,86,87,92,93,94,95,96,97,98,99,100,101,102,103,105,107,108,109,110,111,112,124,131,146,],[63,63,63,63,85,63,119,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,-56,-57,-58,-59,-60,147,63,63,-55,]),'ejecutar_analisis':([30,31,40,43,54,82,86,87,92,93,94,95,96,97,98,99,100,101,102,103,105,107,108,109,110,111,124,131,146,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,-56,-57,-58,-59,-60,64,64,-55,]),'in':([44,],[78,]),'CORDER':([53,54,55,56,57,58,59,60,61,62,63,85,89,90,124,127,130,132,133,134,135,136,137,138,139,140,141,142,143,157,158,161,171,],[-62,89,91,-61,-63,-64,-65,-66,-67,-68,-69,-70,-71,130,154,157,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-73,-74,-75,-76,]),'MAYORQ':([53,55,56,57,58,59,60,61,62,63,65,74,76,77,85,89,90,119,127,128,130,132,133,134,135,136,137,138,139,140,141,142,143,157,158,160,161,171,],[-62,93,-61,-63,-64,-65,-66,-67,-68,-69,107,93,93,-62,-70,-71,93,-70,93,93,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-73,-74,93,-75,-76,]),'MENORQ':([53,55,56,57,58,59,60,61,62,63,65,74,76,77,85,89,90,119,127,128,130,132,133,134,135,136,137,138,139,140,141,142,143,157,158,160,161,171,],[-62,94,-61,-63,-64,-65,-66,-67,-68,-69,108,94,94,-62,-70,-71,94,-70,94,94,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-73,-74,94,-75,-76,]),'MAYOR_IGUALQ':([53,55,56,57,58,59,60,61,62,63,65,74,76,77,85,89,90,119,127,128,130,132,133,134,135,136,137,138,139,140,141,142,143,157,158,160,161,171,],[-62,95,-61,-63,-64,-65,-66,-67,-68,-69,109,95,95,-62,-70,-71,95,-70,95,95,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-73,-74,95,-75,-76,]),'MENOR_IGUALQ':([53,55,56,57,58,59,60,61,62,63,65,74,76,77,85,89,90,119,127,128,130,132,133,134,135,136,137,138,139,140,141,142,143,157,158,160,161,171,],[-62,96,-61,-63,-64,-65,-66,-67,-68,-69,110,96,96,-62,-70,-71,96,-70,96,96,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-73,-74,96,-75,-76,]),'DISTINTO':([53,55,56,57,58,59,60,61,62,63,65,74,76,77,85,89,90,119,127,128,130,132,133,134,135,136,137,138,139,140,141,142,143,157,158,160,161,171,],[-62,97,-61,-63,-64,-65,-66,-67,-68,-69,111,97,97,-62,-70,-71,97,-70,97,97,-72,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-73,-74,97,-75,-76,]),'MAS':([53,55,56,57,58,59,60,61,62,63,74,76,77,85,89,90,119,127,128,130,132,133,134,135,136,137,138,139,140,141,142,143,157,158,160,161,171,],[-62,98,-61,-63,-64,-65,-66,-67,-68,-69,98,98,-62,-70,-71,98,-70,98,98,-72,98,98,98,98,98,98,-49,-50,-51,-52,-53,-54,-73,-74,98,-75,-76,]),'MENOS':([53,55,56,57,58,59,60,61,62,63,74,76,77,85,89,90,119,127,128,130,132,133,134,135,136,137,138,139,140,141,142,143,157,158,160,161,171,],[-62,99,-61,-63,-64,-65,-66,-67,-68,-69,99,99,-62,-70,-71,99,-70,99,99,-72,99,99,99,99,99,99,-49,-50,-51,-52,-53,-54,-73,-74,99,-75,-76,]),'POR':([53,55,56,57,58,59,60,61,62,63,68,74,76,77,85,89,90,119,127,128,130,132,133,134,135,136,137,138,139,140,141,142,143,157,158,160,161,171,],[-62,100,-61,-63,-64,-65,-66,-67,-68,-69,114,100,100,-62,-70,-71,100,-70,100,100,-72,100,100,100,100,100,100,100,100,-51,-52,100,-54,-73,-74,100,-75,-76,]),'DIVIDIDO':([53,55,56,57,58,59,60,61,62,63,74,76,77,85,89,90,119,127,128,130,132,133,134,135,136,137,138,139,140,141,142,143,157,158,160,161,171,],[-62,101,-61,-63,-64,-65,-66,-67,-68,-69,101,101,-62,-70,-71,101,-70,101,101,-72,101,101,101,101,101,101,101,101,-51,-52,101,-54,-73,-74,101,-75,-76,]),'EXPONENCIACION':([53,55,56,57,58,59,60,61,62,63,74,76,77,85,89,90,119,127,128,130,132,133,134,135,136,137,138,139,140,141,142,143,157,158,160,161,171,],[-62,102,-61,-63,-64,-65,-66,-67,-68,-69,102,102,-62,-70,-71,102,-70,102,102,-72,102,102,102,102,102,102,102,102,-51,-52,-53,-54,-73,-74,102,-75,-76,]),'MODULO':([53,55,56,57,58,59,60,61,62,63,74,76,77,85,89,90,119,127,128,130,132,133,134,135,136,137,138,139,140,141,142,143,157,158,160,161,171,],[-62,103,-61,-63,-64,-65,-66,-67,-68,-69,103,103,-62,-70,-71,103,-70,103,103,-72,103,103,103,103,103,103,103,103,103,103,103,-54,-73,-74,103,-75,-76,]),'COMA':([72,126,166,],[117,156,169,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,24,]),'importacion':([0,2,],[7,7,]),'ldeclaracionesg':([0,2,],[8,8,]),'decorador':([0,2,],[9,9,]),'lidsp':([0,2,11,13,78,],[14,14,34,38,120,]),'sentGoto':([0,2,],[20,20,]),'sentLabel':([0,2,],[21,21,]),'expresiones':([30,40,43,54,86,87,92,93,94,95,96,97,98,99,100,101,102,103,124,131,],[55,74,76,90,127,128,132,133,134,135,136,137,138,139,140,141,142,143,90,160,]),'expre':([30,31,40,43,54,82,86,87,92,93,94,95,96,97,98,99,100,101,102,103,105,124,131,],[56,65,56,56,56,123,56,56,56,56,56,56,56,56,56,56,56,56,56,56,145,56,56,]),'importas':([38,113,114,115,],[70,148,149,150,]),'relacional':([65,],[105,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','sintacticoC3D.py',42),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_intrucciones','sintacticoC3D.py',47),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones2','sintacticoC3D.py',53),
  ('instruccion -> def main PARIZQ PARDER DOS_PUNTOS','instruccion',5,'p_intruccion','sintacticoC3D.py',58),
  ('instruccion -> def ID PARIZQ PARDER DOS_PUNTOS','instruccion',5,'p_intruccion','sintacticoC3D.py',59),
  ('instruccion -> importacion','instruccion',1,'p_instruccion2','sintacticoC3D.py',66),
  ('instruccion -> ldeclaracionesg','instruccion',1,'p_instruccion2','sintacticoC3D.py',67),
  ('instruccion -> decorador','instruccion',1,'p_instruccion2','sintacticoC3D.py',68),
  ('instruccion -> if PARIZQ expre relacional expre PARDER DOS_PUNTOS','instruccion',7,'p_instruccion3','sintacticoC3D.py',73),
  ('instruccion -> if NAME IGUAL IGUAL CADENA DOS_PUNTOS','instruccion',6,'p_instruccion3','sintacticoC3D.py',74),
  ('decorador -> ARROBA with_goto','decorador',2,'p_decorador','sintacticoC3D.py',83),
  ('sentGoto -> goto PUNTO ID','sentGoto',3,'p_goto','sintacticoC3D.py',89),
  ('sentLabel -> label PUNTO ID','sentLabel',3,'p_label','sintacticoC3D.py',95),
  ('importacion -> from goto import with_goto importas','importacion',5,'p_importacion','sintacticoC3D.py',101),
  ('importacion -> from lidsp import POR importas','importacion',5,'p_importacion','sintacticoC3D.py',102),
  ('importacion -> from lidsp import ID importas','importacion',5,'p_importacion','sintacticoC3D.py',103),
  ('importas -> as ID','importas',2,'p_importas','sintacticoC3D.py',109),
  ('importas -> <empty>','importas',0,'p_importas','sintacticoC3D.py',110),
  ('importacion -> import lidsp importas','importacion',3,'p_importacion2','sintacticoC3D.py',118),
  ('lidsp -> lidsp PUNTO ID','lidsp',3,'p_lidsp','sintacticoC3D.py',123),
  ('lidsp -> ID','lidsp',1,'p_lidsp2','sintacticoC3D.py',129),
  ('lidsp -> main','lidsp',1,'p_lidsp2','sintacticoC3D.py',130),
  ('lidsp -> ejecutar','lidsp',1,'p_lidsp2','sintacticoC3D.py',131),
  ('ldeclarlocals -> ldeclarlocals ldeclaracionesg','ldeclarlocals',2,'p_ldeclarlocals','sintacticoC3D.py',136),
  ('ldeclarlocals -> ldeclaracionesg','ldeclarlocals',1,'p_ldeclarlocals2','sintacticoC3D.py',142),
  ('ldeclaracionesg -> global ID','ldeclaracionesg',2,'p_ldeclaracionesg','sintacticoC3D.py',147),
  ('ldeclaracionesg -> lidsp PARIZQ ID COMA ID PARDER','ldeclaracionesg',6,'p_ldeclaracionesg2','sintacticoC3D.py',154),
  ('ldeclaracionesg -> lidsp PARIZQ PARDER','ldeclaracionesg',3,'p_ldeclaracionesg2','sintacticoC3D.py',155),
  ('ldeclaracionesg -> ID PARIZQ PARDER','ldeclaracionesg',3,'p_ldeclaracionesg0','sintacticoC3D.py',167),
  ('ldeclaracionesg -> main PARIZQ PARDER','ldeclaracionesg',3,'p_ldeclaracionesg0','sintacticoC3D.py',168),
  ('ldeclaracionesg -> print PARIZQ expresiones PARDER','ldeclaracionesg',4,'p_ldeclaracionesg3','sintacticoC3D.py',173),
  ('ldeclaracionesg -> print PARIZQ ID CADENA PARDER','ldeclaracionesg',5,'p_ldeclaracionesg31','sintacticoC3D.py',179),
  ('ldeclaracionesg -> ID PUNTO ID IGUAL expre','ldeclaracionesg',5,'p_ldeclaracionesg4x','sintacticoC3D.py',185),
  ('ldeclaracionesg -> lidsp IGUAL expresiones','ldeclaracionesg',3,'p_ldeclaracionesg4','sintacticoC3D.py',191),
  ('ldeclaracionesg -> ID CORIZQ expresiones CORDER IGUAL expresiones','ldeclaracionesg',6,'p_ldeclaracionesg4','sintacticoC3D.py',192),
  ('ldeclaracionesg -> ID PUNTO ID PARIZQ ID PARDER','ldeclaracionesg',6,'p_ldeclaracionesg4','sintacticoC3D.py',193),
  ('ldeclaracionesg -> ID PUNTO ejecutar PARIZQ ID COMA ID PARDER','ldeclaracionesg',8,'p_ldeclaracionesg4','sintacticoC3D.py',194),
  ('ldeclaracionesg -> ID PUNTO ID IGUAL CORIZQ CORDER','ldeclaracionesg',6,'p_ldeclaracionesg4','sintacticoC3D.py',195),
  ('ldeclaracionesg -> for ID in lidsp DOS_PUNTOS','ldeclaracionesg',5,'p_ldeclaracionesg5','sintacticoC3D.py',214),
  ('ldeclaracionesg -> return','ldeclaracionesg',1,'p_ldeclaracionesg6','sintacticoC3D.py',221),
  ('ldeclaracionesg -> sentGoto','ldeclaracionesg',1,'p_ldeclaracionesg6','sintacticoC3D.py',222),
  ('ldeclaracionesg -> sentLabel','ldeclaracionesg',1,'p_ldeclaracionesg6','sintacticoC3D.py',223),
  ('expresiones -> expresiones IGUAL expresiones','expresiones',3,'p_expresiones500','sintacticoC3D.py',228),
  ('expresiones -> expresiones MAYORQ expresiones','expresiones',3,'p_expresiones500','sintacticoC3D.py',229),
  ('expresiones -> expresiones MENORQ expresiones','expresiones',3,'p_expresiones500','sintacticoC3D.py',230),
  ('expresiones -> expresiones MAYOR_IGUALQ expresiones','expresiones',3,'p_expresiones500','sintacticoC3D.py',231),
  ('expresiones -> expresiones MENOR_IGUALQ expresiones','expresiones',3,'p_expresiones500','sintacticoC3D.py',232),
  ('expresiones -> expresiones DISTINTO expresiones','expresiones',3,'p_expresiones500','sintacticoC3D.py',233),
  ('expresiones -> expresiones MAS expresiones','expresiones',3,'p_expresiones500','sintacticoC3D.py',234),
  ('expresiones -> expresiones MENOS expresiones','expresiones',3,'p_expresiones500','sintacticoC3D.py',235),
  ('expresiones -> expresiones POR expresiones','expresiones',3,'p_expresiones500','sintacticoC3D.py',236),
  ('expresiones -> expresiones DIVIDIDO expresiones','expresiones',3,'p_expresiones500','sintacticoC3D.py',237),
  ('expresiones -> expresiones EXPONENCIACION expresiones','expresiones',3,'p_expresiones500','sintacticoC3D.py',238),
  ('expresiones -> expresiones MODULO expresiones','expresiones',3,'p_expresiones500','sintacticoC3D.py',239),
  ('relacional -> IGUAL IGUAL','relacional',2,'p_relacional','sintacticoC3D.py',244),
  ('relacional -> MAYORQ','relacional',1,'p_relacional','sintacticoC3D.py',245),
  ('relacional -> MENORQ','relacional',1,'p_relacional','sintacticoC3D.py',246),
  ('relacional -> MAYOR_IGUALQ','relacional',1,'p_relacional','sintacticoC3D.py',247),
  ('relacional -> MENOR_IGUALQ','relacional',1,'p_relacional','sintacticoC3D.py',248),
  ('relacional -> DISTINTO','relacional',1,'p_relacional','sintacticoC3D.py',249),
  ('expresiones -> expre','expresiones',1,'p_expresiones502','sintacticoC3D.py',254),
  ('expre -> ID','expre',1,'p_expre','sintacticoC3D.py',259),
  ('expre -> ENTERO','expre',1,'p_expre','sintacticoC3D.py',260),
  ('expre -> FDECIMAL','expre',1,'p_expre','sintacticoC3D.py',261),
  ('expre -> CARACTER','expre',1,'p_expre','sintacticoC3D.py',262),
  ('expre -> None','expre',1,'p_expre','sintacticoC3D.py',263),
  ('expre -> true','expre',1,'p_expre','sintacticoC3D.py',264),
  ('expre -> false','expre',1,'p_expre','sintacticoC3D.py',265),
  ('expre -> CADENA','expre',1,'p_expre22','sintacticoC3D.py',270),
  ('expre -> ID CADENA','expre',2,'p_expre23','sintacticoC3D.py',275),
  ('expre -> CORIZQ CORDER','expre',2,'p_expre2','sintacticoC3D.py',280),
  ('expre -> CORIZQ expresiones CORDER','expre',3,'p_expre2','sintacticoC3D.py',281),
  ('expre -> ID CORIZQ expresiones CORDER','expre',4,'p_expre3','sintacticoC3D.py',289),
  ('expre -> ID PARIZQ expresiones PARDER','expre',4,'p_expre3','sintacticoC3D.py',290),
  ('expre -> ejecutar_analisis PARIZQ ID PARDER','expre',4,'p_expre3','sintacticoC3D.py',291),
  ('expre -> ID PUNTO ejecutar PARIZQ ID COMA ID PARDER','expre',8,'p_expre3','sintacticoC3D.py',292),
]
