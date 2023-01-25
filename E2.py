def main():
    hoursWorked = 0.0
    regularRate = 0.0
    overtimeRate = 0.0
    overtimePay = 0.0
    regularPay = 0.0
    grossPay = 0.0
    wHolding = 0.0
    TAX = 0.1
    BENEFITS = 0.06
    def get_hours_worked():
        hoursWorked = int(input("Enter your hours worked: "))
        return hoursWorked

    def get_hourly_rate():
        regularRate = int(input("Enter your hourly rate: "))
      
        return regularRate

    def calc_overtime(regularRate, hoursWorked):
        overtimeRate = regularRate * 1.5
        if hoursWorked > 40:
            overtimePay = (hoursWorked - 40) * overtimeRate
        else:
            overtimePay = 0
        return overtimePay

    def calc_gross_pay(regularRate, overtimePay):
        regularPay = 40 * regularRate
        grossPay = regularPay + overtimePay
        return grossPay

    def cal_taxes(grossPay):
        return TAX * grossPay

    def calc_benefits(grossPay):
        return BENEFITS * grossPay

    def calc_withholdings(grossPay):
        return cal_taxes(grossPay) + calc_benefits(grossPay)

    def calc_net_pay(grossPay, wHolding):
        return grossPay - wHolding
    

    hours = get_hours_worked()
    Rrate = get_hourly_rate()
    overPay = calc_overtime(Rrate, hours)
    gPay = calc_gross_pay(Rrate, overPay)
    wHolding = calc_withholdings(gPay)
    nPay = calc_net_pay(gPay, wHolding)
    print("The overtime pay is: ", overPay)
    print("The gross pay is: ", gPay)
    print("Withholdings is: ", wHolding)
    print("The Net Pay is: ", nPay)

    
main()