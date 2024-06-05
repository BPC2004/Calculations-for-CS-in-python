from threading import Thread, Lock
import time

BobBalance = 1500
lock = Lock()  # Create a lock to synchronize access to BobBalance

def DeductAmount(amount):
    global BobBalance
    with lock:
        TempBalance = BobBalance
        if TempBalance >= amount:
            TempBalance -= amount
            if amount >= 1000:
                time.sleep(0.2)
            BobBalance = TempBalance
        else:
            print("Insufficient funds")

def RegisterDeduction(amount):
    transaction = Thread(target=DeductAmount, args=(amount,))
    transaction.start()
    transaction.join()  # Wait for the deduction thread to complete

RegisterDeduction(1100)
RegisterDeduction(100)
time.sleep(1)  # Wait for the deduction requests to complete
print(BobBalance)  # This should output the updated balance
