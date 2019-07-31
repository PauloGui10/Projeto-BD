use oficina_bike;

insert into cliente values 
("11111111111", "Antonio Peixoto", "82349810"),
("22222222222", "Cláudio Oliveira", "45349811"),
("33333333333", "Clara Oliveira", "67349812"),
("44444444444", "Pedro Alcântara", "89349813"),
("55555555555", "Danilo Pinto", "21349814"),
("66666666666", "Jacinto Leite", "77349815"),
("77777777777", "Mário Alencar", "80349816");
SELECT 
    *
FROM
    cliente;

delete from cliente where cpf_cliente = '66666666666';
insert into funcionario values ("12121212121", "Jefferson Dias");
insert into funcionario values ("13131313131", "Júnior Batata");
insert into funcionario values ("14141414141", "Jurandir Ferreira");
insert into funcionario values ("15151515151", "Eduardo Ramos");
insert into funcionario values ("16161616161", "José Carlos");
insert into funcionario values ("17171717171", "Clodoaldo Costa");
SELECT 
    *
FROM
    funcionario;

insert into nota_fiscal values (default, "2019-01-23"); #1
insert into nota_fiscal values (default, "2019-02-12"); #2
insert into nota_fiscal values (default, "2019-02-19"); #3
insert into nota_fiscal values (default, "2019-02-23");SELECT 
    *
FROM
    nota_fiscal;

insert into fornecedor values (default, "Ferragem Ltda.", "34659003");   #1
insert into fornecedor values (default, "Peças Top", "34045034");	     #2
insert into fornecedor values (default, "JR Distribuidora", "38959045"); #3
insert into fornecedor values (default, "Ciclovix", "32655900");		SELECT 
    *
FROM
    fornecedor;

insert into produto values (default, "Quadro", 300.00);		 #1
insert into produto values (default, "Guidão", 120.00); 	 #2
insert into produto values (default, "Câmara de ar", 30.00); #3
insert into produto values (default, "Jante", 80.00); 		 #4
insert into produto values (default, "Rolamento", 20.00);    #5
insert into produto values (default, "Pneu", 10.00);         #6
insert into produto values (default, "Sapata", 4.00);        #7
insert into produto values (default, "Selim", 50.00);        #8
insert into produto values (default, "Capacete", 70.00);     #9
insert into produto values (default, "pedal", 15.00);SELECT 
    *
FROM
    produto;

insert into fornece values (1,2);
insert into fornece values (1,4);
insert into fornece values (3,2);
insert into fornece values (5,2);
insert into fornece values (10,3);
insert into fornece values (8,1);
insert into fornece values (7,3);
insert into fornece values (9,2);
insert into fornece values (3,4);
insert into fornece values (4,3);
SELECT 
    *
FROM
    fornece;

insert into atendimento values (default, "22222222222", "13131313131", 2); #1
insert into atendimento values (default, "11111111111", "17171717171", 3); #2
insert into atendimento values (default, "55555555555", "12121212121", 4); #3
insert into atendimento values (default, "33333333333", "17171717171", 1); #4
insert into atendimento values (default, "22222222222", "14141414141", 2); #5
insert into atendimento values (default, "66666666666", "12121212121", 2); #6
insert into atendimento values (default, "33333333333", "13131313131", 1); #7
insert into atendimento values (default, "55555555555", "13131313131", 4); #8
insert into atendimento values (default, "11111111111", "17171717171", 3); #9
insert into atendimento values (default, "33333333333", "12121212121", 3); #10
insert into atendimento values (default, "55555555555", "17171717171", 3); #11
insert into atendimento values (default, "11111111111", "14141414141", 3);SELECT 
    *
FROM
    atendimento;

insert into compra values (3, 6, 2, "2019-01-21");
insert into compra values (3, 5, 2, "2019-01-21");
insert into compra values (9, 8, 1, "2019-01-27");
insert into compra values (7, 3, 4, "2019-02-04");
insert into compra values (2, 4, 2, "2019-02-15");
insert into compra values (8, 4, 1, "2019-03-03");
insert into compra values (2, 2, 1, "2019-03-18");
insert into compra values (11, 1, 3, "2019-03-21");
insert into compra values (12, 7, 2, "2019-03-27");
SELECT 
    *
FROM
    compra;

insert into servico values (3, "Troca de pneu", 20.00);
insert into servico values (4, "Troca sapata", 5.00);
insert into servico values (1, "Troca de corrente", 15.00);
insert into servico values (9, "Instalação de selim", 3.00);
insert into servico values (5, "Montagem de bicicleta", 100.00);
insert into servico values (2, "Pintura", 70.00);
insert into servico values (6, "Instalação de câmbio", 40.00);
insert into servico values (7, "Revisão", 100.00);
insert into servico values (8, "Instalação de jante", 50.00);
SELECT 
    *
FROM
    servico;

delete from cliente where cpf_cliente = "10101010101";
