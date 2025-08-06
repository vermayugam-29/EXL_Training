import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#loading csv data
df = pd.read_csv('Data/delivery_times.csv')

def plot():
    #boxplot for delivery time
    plt.figure(figsize=(12,8))
    sns.boxplot(
        x = 'Customer_Area',
        y = 'Delivery_Time_Minutes',
        data = df
    )
    plt.title('Boxplot visualization for delivery time')
    plt.xlabel('Customer Area')
    plt.ylabel('Delivery Time')
    plt.tight_layout()
    plt.show()

def cal_iqr():
    #finding iqr
    q1 = df['Delivery_Time_Minutes'].quantile(0.25)
    q3 = df['Delivery_Time_Minutes'].quantile(0.75)

    iqr = q3 - q1

    return {
        'q1' : q1, 'q3' : q3, 'iqr' : iqr
    }

def upper_lower_bounds(data):
    #finding upper_cap and lower_cap
    upper_bound = data['q3'] + 1.5 * data['iqr']
    lower_bound = data['q1'] - 1.5 * data['iqr']

    return {
        'ub' : upper_bound, 'lb' : lower_bound
    }

def flag_outliers(data):
    #adding status col to flag outliers
    df['Status'] = df['Delivery_Time_Minutes'].apply(
        lambda x : 'Outlier' if (x < data['lb']) | (x > data['ub']) else 'Normal'
    )


def print_res():
    #finding outliers
    outliers = df[df['Status'] == 'Outlier']

    print('\nNo of outliers: ', len(outliers))
    print('-------------------------------------------------------------------------')
    print('Outlier details : \n', outliers)
    print('-------------------------------------------------------------------------')

    return outliers

def final_task(outliers):
    #boxplot for outliers
    plt.figure(figsize=(10,8))
    sns.boxplot(
        x='Status',
        y='Delivery_Time_Minutes',
        data = df,
        palette=['skyblue', 'red']
    )
    plt.title('Boxplot for Outlier in red')
    plt.xlabel('Status')
    plt.ylabel('Delivery Time')
    plt.tight_layout()
    plt.show()

    #hist plot for delivery time
    plt.figure(figsize=(10,8))
    sns.histplot(
        df['Delivery_Time_Minutes'],
        bins = 10,
        kde = True
    )
    plt.title('Histogram for Delivery Times')
    plt.xlabel('Delivery Time')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

    #Group by Customer_Area and check where most outliers come from.
    cust_area_outliers = outliers['Customer_Area'].value_counts()
    print('Outliers count : \n',cust_area_outliers)
    print('-------------------------------------------------------------------------')


def main():
    plot()
    iqr_data = cal_iqr()
    up_lp_data = upper_lower_bounds(iqr_data)
    flag_outliers(up_lp_data)
    outliers = print_res()
    final_task(outliers)
    # df.to_csv('Data/modified_delivery_times.csv')
    print('\nFinal Data \n', df)

if __name__ == '__main__':
    main()