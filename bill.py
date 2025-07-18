def main():
    total_bill = int(input("Enter the total bill: "))
    
    try:
        if total_bill == 0 or total_bill < 0:
            print("Enter a valid amount")
            return
        
        people = int(input("Enter number of people: "))
        bill(total_bill, people)
    except ValueError:
        print("Invalid input.")
    
def bill(total_amount,people):    
    share = total_amount/people
    print(f"Each person should pay: {share:.2f}$")
    
main()
