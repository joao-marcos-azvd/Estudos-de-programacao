use db_instituicao_2v;

select * from tb_cursos;
select * from tb_disciplinas;
select * from tb_notas;
select * from tb_alunos;
select * from tb_matriculas;

-- Crie uma função que receba o ‘id do curso’ e retorne um texto com as seguintes informações do curso: 

-- Percentual de alunos aprovados;
create function 
fn_mpond (n1 float, n2 float, n3 float, n4 float)
returns varchar(10)
return round((n1 * 2 + n2 * 3 + n3 * 4 + n4 * 5)/14, 2);


delimiter //
create function fn_situacao(mediaPonderada float) 
returns varchar(45)
begin
    if mediaPonderada>=6 then return 'Aprovado';
    elseif mediaPonderada <=3.5 THEN return 'Reprovado';
    else return 'Prova Final';
    end if;
end //
delimiter ;

set @qntalunos = 
(select count(mat_id) from tb_matriculas 
where mat_curso_id = 2);

select alu_id from tb_alunos join tb_matriculas
on mat_alu_id = alu_id
where mat_curso_id = 2;

-- Percentual de alunos reprovados;
-- Quantidade de disciplinas;
-- Média geral do curso;
-- Quantidade de alunos acima da média do curso.

-- Fazer 
(select count(mat_id) from tb_matriculas 
where mat_curso_id = id);

delimiter !
create function fn_info_cursos (id int)
returns varchar (1000)
begin
set @qntalunos = 
(select count(mat_id) from tb_matriculas 
where mat_curso_id = id);

set @per_aprovados = 
"fazendo";

end!
delimiter ;
