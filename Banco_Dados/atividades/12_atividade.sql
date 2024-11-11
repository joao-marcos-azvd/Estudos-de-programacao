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
