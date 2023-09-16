function [phi,duration] = traj(theta_1, theta_2, r_1, r_2, omega_2, v)
    h = 1e5;
    t_min = abs(r_1 - r_2) / v;
    t_max = (r_1 + r_2) / v;
    t = linspace(t_min, t_max, h+2);
    left = r_2*[cos(theta_2 + omega_2*t); sin(theta_2 + omega_2*t)] - r_1*[cos(theta_1); sin(theta_1)];
    left = left / v ./ t;
    left = left(:,2:end-1);
    t = t(:,2:end-1);
    dirs = [t; left];

    phi = 6;
    duration = -1;
    for i = 1:h
        dir_vec = dirs(2:3,i);
        if norm(dir_vec) < 1 && duration == -1
            phi = atan(dir_vec(2) / dir_vec(1));
            duration = dirs(1,i);
        end
    end
end