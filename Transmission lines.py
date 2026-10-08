# Transmission-lines
print("Transmission Line Calculator")

V = float(input("Enter transmission voltage (V): "))
I = float(input("Enter line current (A): "))
R = float(input("Enter resistance of transmission line (ohm): "))

# Transmitted power
P_transmitted = V * I

# Power loss in transmission line
P_loss = I ** 2 * R

# Receiving-end power
P_received = P_transmitted - P_loss

# Transmission efficiency
efficiency = (P_received / P_transmitted) * 100

print("\n--- Transmission Line Results ---")
print("Transmitted Power =", P_transmitted, "W")
print("Power Loss =", P_loss, "W")
print("Received Power =", P_received, "W")
print("Transmission Efficiency =", efficiency, "%")
