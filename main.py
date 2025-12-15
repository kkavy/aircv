from validators.technical import technical_validator

def run_aircv():
    print("AIRCV started successfully")
    
    change = "Example: Migrate on-prem server to cloud"
    
    result = technical_validator(change)
    
    print("Technical Validation Result:")
    print(result)

if __name__ == "__main__":
    run_aircv()
