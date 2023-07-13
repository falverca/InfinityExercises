# Build a program that asks for the size of file to download (in MB) and the speed of an internet link (in megabits per second).
# Calculate and show the approx. download time for a file using that link (in minutes). Considere que 1 byte = 8 bits.
# Consider 1 byte = 8 bits

file_size_mb = float(input("What's the size of your file in MB? "))
internet_speed_mbps = float(input("What's your internet speed in Mbps? "))

file_size_bits = file_size_mb / 8

download_time = file_size_bits / internet_speed_mbps

print(f"The approximate download time is {download_time} minutes")