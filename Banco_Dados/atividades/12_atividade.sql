USE db_vendas;

-- Qual é o total gasto por cada cliente em todas as suas compras?
SELECT cli_nome, SUM(ven_total) FROM tb_clientes JOIN tb_vendas
ON cli_id = ven_cli_id GROUP BY cli_nome;

-- Quais produtos foram vendidos em mais de uma venda e quantas vezes cada um foi vendido?
SELECT vpr_pro_id, COUNT(vpr_ven_id) FROM tb_vendas_produtos
GROUP BY vpr_pro_id HAVING COUNT(vpr_ven_id) > 1;

-- Qual é a média de quantidade vendida por produto para cada categoria?
SELECT cat_nome, AVG(vpr_quantProduto) FROM tb_categorias JOIN tb_produtos
ON cat_id = pro_categoria_id
JOIN tb_vendas_produtos
ON pro_id = vpr_pro_id 
GROUP BY cat_nome;

-- Quais clientes realizaram mais de uma compra?
select cli_nome,count(ven_cli_id) from tb_clientes join tb_vendas 
on ven_cli_id = cli_id 
group by cli_nome
having count(ven_cli_id) > 1;


-- Qual é a média de preço dos produtos vendidos em cada categoria?
select cat_nome, avg(vpr_precoProduto) from tb_vendas_produtos join tb_produtos
on  vpr_pro_id = pro_id 
join tb_categorias 
on pro_categoria_id = cat_id 
group by cat_nome; 


-- Quais categorias tiveram um total de vendas superior a um valor específico?
select cat_nome, sum(ven_total) from tb_vendas join tb_vendas_produtos 
on vpr_ven_id = ven_id 
join tb_produtos 
on vpr_pro_id = pro_id 
join tb_categorias 
on pro_categoria_id = cat_id 
group by cat_nome
having sum(ven_total) > 15;


-- Qual é a data e o valor da compra mais cara de cada cliente?
select cli_nome, ven_data, max(ven_total)from tb_clientes join tb_vendas
on ven_cli_id = cli_id 
group by cli_nome;


-- Quais produtos têm uma quantidade total vendida superior a um valor específico?
select pro_nome, sum(vpr_quantProduto) from tb_produtos join tb_vendas_produtos
on vpr_pro_id = pro_id
group by pro_nome 
having sum(vpr_quantProduto) > 20;  


-- Qual foi a média de valor gasto em cada mês?
select ven_data, avg(ven_total) from tb_vendas 
group by month(ven_data) 

USE db_vendas;

-- Quais clientes compraram produtos de categorias diferentes em suas compras?

-------- 2 Parte --------
-- Qual é o nome do cliente que realizou a compra mais cara?
select cli_nome, ven_total from tb_clientes join tb_vendas
on ven_cli_id = cli_id
where ven_total = (select max(ven_total) from tb_vendas);

-- Quais produtos nunca foram vendidos?
select pro_nome, pro_id from tb_produtos
where pro_id not in (select vpr_pro_id from tb_vendas_produtos);

-- Quais clientes nunca realizaram uma compra?
-- Qual é o nome e o e-mail do cliente que mais gastou em todas as suas compras?
-- Quais produtos foram vendidos pelo menor preço em relação ao seu preço original?
-- Qual é o segundo maior valor total de uma venda?
-- Quais são os nomes dos clientes que compraram apenas uma vez?
-- Quais categorias de produtos nunca foram vendidas?
-- Qual foi o mês com o maior valor total de vendas em todo o histórico?
-- Quais clientes compraram o produto mais caro vendido na loja?
