x <- 10
x

x = 12
x

sqrt(9) == 3


mdlalmdm3 <- c(TRUE, FALSE, TRUE, TRUE, FALSE)
class(mdlalmdm3) 

x3 <- 1:20
class(x3)

nome <- c("Fulano", "Sicrano", "Beltrano") 
nome

altura <- c(1.72, 1.58, 1.01) 
altura

data1 <- data.frame(nome, altura, stringsAsFactors = FALSE)
data1

help(data.frame)

getwd()

list.files()

setwd("Dados")

# ADD SALVAR BASE
acidentes_transito_2016 <- read_delim("acidentes-transito-2016.csv", 
                                      ";", escape_double = FALSE, trim_ws = TRUE)

str(acidentes_transito_2016)












