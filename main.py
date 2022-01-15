import pandas as pd

# On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one
# model of shoe. We want to do some analysis of the average order value (AOV). When
# we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13.
# Given that we know these shops are selling sneakers, a relatively affordable item,
# something seems wrong with our analysis

def main():
    df = pd.read_csv('data.csv')
    # find the average order value (AOV) using mean()
    print('average of all orders for all stores:')
    naive = df['order_amount'].mean()
    # df.groupby('shop_id').order_value.mean()
    print(f'${naive:.2f}')
    print(sorted(df['order_amount'].unique())[:5])
    print(sorted(df['order_amount'].unique())[-5:])

    # we can nullify this by removing any outliers
    # 2 standard deviations away from the mean keeps 95% of the data
    # calculate standard deviation
    std = df['order_amount'].std()
    mean = df['order_amount'].mean()
    q25, q75 = mean - std, mean + std
    # filter out any values outside of the 95% quantile
    df = df[(df['order_amount'] > q25) & (df['order_amount'] < q75)]
    # calculate the new AOV
    print('average of all orders for all stores after removing outliers:')
    print(f'${df["order_amount"].mean():.2f}')
    print(sorted(df['order_amount'].unique())[:5])
    print(sorted(df['order_amount'].unique())[-5:])

if __name__ == '__main__':
    main()
