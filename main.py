import random

# Generate a random 6-digit OTP
def generate_otp():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

# Simulate sending the OTP via SMS or email
def send_otp(user_phone, otp):
    print(f"Sending OTP {otp} to {user_phone}")

# Verify the entered OTP
def verify_otp(entered_otp, generated_otp):
    return entered_otp == generated_otp


if __name__ == "__main__":
    user_phone_number = "+1234567890"  # Replace with user's phone number
    generated_otp = generate_otp()

    print(f"Generated OTP: {generated_otp}")
    send_otp(user_phone_number, generated_otp)

    entered_otp = input("Enter the OTP you received: ")

    if verify_otp(entered_otp, generated_otp):
        print("OTP verification successful!")
    else:
        print("Invalid OTP. Verification failed.")
