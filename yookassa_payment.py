from yookassa import Configuration, Payment

# Замените YOUR_SHOP_ID и YOUR_SECRET_KEY на ваши данные из ЮKassa
Configuration.account_id = 'YOUR_SHOP_ID'
Configuration.secret_key = 'YOUR_SECRET_KEY'

def create_payment(amount, currency, description):
    payment = Payment.create({
        "amount": {
            "value": str(amount),
            "currency": currency
        },
        "payment_method_data": {
            "type": "bank_card"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://your-return-url.com"
        },
        "capture": True,
        "description": description
    })
    return payment.confirmation.confirmation_url

if __name__ == '__main__':
    amount = 500.00  # Пример суммы платежа
    currency = 'RUB'
    description = 'Подписка на автомобильного помощника'
    payment_url = create_payment(amount, currency, description)
    print(f'Payment URL: {payment_url}')
