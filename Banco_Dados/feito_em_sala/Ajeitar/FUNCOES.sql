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



# 1 - Calcular valor total (em reais) de pedidos de um cliente em um período;
delimiter //
create function fn_total_pedidos_cliente (id int) 

delimiter ;

select * from tb_clientes;

select cli_id, ped_total from tb_clientes join tb_pedidos
on cli_id = ped_cli_id
where month(ped_data) = curdate() - interval 12 month;

select ped_data from tb_pedidos join tb_clientes
on ped_cli_id = cli_id where cli_id = 2;

# 2 - Atualizar o estoque de um livro após um pedido;
DELIMITER //
CREATE FUNCTION fn_pedido_livro (id INT, emprestimo INT) 
RETURNS VARCHAR(255)
BEGIN
    DECLARE quant_livro INT;

    SET quant_livro = (SELECT liv_estoque FROM tb_livros WHERE liv_id = id);

    IF quant_livro IS NULL THEN
        RETURN 'Esse livro não existe.';
    ELSEIF quant_livro > 0 THEN
        UPDATE tb_livros 
        SET liv_estoque = quant_livro - emprestimo
        WHERE liv_id = id;
        
        RETURN 'Estoque atualizado!';
    ELSE
        RETURN 'Esse livro não está disponível.';
    END IF;
END //

DELIMITER ;

SELECT liv_id, liv_estoque FROM tb_livros;

SELECT fn_pedido_livro(1);



-- Parte 1 (Funciona)
delimiter //
create function fn_atualiza_livro(id_livro int, quant_emprestimo int) 
returns varchar (255)
begin
	declare total_livros int;
    set total_livros = (select liv_estoque from tb_livros where liv_id = id_livro);
    if total_livros >= 1 then
		update tb_livros
		set liv_estoque = total_livros - quant_emprestimo
		where liv_id = id_livro;
		return "Atualizado!";
	else 
		return "Livro esgotado!";
	end if;
end //
delimiter ;

-- Parte 2 (Funciona)
delimiter //
create function fn_atauliza (pedido_id int)
returns varchar (255)
begin
	declare var varchar (255);
	set var = (select group_concat(fn_atualiza_livro(pli_liv_id, pli_quantidade)) from tb_pedidos_livros where pli_ped_id = pedido_id);
	return "Livros atualixados!";
end //
delimiter ;

select fn_atualiza(1);
select fn_atualiza_livro(3, 20);
SELECT liv_id, liv_estoque FROM tb_livros;
select * from tb_pedidos;
select * from tb_pedidos_livros;

# 3 - Atualizar o valor total dos pedidos com base nos itens desses;


# 4 - Listar o nome dos livros que estão com estoque zerado; GROUP_CONCAT(coluna SEPARATOR ',')


# 5 - Atualizar o preço de um livro específico;
delimiter //
	create function fn_Q5 (id_livro int, novo_valor float) 
	return varchar (255)
	update tb_livros set liv_preco = novo_valor where liv_id = id_livro;
    return "Livro atualizado!"
delimiter ;

select * from tb_livros;
select fn_Q5(1, 10.0);
# 6 - Obter a média de livros, por pedido, para todos os clientes em um determinado período.
