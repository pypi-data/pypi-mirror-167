# **Shapiro-Francia normality test**

## Description:

The statistical test of Shapiro-Francia considers the squared correlation between the ordered sample values and the (approximated) expected ordered quantiles from the standard normal distribution. The p-value is computed from the formula given by Royston (1993).

This function performs the Shapiro-Francia test for the composite hypothesis of normality, according to Thode Jr. (2002).

## **Install**

    pip install sfrancia

## **Usage**

    from sfrancia import shapiroFrancia
    import pandas as pd

    df = pd.read_csv('fake_table.csv')

    # any array, series or list of numeric values
    shapiroFrancia(df['column'])

---

## References:

- Royston, P. (1993). A pocket-calculator algorithm for the Shapiro-Francia test for non-normality: an application to medicine. Statistics in Medicine, 12, 181-184.
- Thode Jr., H. C. (2002). Testing for Normality. Marcel Dekker, New York.
