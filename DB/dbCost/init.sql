CREATE TABLE Costs(
    id_cost INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_user INT,
    value DECIMAL(10,2),
    date DATETIME
);

CREATE TABLE Costs_Names(
    id_cost_name INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_cost INT,
    name VARCHAR(50),
    CONSTRAINT cost_name_FK FOREIGN KEY (id_cost) REFERENCES Costs(id_cost)
);

CREATE TABLE Type_Cost(
    id_type_cost INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_cost INT,
    type_cost VARCHAR(50),
    CONSTRAINT type_cost_FK FOREIGN KEY (id_cost) REFERENCES Costs(id_cost)
);