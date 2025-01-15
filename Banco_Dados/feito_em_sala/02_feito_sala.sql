# Faça uma função que receba o nome do livro e retorne o tatol de livros vendidos.

delimiter //
create function fn_total_vendas (nome varchar(50)) returns int
begin 	
	declare total int;
	set total = (select sum(pli_quantidade) from tb_livros join tb_pedidos_livros
    on liv_id = pli_liv_id
    where liv_titulo = nome);
    return total;
end//
delimiter ;

select liv_titulo, fn_total_vendas(liv_titulo) from tb_livros;
