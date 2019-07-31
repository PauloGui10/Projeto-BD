use oficina_bike;

#1 retorne o nome todos os clientes cujo nome começa com a letra C
SELECT 
    nome
FROM
    cliente
WHERE
    nome LIKE 'C%';

#2 retorne a média dos preços de todos os produtos
SELECT 
    AVG(preco) AS media_de_preços
FROM
    produto; 

#3 retorne as descrições dos serviços, cujo id_atendimento = 3
SELECT 
    id_atendimento, descricao
FROM
    servico
WHERE
    id_atendimento = 3;

#4 retorne os produtos fornecidos pelo fornecedor Ciclovix
SELECT 
    p.nome
FROM
    produto p
        JOIN
    fornece pf ON (p.id_produto = pf.id_produto)
        JOIN
    fornecedor f ON (f.id_fornecedor = pf.id_fornecedor)
WHERE
    nome_empresa = 'Ciclovix';

#5 retornar o cpf e o nome dos clientes que foram atendidos mais de uma vez, em ordem alfabética
SELECT 
    c.nome, a.cpf_cliente, COUNT(a.id_atendimento) AS atendidos
FROM
    cliente c
        JOIN
    atendimento a ON (c.cpf_cliente = a.cpf_cliente)
GROUP BY (a.cpf_cliente)
HAVING atendidos > 1
ORDER BY (c.nome);   

#6 retorne os nomes de todos os produtos e seus respectivos fornecedores (caso um produto não possua fornecedor, só retornará o nome do produto):   
SELECT 
    p.nome, f.nome_empresa
FROM
    produto p
        LEFT JOIN
    fornece pf ON (p.id_produto = pf.id_produto)
        LEFT JOIN
    fornecedor f ON (f.id_fornecedor = pf.id_fornecedor);

#7 retornar o cpf dos funcionários e a quantidade de atendimentos(inlusive aqueles que não realizaram nenhum), na ordem dos que mais realizaram atendimentos
SELECT 
    f.cpf_funcionario,
    COUNT(a.id_atendimento) AS qtd_atendimento
FROM
    funcionario f
        LEFT JOIN
    atendimento a ON (f.cpf_funcionario = a.cpf_funcionario)
GROUP BY (a.cpf_funcionario)
ORDER BY (qtd_atendimento) DESC;

#8 retornar todos os id de todos os atendimentos, com as descrições de seus respectivos serviços (caso o atendimento seja apenas uma compra, retornará apenas o id)
SELECT 
    a.id_atendimento, s.descricao
FROM
    servico s
        RIGHT JOIN
    atendimento a ON (s.id_atendimento = a.id_atendimento);

#9 retornar funcionários que possuem, ao menos, um atendimento:
SELECT 
    f.nome
FROM
    funcionario f
WHERE
    EXISTS( SELECT 
            *
        FROM
            atendimento a
        WHERE
            a.cpf_funcionario = f.cpf_funcionario);
    
#10 retornar os fornecedores que fornecem "câmara de ar"
SELECT 
    f.nome_empresa
FROM
    fornecedor f
WHERE
    f.id_fornecedor IN (SELECT 
            pf.id_fornecedor
        FROM
            fornece pf
                JOIN
            produto p ON (p.id_produto = pf.id_produto)
        WHERE
            p.nome = 'Câmara de ar'); 

#11 retornar o nome do(s) produto(s) que tem o preço maior do que todos os preços de serviços, cujo preço maior que 3 reais
SELECT 
    p.nome
FROM
    produto p
WHERE
    p.preco > ALL (SELECT 
            sc.preco
        FROM
            servico sc
        WHERE
            sc.preco > 3); 

#12 retornar o valor total das compras feitas por Danilo Pinto
SELECT 
    SUM(p.preco * c.quantidade) AS valor_total
FROM
    compra c
        JOIN
    produto p ON (c.id_produto = p.id_produto)
        JOIN
    atendimento a ON (c.id_atendimento = a.id_atendimento)
        JOIN
    cliente cl ON (cl.cpf_cliente = a.cpf_cliente)
WHERE
    cl.nome = 'Danilo Pinto';
    
# retornar os atendimentos do cliente com cpf = 11111111111
SELECT
    p.nome as nome_produto, c.quantidade, (p.preco*c.quantidade) as valor
FROM
    cliente cl
        JOIN
    atendimento a ON (cl.cpf_cliente = a.cpf_cliente)
        JOIN
    compra c ON (a.id_atendimento = c.id_atendimento)
        JOIN
    produto p ON (c.id_produto = p.id_produto)
WHERE
    cl.cpf_cliente = '11111111111';