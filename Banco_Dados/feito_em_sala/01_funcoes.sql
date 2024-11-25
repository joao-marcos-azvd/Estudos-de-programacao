create function 
fn_media(n1 float, n2 float, n3 float, n4 float)
returns float
return (n1 + n2 + n3 + n4)/4;

select not_alu_id, 
round(fn_media(not_nota1, not_nota2, not_nota3, not_nota4), 1)
from tb_notas;

create function 
fn_mpond (n1 float, n2 float, n3 float, n4 float)
returns varchar(10)
return round((n1 * 2 + n2 * 3 + n3 * 4 + n4 * 5)/14, 2);

drop function fn_mpond;

select not_alu_id,
round(fn_mpond(not_nota1, not_nota2, not_nota3, not_nota4), 2)
from tb_notas;

create function
fn_boas_vindas(s1 varchar(999), s2 varchar(999))
returns varchar(999)
return concat(s1, " ", s2, "!");

drop function fn_boas_vindas;

select fn_boas_vindas("Bem vindo,", alu_nome) as bem_vindo, 
fn_boas_vindas("Sua nota foi:", fn_mpond(not_nota1, not_nota2, not_nota3, not_nota4)) as sua_nota
from tb_alunos join tb_notas
on alu_id = not_alu_id;
