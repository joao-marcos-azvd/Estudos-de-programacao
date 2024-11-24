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
<<<<<<< HEAD
group by month(ven_data);
=======
group by month(ven_data) 
>>>>>>> 8292c7cee3787c44be167b244a0f0f46ccea8148

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
select cli_id from tb_clientes
where cli_id not in (select ven_cli_id from tb_vendas);

-- Qual é o nome e o e-mail do cliente que mais gastou em todas as suas compras?
select cli_nome, cli_email, sum(ven_total) as valor_max from tb_clientes join tb_vendas
on cli_id = ven_cli_id 
group by ven_cli_id
order by valor_max desc
limit 1;

-- Quais produtos foram vendidos pelo menor preço em relação ao seu preço original?
select pro_id, vpr_pro_id, pro_nome, pro_preco, vpr_precoproduto
from tb_produtos join tb_vendas_produtos
on pro_id = vpr_pro_id
where vpr_precoproduto < pro_preco;

-- Qual é o segundo maior valor total de uma venda?
select ven_total as valor from tb_vendas
where ven_total < (select max(ven_total) from tb_vendas)
group by ven_id
order by ven_total desc
limit 1;

-- Quais são os nomes dos clientes que compraram apenas uma vez?
select cli_nome, cli_id, count(ven_cli_id) as num_cli from tb_clientes join tb_vendas
on cli_id = ven_cli_id
group by ven_cli_id
having num_cli = 1;

-- Quais categorias de produtos nunca foram vendidas?
select cat_nome,  cat_id from tb_categorias
where cat_id not in (select cat_id from tb_categorias join tb_produtos
on cat_id = pro_categoria_id
join tb_vendas_produtos
on vpr_pro_id = pro_id);

-- Qual foi o mês com o maior valor total de vendas em todo o histórico?
select month(ven_data), sum(ven_total) from tb_vendas
group by month(ven_data);

-- Quais clientes compraram o produto mais caro vendido na loja?
select cli_nome, vpr_pro_id from tb_clientes join tb_vendas 
on cli_id = ven_cli_id 
join tb_vendas_produtos
on ven_id = vpr_ven_id 
join tb_produtos 
on pro_id = vpr_pro_id
where pro_preco = (select max(pro_preco) from tb_produtos);