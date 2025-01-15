delimiter //
create function fn_verifica(id int) returns varchar(20)
begin
	declare estoque int;
    set estoque = (select liv_estoque from tb_livros
    where liv_id = id);
    if estoque > 0 then
		return "Disponível";
	else 
		return "Indisponível";
    end if;
end//
delimiter ;

select * from tb_livros;

select liv_titulo, fn_verifica(liv_id) from tb_livros;

update tb_livros set liv_estoque = 0 
where liv_id = 7;
