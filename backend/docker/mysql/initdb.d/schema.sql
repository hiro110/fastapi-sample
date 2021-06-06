CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    token text DEFAULT NULL,
    is_active tinyint(1) NOT NULL DEFAULT true,
    is_superuser tinyint(1) NOT NULL DEFAULT false,
    created_at datetime default current_timestamp,
    updated_at timestamp default current_timestamp on update current_timestamp,
    PRIMARY KEY (id)
);