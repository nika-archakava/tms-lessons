from random import randint
import json
import os


def get_random_digit(count):
    return ''.join([str(randint(0, 9)) for i in range(count)])


class BankAccount:
    def __init__(self, card_holder, money=0.0, card_number=None, account_number=None):
        self.card_holder = card_holder.upper()
        self.money = money
        # if self.account_number is None:
        #    self.account_number = get_random_digit(20)
        # else:
        #    self.account_number = account_number
        # if card_number is None:
        #    self.card_number = get_random_digit(16)
        # else:
        #    self.card_number = card_number
        self.card_number = get_random_digit(16) if card_number is None else card_number
        self.account_number = get_random_digit(20) if account_number is None else account_number


class Bank:
    def __init__(self, bank_accounts=None):
        # if bank_accounts is not None:
        #   self.bank_accounts = bank_accounts
        # else:
        #    self.bank_accounts: dict[str, BankAccount] = {}
        self.bank_accounts = bank_accounts or {}

    def open_account(self, card_holder):
        person = BankAccount(card_holder)
        self.bank_accounts[person.account_number] = person
        return person

    def add_money(self, account_number, money):
        self.bank_accounts[account_number].money += money

    def transfer_money(self, from_account_number, to_account_numbers, money):
        self.bank_accounts[from_account_number].money -= money
        self.bank_accounts[to_account_numbers].money += money

    def external_transfer(self, from_account_number, to_external_number, money):
        b = self.bank_accounts[from_account_number]
        b.money -= money
        print(
            f'Bank transferred {money}$ from your account{from_account_number} to external account {to_external_number}')


class Controller:
    def __init__(self, data_file_name):
        self.data_file_name = data_file_name
        bank_accounts = load_accounts(data_file_name)
        self.bank = Bank(bank_accounts)

    def run(self):
        print("Welcome to our bank!")
        while True:
            print('Choose your action:')
            print('0. Finish the program')
            print('1. Open new account')
            print('2.Look open accounts')
            print('3.Put money on account')
            print('4.Transfer money between accounts')
            print('5.Make a payment')
            answer = int(input())
            if answer == 0:
                save_accounts(self.bank.bank_accounts, self.data_file_name)
                print('Bye-bye')
                break
            elif answer == 1:
                information = input("Put the cardholder's first and last name:")
                s = self.bank.open_account(information)
                print(f'Account {s.account_number} is created')
            elif answer == 2:
                self.show_accounts()
            elif answer == 3:
                ask = input("Put the account number:")
                ask1 = float(input("Put the sum you want to add:"))
                self.bank.add_money(ask, ask1)
            elif answer == 4:
                ask = input("Enter the sender's account number:")
                ask1 = input("Enter the recipient account number:")
                ask2 = float(input("Amount of money:"))
                self.bank.transfer_money(ask, ask1, ask2)
            elif answer == 5:
                ask = input("Enter the sender's account number:")
                ask1 = input("Enter the external account number:")
                ask2 = float(input("Amount of money:"))
                self.bank.external_transfer(ask, ask1, ask2)

    def show_accounts(self):
        print("Your opened accounts:")
        for account_number, account in self.bank.bank_accounts.items():
            print(f'Account:{account_number}')
            print(f'Account balance: {account.money}$')
            print(f'Card number: {account.card_number}')
            print(f'Cardholder: {account.card_holder}')


def convert_bank_account_to_dict(person):
    return {
        'card_holder': person.card_holder,
        'money': person.money,
        'card_number': person.card_number,
        'account_number': person.account_number
    }


def save_accounts(s, file_name):
    data = {}
    for key, value in s.items():
        data[key] = convert_bank_account_to_dict(value)
    with open(file_name, 'w') as file:
        json.dump(data, file)


def load_accounts(file_name):
    if not os.path.exists(file_name):
        return {}
    with open(file_name, 'r') as file:
        return {number: BankAccount(**data) for number, data in json.load(file).items()}


if __name__ == '__main__':
    controller = Controller('data.json')
    controller.run()
