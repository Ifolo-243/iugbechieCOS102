class BudgetApp:
    def __init__(self):
        self.total_budget = 0
        self.budget_manager = None    
        self.simulator = None         
        self.root = tk.Tk()            
    
    def is_valid_number(self, text):
        if text.count('.') > 1:
            return False
        parts = text.split('.')
        return all(part.isdigit() for part in parts)

    def get_user_budget(self):
        while True:
            user_input = input("Enter your monthly budget (e.g. 5000): ")
            
            if self.is_valid_number(user_input):
                budget = float(user_input)

                if budget > 0:
                    self.total_budge = budget 
                    print(f"Budget set to ₦{budget}")
                    break
                else:
                    print("Budget must be greater than 0.")
            
            else:
                print("Invalid input. Please enter a valid number.")
            
    def setup(self):
        self.budget_manager = BudgetManager(self.total_budget)
        self.simulator = BudgetSimulator(self.budget_manager)
        self.root.title("Budget Simulator")

    def start_gui(self):
        gui = BudgetGUI(self.root, self.simulator)
        self.root.mainloop()

    def run(self):
        self.get_user_budget()
        self.setup()
        self.start_gui()

if __name__ == "__main__":
    app = BudgetApp()
    app.run()           
