# LinkedIn project post

🚀 **Completed a Sanctions Screening Analytics project using Microsoft Excel and Power Query concepts**

I built a portfolio project to explore how customer names can be screened against a sanctions reference list, how potential matches can be consolidated into reviewable alerts, and how the output can be evaluated using classification metrics.

### Project scope
- 500 synthetic customer records
- 50 synthetic sanctions-reference rows
- 68 candidate-level alert rows
- 49 customers with at least one candidate alert

### Tools and concepts
- Microsoft Excel
- Power Query concepts
- Name cleaning and normalization
- Fuzzy name matching
- Candidate-alert consolidation
- Data-quality assessment
- Confusion matrix and classification metrics

### Evaluation against synthetic labels
- **Precision:** 100%
- **Recall:** 98%
- **Accuracy:** 99.8%
- **F1 score:** 98.99%

The consolidated results contained 49 true positives, 0 false positives, 450 true negatives, and 1 false negative.

An important learning was that data quality directly affects screening outcomes. One synthetic customer record (`CUST045`) had a blank customer name and screening name, and remained a missed test case rather than being manually forced into a match. I also documented an incomplete sanctions-reference row and the fact that live Power Query refreshability has not yet been validated.

This project strengthened my understanding of how data preparation, fuzzy matching, alert review, and performance measurement can support KYC, AML, and financial-crime compliance operations.

📂 **GitHub repository:** [Add your repository URL]

*This is an educational project using synthetic data. Candidate alerts require human review and are not confirmed sanctions matches. The reported metrics describe this synthetic test set only.*

#DataAnalytics #Excel #PowerQuery #AML #KYC #SanctionsScreening #FinancialCrimeCompliance #DataQuality #FuzzyMatching #PortfolioProject
