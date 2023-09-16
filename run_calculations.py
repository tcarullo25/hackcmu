import subprocess

def run_matlab_script(theta1, theta2, r1, r2, omega2, v):
    error_path = "log.txt"

    input_data = f"{theta1},{theta2},{r1},{r2},{omega2},{v}"
    with open("temp_data.csv", "w", encoding="utf-8-sig") as f:
        f.write(input_data)
    
    with open("log.txt", "w", encoding="utf-8-sig") as f:
        subprocess.run('''matlab -batch "run('calculate_trajectory.m')"''', stdout=f)
    
    with open("out.txt", "r", encoding="utf-8-sig") as f:
        out = f.read().split(",")
        phi = float(out[0])
        duration = float(out[1])
        verified = bool(out[2])
    print(f"verified: {verified}; phi = {phi}; travel time = {duration}")
    return (verified, phi, duration)



if __name__ == "__main__":
    import math
    run_matlab_script(0, math.pi/4, 1e6, 1e8, 1, 1e-4)
