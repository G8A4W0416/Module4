SALES_TAX = .06


def calculate_price(price, cash_coupon, percent_coupon):
    if price <= 5 and cash_coupon == 5 or price < 10 and cash_coupon == 10:
        total_price = 5.95
    else:
        deduct_cash_coupon = price - cash_coupon
        pct_coupon_amt = deduct_cash_coupon * percent_coupon
        deduct_pct_coupon = deduct_cash_coupon - pct_coupon_amt
        tax_amt = deduct_pct_coupon * SALES_TAX
        deduct_tax_amt = deduct_pct_coupon - tax_amt
        total_price = round(deduct_tax_amt + 5.95, 2)

    return total_price


if __name__ == '__main__':
    pass
