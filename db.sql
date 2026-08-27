-- CREATE TABLE tabela (campo1 TIPO_DADO, campo2 TIPO_DADO2...);
-- ALTER TABLE tabela COMANDOS_ALTERACAO (campo1 TIPO_DADO1...);
-- INSERT INTO tabela (campo1,campo2...) VALUES (valorcampo1,valorcampo2...);
INSERT INTO usuario (nome,email)
VALUES ('Fernando','fernando@email.com'),
       ('Júlia','julia@email.com'),
       ('Afonso','afonso@email.com');
SELECT * FROM usuario;