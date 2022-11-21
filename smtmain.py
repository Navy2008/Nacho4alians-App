#!/usr/bin/env python3

print("[*] Receiving funds.")
print("[*] this is Wallet B\n\n")


#### U3: Sending funds
print("Enter ID of the reciving wallet: ")
#wid_b = input().strip()
wid_b = "0010"
print("Enter Amount of funds to add/remove from the wallet (-XXX for remove): ")
#wid_b_amount = input().strip()
wid_b_amount = "1234"

""":counter b: counter value"""
cb = 1234

def hellofunction(z):
    """A stub function for starting the U3: sending funds function (see testcase)

    :param: z a vaule coming in (optional)

    :return: The value of the calculation for funds added or removed.
    """
    return 32


if __name__ == "__main__":

    print("\n\n\n")
    print("python main!")
    print("python main!")
    print("\n")

    print("[+] Wallet ID: " + wid_b)
    print("[+] Amount wid_b_amount: " + wid_b_amount)
    print("\n\n\n")

    initial_amount = 1235
    print("[+] Amount wid_b_amount: " + str((initial_amount + int(wid_b_amount))))
    print("\n\n\n")



    print("[+] ****** DONE. ********")

