-- Código MySQL🐬 pra criar a tabelas (Se ela não existir)
create table if not exists usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);
