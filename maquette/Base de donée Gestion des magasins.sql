
-- Utilisation de la base de donn�es
USE Gestion_des_Magasins;

-- Cr�ation de la table Magasin
CREATE TABLE Magasin (
    IdMagasin INT PRIMARY KEY IDENTITY (1,1),
    NomMagasin VARCHAR(255) not null,
	Adresse VARCHAR (50) not null,
    Telephone VARCHAR (15) not null,
    Email VARCHAR(50) not null
);

-- Cr�ation de la table Produit
CREATE TABLE Produit (
    IdProduit INT PRIMARY KEY IDENTITY (1,1),
    NomProduit VARCHAR(255) not null,
    CategorieProduit VARCHAR not null,
    PrixUnitaire float not null
);

