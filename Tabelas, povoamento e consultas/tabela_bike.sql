create database oficina_bike;
use oficina_bike;

CREATE TABLE cliente (
    cpf_cliente CHAR(11) NOT NULL UNIQUE,
    nome VARCHAR(100) NOT NULL,
    telefone CHAR(8) NOT NULL,
    PRIMARY KEY (cpf_cliente)
);
    
create table funcionario(
	cpf_funcionario char(11) not null unique,
    nome varchar(100) not null,
    primary key(cpf_funcionario));
    
create table nota_fiscal(
	id_nota int not null auto_increment,
    data_emissao date not null,
    primary key(id_nota));

create table atendimento(
	id_atendimento int not null auto_increment,
    cpf_cliente char(11) not null,
    cpf_funcionario char(11) not null,
    id_nota int not null,
    primary key(id_atendimento),
    foreign key(cpf_cliente) references cliente(cpf_cliente),
    foreign key(cpf_funcionario) references funcionario(cpf_funcionario),
    foreign key(id_nota) references nota_fiscal(id_nota));
    
create table servico(
	id_atendimento int not null,
    descricao varchar(100) not null,
    preco decimal(5,2) not null,
    primary key(id_atendimento),
    foreign key(id_atendimento) references atendimento(id_atendimento));
   
create table compra(
	id_atendimento int not null,
    id_produto int not null,
    quantidade int not null,
    data_compra date not null,
    primary key(id_atendimento, id_produto),
    foreign key(id_atendimento) references atendimento(id_atendimento),
    foreign key(id_produto) references produto(id_produto));
    
create table produto(
	id_produto int not null auto_increment,
    nome varchar(30) not null,
    preco decimal(5,2) not null,
    primary key(id_produto));

create table fornecedor(
	id_fornecedor int not null auto_increment,
    nome_empresa varchar(100) not null,
    telefone char(8) not null,
    primary key(id_fornecedor));

create table fornece(
	id_produto int not null,
    id_fornecedor int not null,
    primary key(id_produto, id_fornecedor),
    foreign key(id_produto) references produto(id_produto),
    foreign key(id_fornecedor) references fornecedor(id_fornecedor));


