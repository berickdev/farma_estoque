create schema if not exists estoque_flet;

use estoque_flet;

create table if not exists usuarios(
	id int auto_increment primary key,
    nome varchar(100) not null,
    email varchar(100) not null unique,
    senha varchar(100) not null
);

create table if not exists produtos(
	id int auto_increment primary key,
    nome_produto varchar(100) not null,
    categoria varchar(50) not null,
    lote varchar(50) not null,
    validade date not null,
    quantidade int default 0,
    estoque_minimo int default 5
);

create table if not exists movimentacoes(
	id int auto_increment primary key,
    tipo varchar(50) not null,
    quantidade int not null,
    data_movimentacao datetime default current_timestamp,
    id_produto int,
    id_usuario int,
    foreign key (id_produto) references produtos(id),
    foreign key (id_usuario) references usuarios(id)
);

insert into usuarios (nome, email, senha)
values ("Bruno", "bruno@gmail.com", "admin123")