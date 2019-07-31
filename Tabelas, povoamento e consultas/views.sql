use oficina_bike;

# retornar o somatório de todos os produtos
create view somatorio_precos as
	select sum(p.preco) from produto p;

# retornar o cpf dos clientes que compraram mais de uma vez
create view compras_clientes as
	select cl.cpf_cliente, count(c.id_atendimento) as qtd_atendimentos
    from 
		cliente cl join atendimento a on(cl.cpf_cliente = a.cpf_cliente)
        join compra c on(a.id_atendimento = c.id_atendimento)
		group by(c.id_atendimento)
        having qtd_atendimentos > 1;