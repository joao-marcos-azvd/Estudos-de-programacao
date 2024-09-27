-- Código sqlite 🪶 pra criar a tabelas (Se ela não existir)
create table if not exists usuarios (
    -- Cria o ID 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    -- Cria o nome 
    nome TEXT NOT NULL
);
