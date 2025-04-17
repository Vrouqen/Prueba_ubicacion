USE dbIncomes;

CREATE TABLE Incomes(
    id_income INT AUTO_INCREMENT PRIMARY KEY,
    id_user INT,
    value DECIMAL(10,2),
    date DATETIME
);

CREATE TABLE Incomes_Names(
    id_name_income INT AUTO_INCREMENT PRIMARY KEY,
    id_income INT,
    name VARCHAR(50),
    CONSTRAINT income_name_FK  FOREIGN KEY (id_income) REFERENCES Incomes(id_income)
);

CREATE TABLE Type_Income(
    id_type_income INT AUTO_INCREMENT PRIMARY KEY,
    id_income INT,
    type_income VARCHAR(50),
    CONSTRAINT type_income_FK FOREIGN KEY (id_income) REFERENCES Incomes(id_income)
);