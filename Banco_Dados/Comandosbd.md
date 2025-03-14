# Comandos Banco de Dados

- ADICIONA UMA NOVA COLUNA:

      alter table tb_funcionarios add column fun_cargo varchar(45);

- ALTERA O NOME DA TABELA:

      alter table NOME rename to NOME_NOVO

- REMOVE UMA COLUNA:
      
      alter table tb_funcionarios drop column fun_cargo;

- MODIFICA CARACTERISTICAS DA COLUNA:
      
      alter table tb_funcionarios modify column funn_cargo int;

- MODIFICA CARACTERISTICAS E O NOME DA COLUNA:

      alter table tb_funcionarios change column funn_cargo fun_cargo varchar(45);

- RENOMEIA O NOME DA TABELA :
      
      alter table tb_func rename to tb_funcionarios;

- SELECIONA TODOS OS ELEMENTOS DA TABELA:
      
      select * from tabela

- SELECIONA APENAS AS COUNAS ESPECÍFICAS:
      
      select COLUNA(S) from tabela

- ADICIONA VALORES AS COLUNAS DA TABELA:

      insert into TABELA (COLUNA(S)) values( VALOR(ES))
- Caso eu queira, posso inserir várias outras linhas.
      
      insert into TABELA (COLUNA(S)) values (VALOR(ES)), (VALOR(ES));

- REFERENCIA A CHAVE ESTRANGEIRA: 

      insert into tb_telcli values (default, '95876414', 10(Referencia));


- SELECIONA AS COLUNAS COM CONDIÇÃO (WHERE):
    
      select * from tb_alunos where alu_estado="NY" and alu_genero="M" or
      alu_bairro="Hollywood" and alu_genero="M";

- COLOCA OS PARAMENTROS EM ORDEM, DE ACORDO COM A COLUNA PASSA:
      
      select * from atletismo_resultados order by atleta_nome;

- COLOCA OS PARAMENTROS EM ORDEM REVERÇA, DE ACORDO COM A COLUNA PASSA:

      select * from atletismo_resultados order by atleta_nome desc;

- SELECIONA OS PARAMETROS QUE SÃO COMPATIVEIS COM OS TEMOS ESPECIFICADOS:
      
      select * from atletismo_resultados where pais in ("Brasil", "África do Sul");

- SELECIONA OS PARAMETROS QUE NÃO SÃO COMPATIVEIS COM OS TEMOS ESPECIFICADOS:

      select * from atletismo_resultados where pais not in ("Brasil", "África do Sul");

- SELECIONA OS PARAMETROS COM X LETRA NO COMEÇO:

      select * from tb_alunos where alu_nome like "a%";

- SELECIONA OS PARAMETROS COM X LETRA NO FINAL:
      
      select * from tb_alunos where alu_nome like "%a";

- SELECIONA OS PARAMETROS COM X LETRA EM QUALQUER PARTE:

      select * from tb_alunos where alu_nome like "%a%";

- SELECIONA OS PARAMETROS COM LIMITE:

      select * from tb_alunos where alu_nome like "%a%" limit 5;

- ATUALIZA TABELAS:
      
      update tb_jogadores  set jog_nome = 'Hugo' where jog_id = 1;

- DELETA ELEMENTOS DE TABELAS:

      delete from tb_jogadores  where jog_id = 1;

- MOSTRA A DATA ATUAL DO SISTEMA:
      
      select curdate();

- MOSTRA A DATA DO SISTEMA - UM INTERVALO DE TEMPO (DAY, MONTH, YEAR):

      select curdate() - interval 3 day;

- JUNÇÃO DE INTERVALOS:
      
        curdate() - interval 3 month - interval 15 day; 

- INTERLIGA DADOS DE TABELAS COM PELOMENOS UM DOS ELEMENTOS IGUAIS:

        select pro_id, pro_nome, pro_cat_id, cat_nome, cat_id, cat_descricao from tb_produtos join tb_categorias
        on pro_cat_id = cat_id;

- INTERLIGA DADOS DE TABELAS COM PELOMENOS UM DOS ELEMENTOS IGUAIS COM FILTRO:

        select pro_id, pro_nome, pro_cat_id, cat_nome, cat_id, cat_descricao from tb_produtos join tb_categorias
        on pro_cat_id = cat_id where cat_nome = 'Eletrônicos';

- RENOMEIA O NOME DA COLUNA:
      
      Nome_antigo as Nome_novo;

- EXTRAI APENAS O ANO DA DATA:
      
      year(DATA);

- REALIZA A FUNÇÃO E AGRUPA-A COM BASE EM OUTRA COLUNA PASSADA:
      
      select ven_data, sum(ven_total) from tb_vendas group by ven_data;

- FAZ UM FILTRO NA TABELA APOS O AGRUPAMENTO (SÓ PODE SER USADO DEPOIS DO "group by":

      select sum(valor) from tb_vendas where cli_nome like "a%" group by cli_nome having sum(valor) > 15;

- FAZ UM SUBCONSULTA (Uma consulta dentro de outra consulta):
  
        select pro_id, pro_preco from tb_produtos
        where pro_preco = (select max(pro_preco) from tb_produtos);

- LINK PARA VISUALIZAR FUNÇÕES DE AGREGAÇÃO: https://www.w3schools.com/sql/sql_ref_mysql.asp

- CRIANDO FUNÇÕES EM UMA LINHA:
  
      create function 
      fn_soma (a int, b int)
      returns int
      return a+b;

- CRIANDO FUNÇÕES EM VÁRIAS LINHAS:

      delimiter //
      create function fn_some(a int)
      returns int
      begin
      set @variavel_1=4;
      set @variavel_2=3;
      set @variavel_3=9;
      set @variavel_4= @variavel_1 + @variavel_2 + @variavel_3;
      return @varriavel_4;
      end //
      delimiter ;

- CRIANDO UM PROCEDIUMENTO NO SQL:

      DELIMITER //
      CREATE PROCEDURE verificar_idade(IN idade INT, OUT resultado VARCHAR(20))
      BEGIN
      IF idade >= 18 THEN
            SET resultado = 'Maior de idade';
      ELSE
            SET resultado = 'Menor de idade';
      END IF;
      END //
      DELIMITER ;

      CALL verificar_idade(25, @resu);
      select @resu;
  
      *Comando* --> *Descrição*              
      CREATE PROCEDURE nome_proc() --> Cria um procedimento       
      IN --> Parâmetro de entrada       
      OUT --> Parâmetro de saída
      INOUT --> Parâmetro de entrada e saída
      CALL nome_proc() --> Executa o procedimento

- CRIANDO UM GATILHO NO SQL:
  
      DELIMITER //

      CREATE TRIGGER after_update_notas 
      AFTER UPDATE ON tb_notas
      FOR EACH ROW
      BEGIN
          INSERT INTO historico_notas (id_aluno, nota1, nota2, nota3, nota4)
          VALUES (NEW.not_alu_id, NEW.not_nota1, NEW.not_nota2, NEW.not_nota3, NEW.not_nota4);
      END //
      
      DELIMITER ;

      EXPLICAÇÃO:
      AFTER UPDATE → O gatilho será executado após a execução de um UPDATE na tabela tb_notas.
      FOR EACH ROW → O gatilho é disparado para cada linha que for atualizada.
      NEW → Referência aos novos valores dos campos após o UPDATE.
