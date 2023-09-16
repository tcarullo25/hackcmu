% read inputs
inputs = readmatrix("temp_data.csv");

theta_1 = inputs(1);
theta_2 = inputs(2);
r_1 = inputs(3);
r_2 = inputs(4);
omega_2 = inputs(5);
v = inputs(6);

% run the actual traj calculation
[phi, duration] = traj(theta_1, theta_2, r_1, r_2, omega_2, v);
t = duration;

% verify results line up
p2 = [cos(theta_2 + omega_2*t); sin(theta_2 + omega_2*t)] * r_2;
s = [r_1*cos(theta_1) + v*cos(phi)*t; r_1*sin(theta_1) + v*sin(phi)*t];
v = norm((p2 - s) / t) > 1e-4;

% write to out
writematrix([phi, duration, v], "out.txt");
