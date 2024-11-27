use db_instituicao_2v;

select * from tb_cursos;
select * from tb_disciplinas;
select * from tb_notas;
select * from tb_alunos;
select * from tb_matriculas;

-- Fazer 
select count(mat_id) from tb_matriculas join tb_cursos
on 2 = mat_curso_id;

delimiter !
create function fn_info_cursos (id int)
returns varchar (1000)
begin
set @num_matriculas = (select count(mat_id) from tb_matriculas);

end!
delimiter ;
