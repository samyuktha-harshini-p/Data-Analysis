SELECT COUNT(*) AS Male_Count
FROM your_table_name
WHERE Gender = 'MALE' AND Year_of_Birth = 2011;

#display all entries
SELECT *
FROM your_table_name;

#to get the count of all entries
SELECT COUNT(*)
FROM your_table_name;

#to get count of all male for each year
SELECT "Year of Birth", COUNT(*) AS Male_Count
FROM your_table_name
WHERE Gender = 'MALE'
GROUP BY "Year of Birth"
ORDER BY "Year of Birth";

#to get count of all female for each year
SELECT "Year of Birth", COUNT(*) AS Female_Count
FROM your_table_name
WHERE Gender = 'FEMALE'
GROUP BY "Year of Birth"
ORDER BY "Year of Birth";


#to get entries with rank1 which gives all popular names
SELECT *
FROM your_table_name
WHERE Rank = 1;

#min-max
SELECT Year_of_Birth, Ethnicity, Gender, MIN(Count) AS Min_Count, MAX(Count) AS Max_Count
FROM your_table_name
GROUP BY Year_of_Birth, Ethnicity, Gender;

#average count
SELECT `Year of Birth`, Ethnicity, AVG(Count) AS AvgCount
FROM babynames
GROUP BY `Year of Birth`, Ethnicity
ORDER BY `Year of Birth`, Ethnicity;
