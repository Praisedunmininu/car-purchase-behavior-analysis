Car Purchase Behavior Analysis Using Python

📌 Overview
This project explores customer data to identify the key factors influencing car purchase amounts. The goal is to understand how different variables affect customer spending behavior and provide meaningful business insights.

📂 Dataset Description
The dataset contains 500 customer records with features including:
Age
Gender
Country
Annual Salary
Net Worth
Credit Card Debt
Car Purchase Amount

🔧 Data Preparation
Loaded dataset and handled encoding issues
Explored data using .head(), .info(), .describe()
Created new features using binning:
Car purchase categories
Age groups
Net worth groups
Credit card debt groups

📊 Exploratory Data Analysis (EDA)

1️⃣ Gender Analysis
• Gender 1 made slightly more purchases than gender 0
• Gender 0 had slightly higher average spending
• Total revenue from gender 0 was slightly higher
🌹Insight: Gender has minimal impact on car purchase behavior.


2️⃣ Net Worth Analysis
• Customers with higher net worth consistently spent more
• Clear upward trend observed across groups
🌹 Insight: Net worth is the strongest factor influencing car purchase amount.


3️⃣ Age Analysis
• Older customers tend to spend more than younger ones
• Moderate increase in spending across age groups
🌹 Insight: Age has a moderate influence on spending.


4️⃣ Country Analysis
• Some locations showed slightly higher average spending
• Differences between countries were relatively small
🌹Insight: Country has limited impact on car purchase amount.


5️⃣ Credit Card Debt Analysis
• Average spending across debt groups was very similar
• No consistent upward or downward trend observed
🌹 Insight: Credit card debt has little to no significant impact on car purchase amount.

📈 Tools Used
Python
Pandas
NumPy
Matplotlib


🎯 Key Findings
Net worth is the most important predictor of car purchase amount
Age shows a moderate relationship
Gender, country, and credit card debt have weak influence
Financial strength is a stronger driver than demographic factors

🎉 Conclusion
This analysis shows that customer financial capacity, especially net worth, plays a major role in determining car purchase behavior. Businesses should focus on high-value customers rather than relying heavily on demographic segmentation.