-- Criando a função pra calcular a média ponderada!
delimiter //
Create function fn_mediaPonderada(not1 float, not2 float, not3 float, not4 float)
returns float
begin
	declare media float;
    set media = (not1 * 2 + not2 * 2 + not3 * 3 + not4 * 3)/10;
    return media;
end //
delimiter ;

-- Criando a função pra retornar a situação
delimiter //
create function fn_situacao(media float)
returns varchar(255)
begin
	if media >= 6 then
		return "APROVAD@";
	else
		return "REPROVAD@";
	END IF;
end//
delimiter ;


-- Fazendo o procedimento
delimiter //
create procedure resumo_db_instituicao()
begin
	select curso_nome, dis_nome, alu_nome,
    round(fn_mediaPonderada(not_nota1, not_nota2, not_nota3, not_nota4), 2),
    fn_situacao(fn_mediaPonderada(not_nota1, not_nota2, not_nota3, not_nota4))
    from tb_cursos
    join tb_disciplinas on curso_id = dis_curso_id
    join tb_notas on not_dis_id = dis_id
    join tb_alunos on not_alu_id = alu_id;
end //
delimiter ;

call resumo_db_instituicao;

-- TESTE DO GPT
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
