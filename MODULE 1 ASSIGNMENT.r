library(tidyverse)
library(readxl)
library(writexl)

first_names <- c("Yomi", "Fike", "Sayo", "Tundun", "Gbenga", "Adesola", "Tonia", "Gibson", "Toriola", "Amokachi")
last_names <- c("Nathaniel", "Anthony", "Tinubu", "Godson", "Peterson", "Adekola", "Osamudiamen", "Egetton", "Briggs", "Alabo")

employees <- data.frame(matrix(ncol = 4, nrow = 0))
colnames(employees) <- c("Full Name", "salary", "Gender", "level")

for (i in 1:400) {
  first_name <- sample(first_names, 1)
  last_name <- sample(last_names, 1)
  full_name <- paste(first_name, last_name)
  salary <- sample(3000:30000, 1)
  gender <- sample(c("Male", "Female"), 1)
  
  if (salary > 10000 & salary < 20000) {
    level <- "A1"
  } else if (salary > 7500 & salary < 30000 & gender == "Female") {
    level <- "A5-F"
  } else {
    level <- ""
  }
  
  employees[nrow(employees) + 1, ] <- c(full_name, salary, gender, level)
}

tryCatch({
  write_xlsx(employees, "employees.xlsx")
  print(employees)
}, error = function(e) {
  print("Something is wrong")
})

