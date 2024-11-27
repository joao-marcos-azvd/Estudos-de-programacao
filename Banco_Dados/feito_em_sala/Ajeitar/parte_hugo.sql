delimiter //
create function fn_resumo(id int)
returns varchar(45)
begin
set @qntTotal = 
(select count(mat_id) from tb_matriculas 
where mat_curso_id = id);

return concat("O total de alunos matriculados é: ", @qntTotal);
end //
delimiter ;

select fn_resumo(2);
