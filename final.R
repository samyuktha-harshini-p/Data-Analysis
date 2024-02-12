# Load the ggplot2 library
library(ggplot2)
library(dplyr)

data <- read.csv('df_no_duplicates.csv')

# Check the structure of the loaded data
str(data)

# View the first few rows of the data
head(data)

summary(data)

data %>%
  group_by(Gender) %>%
  summarise(count = n())

data %>%
  group_by(Ethnicity) %>%
  summarise(count = n())
    
# Count the occurrences of each ethnicity
ethnicity_counts <- table(data$Ethnicity)

# Create a pie chart
pie(ethnicity_counts, labels = names(ethnicity_counts), col = rainbow(length(ethnicity_counts)),
    main = "Ethnicity Distribution")

# Add a legend
legend("topright", legend = names(ethnicity_counts), fill = rainbow(length(ethnicity_counts)))

# Create a bar plot for Gender
ggplot(data, aes(x = Gender)) +
  geom_bar(fill = "skyblue", color = "black") +
  labs(title = "Distribution of Gender", x = "Gender", y = "Count") +
  theme_minimal()

# Create a bar plot showing counts of each Ethnicity by Gender
ggplot(data, aes(x = Ethnicity, fill = Gender)) +
  geom_bar(position = "dodge") +
  labs(title = "Distribution of Gender across Ethnicities", x = "Ethnicity", y = "Count") +
  theme_minimal()

