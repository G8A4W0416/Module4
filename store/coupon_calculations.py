SALES_TAX = .06


def calculate_price(price, cash_coupon, percent_coupon):
    shipping = 0.00

    if price < 10:
        shipping = 5.95
    elif 10 <= price < 30:
        shipping = 7.95
    elif 30 <= price < 50:
        shipping = 11.95

    if price <= cash_coupon:
        total_price = shipping
    else:
        deduct_cash_coupon = price - cash_coupon
        pct_coupon_amt = deduct_cash_coupon * percent_coupon
        deduct_pct_coupon = deduct_cash_coupon - pct_coupon_amt
        tax_amt = deduct_pct_coupon * SALES_TAX
        add_tax_amt = deduct_pct_coupon + tax_amt
        total_price = round(add_tax_amt + shipping, 2)

    return total_price


if __name__ == '__main__':
    pass
